# Multilingual Text to Speech

A simple, free text-to-speech tool. Type any text, pick a language, and listen. No install, no account, no API key.

**Live demo:** `https://amiralidlb93-hash.github.io/text-to-speech-/

## Features

- Reads any text you type. The language list shows only the languages that have a voice installed on your device (out of Persian, English, Azerbaijani, Turkish, Russian, Arabic, French, Spanish, German, Italian, Chinese, Japanese, Korean, Hindi)
- Adjustable speech speed, plus pause and stop controls
- Automatic right-to-left layout for Persian and Arabic text
- Light and dark mode
- Runs entirely in your browser. Your text is never sent to any server by this project
- Includes an optional offline desktop version written in Python

## Usage

### Web version

Open the live demo, or open `index.html` in any modern browser. Type your text, choose a language, and press **Play**.

The page uses the browser's built-in [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis), so the available voices depend on your browser and operating system. The language dropdown is built automatically from the voices available on your device, so you only see languages that will actually work. Microsoft Edge and Chrome usually offer the widest coverage. Install more voices in your OS settings and reload the page to see more languages.

### Desktop version (Python)

`texttospeech.py` is a small Tkinter app that uses voices already installed on your system. It needs no `pip install`.

```bash
python texttospeech.py
```

- **Windows:** uses the built-in speech engine. Add more voices under *Settings > Time & language > Speech*.
- **macOS:** uses the built-in `say` command.
- **Linux:** requires `espeak-ng` (`sudo apt install espeak-ng`) and `python3-tk`.

The app lists only the languages that have an installed voice on your system. Windows and macOS usually have no offline Persian or Azerbaijani voice, so use the web version in Edge for those.

## Deploy on GitHub Pages

1. Push these files to a GitHub repository.
2. Go to **Settings > Pages**.
3. Under **Source**, choose **Deploy from a branch**, select `main` and the `/ (root)` folder, then save.
4. After a minute, the site is live at `https://<your-username>.github.io/<repo-name>/`.

## Project structure

```
index.html        Web app (HTML, CSS and JavaScript in one file)
texttospeech.py   Optional desktop app (Python, Tkinter)
LICENSE           MIT License
README.md         This file
```

## License

Released under the [MIT License](LICENSE).

---

<div dir="rtl">

## توضیحات فارسی

این پروژه یک ابزار ساده و رایگان برای تبدیل متن به گفتار است. متن را می‌نویسید، زبان را انتخاب می‌کنید و برنامه آن را می‌خواند. نیازی به نصب برنامه، ساخت حساب کاربری یا کلید API نیست.

### ⚠️ نکته‌ی مهم: زبان باید روی سیستم شما وجود داشته باشد

این برنامه خودش صدا ندارد و از **صداهایی که روی سیستم‌عامل یا مرورگر شما نصب است** استفاده می‌کند. بنابراین:

- فقط زبان‌هایی در لیست نمایش داده می‌شوند که صدای آن‌ها روی دستگاه شما نصب باشد.
- اگر زبانی در لیست نیست، یعنی صدای آن روی سیستم شما وجود ندارد.
- هر دستگاه لیست متفاوتی می‌بیند. مثلاً Edge و Chrome معمولاً زبان‌های بیشتری دارند.
- ویندوز و مک معمولاً صدای آفلاین برای فارسی و آذربایجانی ندارند. برای این دو زبان از مرورگر Edge استفاده کنید.

### اضافه کردن زبان‌های بیشتر

- **ویندوز:** تنظیمات ← Time & language ← Speech ← Add voices
- **مک:** تنظیمات ← Accessibility ← Spoken Content ← System Voice ← Manage Voices
- **لینوکس:** نصب `espeak-ng` با دستور `sudo apt install espeak-ng`

بعد از نصب صدا، صفحه را دوباره بارگذاری کنید (یا نسخه‌ی پایتون را دوباره اجرا کنید) تا زبان جدید در لیست بیاید.

### نحوه‌ی استفاده

- **نسخه‌ی وب:** فایل `index.html` را در مرورگر باز کنید، یا از لینک GitHub Pages استفاده کنید.
- **نسخه‌ی پایتون:** دستور `python texttospeech.py` را اجرا کنید. این نسخه فقط به کتابخانه‌های خود پایتون نیاز دارد.

### مجوز

این پروژه با مجوز MIT منتشر شده است. می‌توانید آزادانه از آن استفاده کنید، تغییرش دهید و منتشرش کنید.

</div>
