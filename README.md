# Multilingual Text to Speech

A simple, free text-to-speech tool. Type any text, pick a language, and listen. No install, no account, no API key.

**Live demo:** https://amiralidlb93-hash.github.io/text-to-speech-/

## Features

- Reads any text you type, in 14 languages: Persian, English, Azerbaijani, Turkish, Russian, Arabic, French, Spanish, German, Italian, Chinese, Japanese, Korean, Hindi
- Adjustable speech speed, plus pause and stop controls
- Automatic right-to-left layout for Persian and Arabic text
- Light and dark mode
- Runs entirely in your browser. Your text is never sent to any server by this project
- Includes an optional offline desktop version written in Python

## Usage

### Web version

Open the live demo, or open `index.html` in any modern browser. Type your text, choose a language, and press **Play**.

The page uses the browser's built-in [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis), so the available voices depend on your browser and operating system. Microsoft Edge and Chrome usually offer the widest language coverage, including Persian and Azerbaijani. If no voice exists for a language, the page shows a notice and may fall back to a default voice.

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
