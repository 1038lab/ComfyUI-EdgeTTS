import torchaudio
import os
from datetime import datetime
import re
from comfy.cli_args import args
import folder_paths

class Save_Audio:
    """
    Save Audio node for ComfyUI
    Default save path: /output/TTS/{date}/TTS-xxxx.{format}
    """
    
    AUDIO_FORMATS = ["wav", "mp3", "flac"]
    QUALITY_PRESETS = ["high", "medium", "low"]
    
    QUALITY_SETTINGS = {
        "high": (320, 48000),
        "medium": (192, 44100),
        "low": (128, 32000)
    }

    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { 
                "audio": ("AUDIO", ),
                "filepath": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "custom_path/filename",
                    "tooltip": "by default, the audio will be saved to output/TTS/{date}/TTS-xxxx.{format}"
                }),
                "format": (s.AUDIO_FORMATS, {"default": "mp3"}),
                "quality": (s.QUALITY_PRESETS, {"default": "high"}),
                "overwrite": ("BOOLEAN", {"default": False})
            },
        }

    RETURN_TYPES = ("STRING", "AUDIO",)
    RETURN_NAMES = ("filepath", "audio",)
    FUNCTION = "save_audio"
    OUTPUT_NODE = True
    CATEGORY = "🧪AILab/🔊Audio"

    def get_next_number(self, base_path, filename):
        pattern = re.compile(rf"{filename}-(\d+)\.\w+$")
        existing_numbers = []
        
        if os.path.exists(base_path):
            for file in os.listdir(base_path):
                match = pattern.match(file)
                if match:
                    existing_numbers.append(int(match.group(1)))
        
        return 1 if not existing_numbers else max(existing_numbers) + 1

    def save_audio(self, audio, filepath="", format="mp3", quality="high", overwrite=False):
        try:
            # Setup save path
            current_date = datetime.now().strftime("%Y-%m-%d")
            file_dir = os.path.join("TTS", current_date)
            filename = "TTS"
            
            if filepath.strip():
                file_dir, custom_filename = os.path.split(filepath.strip().strip('/'))
                if custom_filename:
                    filename = custom_filename
            
            full_dir = os.path.join(self.output_dir, file_dir)
            os.makedirs(full_dir, exist_ok=True)

            # Get quality settings and filename
            bitrate, sample_rate = self.QUALITY_SETTINGS[quality]
            final_filename = f"{filename}.{format}" if overwrite else \
                           f"{filename}-{self.get_next_number(full_dir, filename):04d}.{format}"
            save_path = os.path.join(full_dir, final_filename)

            # Process audio
            waveform = audio["waveform"]
            if waveform.dim() == 3:
                waveform = waveform.squeeze(0)

            # Resample if needed
            if sample_rate != audio["sample_rate"]:
                waveform = torchaudio.transforms.Resample(
                    audio["sample_rate"], 
                    sample_rate
                )(waveform)

            # Save audio
            torchaudio.save(save_path, waveform, sample_rate, format=format)

            results = [{
                "filename": final_filename,
                "subfolder": file_dir,
                "type": self.type
            }]

            print(f"Audio saved to: {save_path}")
            return (save_path, audio, { "ui": { "audio": results } })

        except Exception as e:
            print(f"Error saving audio: {str(e)}")
            return ("", audio, { "ui": { "audio": [] } })

NODE_CLASS_MAPPINGS = {
    "Save_Audio": Save_Audio
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Save_Audio": "Save Audio 🔊"
}
