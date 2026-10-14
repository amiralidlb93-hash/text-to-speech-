import os
import re
import sys
import subprocess
import traceback

try:
    import tkinter as tk
    from tkinter import ttk, messagebox
except ImportError:
    print("tkinter is not installed. Linux: sudo apt install python3-tk")
    sys.exit(1)

ALL_LANGS = {
    "فارسی": "fa", "English": "en", "Azərbaycan dili": "az", "Türkçe": "tr",
    "Русский": "ru", "العربية": "ar", "Français": "fr", "Español": "es",
    "Deutsch": "de", "Italiano": "it", "中文": "zh", "日本語": "ja",
}

WIN = sys.platform.startswith("win")
MAC = sys.platform == "darwin"
NOWIN = 0x08000000 if WIN else 0
proc = None
killed = False


def run(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           encoding="utf-8", errors="replace",
                           creationflags=NOWIN)
        return r.stdout or ""
    except FileNotFoundError:
        return ""


def find_espeak():
    for exe in ("espeak-ng", "espeak"):
        out = run([exe, "--voices"])
        if out:
            return exe, out
    return None, ""


def installed_langs():
    found = set()
    if WIN:
        ps = ("Add-Type -AssemblyName System.Speech;"
              "$s = New-Object System.Speech.Synthesis.SpeechSynthesizer;"
              "$s.GetInstalledVoices() | ForEach-Object { $_.VoiceInfo.Culture.Name }")
        out = run(["powershell", "-NoProfile", "-Command", ps])
        for name in out.split():
            found.add(name.split("-")[0].lower())
    elif MAC:
        out = run(["say", "-v", "?"])
        for m in re.finditer(r"\b([a-z]{2,3})_[A-Z]{2}\b", out):
            found.add(m.group(1))
    else:
        exe, out = find_espeak()
        for line in out.splitlines()[1:]:
            parts = line.split()
            if len(parts) > 1:
                found.add(parts[1].split("-")[0].lower())
    return found


def start(text, lang):
    kw = dict(stderr=subprocess.PIPE, text=True,
              encoding="utf-8", errors="replace")
    if WIN:
        ps = ("Add-Type -AssemblyName System.Speech;"
              "$s = New-Object System.Speech.Synthesis.SpeechSynthesizer;"
              "$p = $env:TTS_LANG + '*';"
              "$v = $s.GetInstalledVoices() | Where-Object "
              "{ $_.VoiceInfo.Culture.Name -like $p } | Select-Object -First 1;"
              "if (-not $v) { [Console]::Error.WriteLine('No voice for this language'); exit 2 };"
              "$s.SelectVoice($v.VoiceInfo.Name); $s.Speak($env:TTS_TEXT)")
        env = dict(os.environ, TTS_TEXT=text, TTS_LANG=lang)
        return subprocess.Popen(["powershell", "-NoProfile", "-Command", ps],
                                env=env, creationflags=NOWIN, **kw)
    if MAC:
        voice = None
        for line in run(["say", "-v", "?"]).splitlines():
            if re.search(r"\b" + lang + r"_[A-Z]{2}\b", line):
                voice = re.split(r"\s{2,}", line)[0].strip()
                break
        cmd = ["say"]
        if voice:
            cmd += ["-v", voice]
        return subprocess.Popen(cmd + [text], **kw)
    exe, _ = find_espeak()
    if not exe:
        raise RuntimeError("espeak-ng is not installed.\nsudo apt install espeak-ng")
    return subprocess.Popen([exe, "-v", lang, text], **kw)


def watch(p):
    if p.poll() is None:
        root.after(300, lambda: watch(p))
        return
    if p.returncode != 0 and not killed and p is proc:
        err = (p.stderr.read() or "").strip() or "error code: " + str(p.returncode)
        messagebox.showwarning("Playback error", err)


def stop():
    global killed
    if proc is not None and proc.poll() is None:
        killed = True
        proc.terminate()


def play():
    global proc, killed
    stop()
    text = box.get("1.0", "end").strip()
    if not text:
        return
    killed = False
    try:
        proc = start(text, LANGS[combo.get()])
        watch(proc)
    except Exception:
        messagebox.showerror("Error", traceback.format_exc())


root = tk.Tk()
root.title("Text to Speech")
root.geometry("520x360")

LANGS = {n: c for n, c in ALL_LANGS.items() if c in installed_langs()}
if not LANGS:
    messagebox.showerror(
        "No voices found",
        "No voices found on your system.\n"
        "Windows: Settings > Time & language > Speech\n"
        "Linux: sudo apt install espeak-ng")
    sys.exit()

box = tk.Text(root, font=("Tahoma", 13), wrap="word", height=10)
box.pack(fill="both", expand=True, padx=10, pady=10)

bar = ttk.Frame(root)
bar.pack(pady=(0, 10))
combo = ttk.Combobox(bar, values=list(LANGS), state="readonly", width=18)
combo.current(0)
combo.pack(side="left", padx=5)
ttk.Button(bar, text="Play", command=play).pack(side="left", padx=5)
ttk.Button(bar, text="Stop", command=stop).pack(side="left", padx=5)

root.mainloop()