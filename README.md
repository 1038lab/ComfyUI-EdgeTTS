# ComfyUI-EdgeTTS

<p align="center">
  <img src="https://img.shields.io/badge/ComfyUI-Custom--Node-blue?style=for-the-badge&logo=comfyui" alt="ComfyUI">
  <img src="https://img.shields.io/badge/PyTorch-%3E=2.0-red?style=for-the-badge&logo=pytorch" alt="PyTorch">
  <img src="https://img.shields.io/badge/License-GPL--3.0-green?style=for-the-badge" alt="GPL-3.0">
</p>

ComfyUI-EdgeTTS is a powerful text-to-speech node for ComfyUI, leveraging Microsoft's Edge TTS capabilities. It enables seamless conversion of text into natural-sounding speech, supporting multiple languages and voices. Ideal for enhancing user interactions, this node is easy to integrate and customize, making it perfect for various applications.

https://github.com/user-attachments/assets/a5b9165b-a413-49fd-989e-0ef3141afce7

## News & Updates
- **2026/10/13**: Update ComfyUI-EdgeTTS to **v2.0.0** ( [update.md](update.md#v200-20261013) )
- **2026/01/25**: Update ComfyUI-EdgeTTS to **v1.2.2** ( [update.md](update.md#v122-2026125) )
- **2025/07/23**: Update ComfyUI-EdgeTTS to **v1.2.1** ( [update.md](update.md#v121-2025723) )
- **2025/06/20**: Update ComfyUI-EdgeTTS to **v1.2.0** ( [update.md](update.md#v120-2025620) )
- **2025/01/24**: Update ComfyUI-EdgeTTS to **v1.1.0** ( [update.md](update.md#v110-2025124) )

## Features

### Edge TTS Node
- **Edge TTS**: Convert text to speech using Microsoft Edge TTS
  - Multiple languages and voices support
  - Adjustable speech rate and pitch
  - High-quality voice synthesis
  - Configurable via config.json

### Speech to Text Node
- **Whisper STT**: High-accuracy speech recognition
  - Multiple language support with auto-detection
  - Multiple model sizes (tiny to large)
  - Dual output: raw transcription text (`TEXT`) and timecoded subtitles (`SRT`)
  - Supports ComfyUI audio format
  - Language detection confidence reporting

### Audio File Node
- **Save Audio**: Export audio files
  - Supports WAV, MP3, FLAC formats
  - Quality presets (high/medium/low)
  - Custom file naming and paths
  - Automatic file numbering

## Installation

### Method 1. install on ComfyUI-Manager, search `Comfyui-EdgeTTS` and install
install requirment.txt in the ComfyUI-EdgeTTS folder
  ```bash
  ./ComfyUI/python_embeded/python -m pip install -r requirements.txt
  ```

### Method 2. Clone this repository to your ComfyUI custom_nodes folder:
  ```bash
  cd ComfyUI/custom_nodes
  git clone https://github.com/1038lab/ComfyUI-EdgeTTS.git
  ```
  install requirment.txt in the ComfyUI-EdgeTTS folder
  ```bash
  ./ComfyUI/python_embeded/python -m pip install -r requirements.txt
  ```
## Requirements
- Python packages (see `requirements.txt`)
- FFmpeg on system `PATH` (required by Whisper STT)
  - Example (Windows PowerShell): `$env:Path += ";F:\\FFmpeg\\bin"` then restart ComfyUI
- CUDA compatible GPU (optional, for faster Whisper processing)

> [!NOTE]
> ### Important: torchaudio 2.9+ requires torchcodec
> If you use `torch/torchaudio` 2.9 or newer, `torchaudio.load/save` requires `torchcodec`.

Recommended fix (match PyTorch 2.9.x):
```bash
./ComfyUI/python_embeded/python -m pip uninstall -y torchcodec
./ComfyUI/python_embeded/python -m pip install --no-cache-dir "torchcodec==0.9"
```

### Text to Speech
1. Add Edge TTS node to workflow
2. Input text and select voice
3. Adjust speed and pitch if needed
4. Connect to Save Audio node for export  

![edgeTTS](https://github.com/user-attachments/assets/4eb75f7e-72ee-4b69-8de5-6ca436f1e043)

### Speech to Text
1. Add Whisper STT node
2. Connect audio input
3. Select model size and language (or auto-detect)
4. Run to get transcription

![TTS-STT](https://github.com/user-attachments/assets/9e7367c0-4da1-47e5-b831-1cbb3419273a)

## Supported Voices

| Language | Female Voices | Male Voices |
|----------|--------------|-------------|
| Chinese-Mainland | XiaoXiao (News, Novel, Warm), XiaoYi (Cartoon, Novel, Lively) | Yunjian (Sports, Novel, Passion), Yunxi (Novel, Lively), Yunxia (Cartoon, Novel), Yunyang (News, Professional) |
| Chinese-Cantonese | HiuGaai (Friendly), HiuMaan (Friendly) | WanLung (Friendly) |
| Chinese-Taiwan | HsiaoChen (Friendly), HsiaoYu (Friendly) | YunJhe (Friendly) |
| English-US | Jenny (Friendly), Aria (Positive), Ana (Cute), Michelle (Friendly) | Guy (Passion), Christopher (Authority), Eric (Rational), Roger (Lively), Steffan (Rational) |
| English-GB | Libby (Friendly), Maisie (Friendly), Sonia (Friendly) | Ryan (Friendly), Thomas (Friendly) |
| English-AU | Natasha (Friendly) | William (Friendly) |
| Japanese | Nanami (Friendly) | Keita (Friendly) |
| Korean | SunHi (Friendly) | InJoon (Friendly), Hyunsu (Multilingual) |
| French-FR | Denise (Friendly), Eloise (Friendly), Vivienne (Multilingual) | Henri (Friendly), Remy (Multilingual) |
| French-CA | Sylvie (Friendly) | Jean (Friendly), Antoine (Friendly) |
| German-DE | Katja (Friendly), Amala (Friendly), Seraphina (Multilingual) | Conrad (Friendly), Killian (Friendly), Florian (Multilingual) |

More voices available in config.json, including voices for:
- German (AT/CH)
- Spanish (ES/MX)
- Russian
- Italian
- Portuguese (BR/PT)
- Dutch
- Polish
- Turkish
- Arabic
- Hindi
- Indonesian
- Vietnamese
- Thai
- Ukrainian
And many more...

Each language provides at least one male and female voice option, allowing you to choose different voice styles based on your needs. 

## Credits
- Edge TTS: [Microsoft Edge TTS](https://github.com/rany2/edge-tts)
- Whisper: [OpenAI Whisper](https://github.com/openai/whisper)
