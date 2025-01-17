# ComfyUI Audio Nodes

ComfyUI-EdgeTTS is a powerful text-to-speech node for ComfyUI, leveraging Microsoft's Edge TTS capabilities. It enables seamless conversion of text into natural-sounding speech, supporting multiple languages and voices. Ideal for enhancing user interactions, this node is easy to integrate and customize, making it perfect for various applications.

![edgeTTS](https://github.com/user-attachments/assets/4eb75f7e-72ee-4b69-8de5-6ca436f1e043)

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
- Python packages (see requirements.txt)
- CUDA compatible GPU (optional, for faster Whisper processing)

## Usage Examples
https://github.com/user-attachments/assets/a5b9165b-a413-49fd-989e-0ef3141afce7
### Text to Speech
1. Add Edge TTS node to workflow
2. Input text and select voice
3. Adjust speed and pitch if needed
4. Connect to Save Audio node for export

### Speech to Text
1. Add Whisper STT node
2. Connect audio input
3. Select model size and language (or auto-detect)
4. Run to get transcription

## Supported Voices

| Language | Female Voices | Male Voices |
|----------|--------------|-------------|
| **Main Languages** |
| Chinese | XiaoXiao (Cheerful), XiaoYi (Warm) | Yunjian (Formal), Yunxi (Casual), Yunxia (Warm), Yunyang (Pro) |
| English | Jenny (Casual), Aria (Pro), Sonia (GB), Natasha (AU) | Guy (Casual), Davis (Pro), Ryan (GB), William (AU) |
| Japanese | Nanami (Natural), Aoi (Cheerful) | Keita (Formal) |
| Korean | SunHi (Warm) | InJoon (Formal) |
| **European Languages** |
| French | Denise (Pro) | Henri (Formal) |
| German | Katja (Clear) | Conrad (Pro) |
| Spanish | Elvira (Warm) | Alvaro (Friendly) |
| Russian | Svetlana (Pro) | Dmitry (Formal) |
| Italian | Elsa (Warm) | Diego (Formal) |
| Portuguese | Francisca (BR), Raquel (PT) | Antonio (BR) |
| Dutch | Colette (Warm) | Maarten (Formal) |
| Polish | Zofia (Natural) | Marek (Formal) |
| Turkish | Emel (Warm) | Ahmet (Formal) |
| **Asian Languages** |
| Arabic | Zariyah (Warm) | Hamed (Formal) |
| Hindi | Swara (Warm) | Madhur (Formal) |
| Indonesian | Gadis (Warm) | Ardi (Formal) |

Each language provides at least one male and female voice option, allowing you to choose different voice styles based on your needs. 

## Credits
- Edge TTS: [Microsoft Edge TTS](https://github.com/rany2/edge-tts)
- Whisper: [OpenAI Whisper](https://github.com/openai/whisper)
