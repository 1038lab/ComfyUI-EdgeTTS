import os
import torch
import torchaudio
import whisper
import json

class WhisperSTT:
    """
    A simplified STT node for ComfyUI
    Uses Whisper for speech recognition
    """
    
    WHISPER_MODELS = ["tiny", "base", "small", "medium", "large"]
    
    @staticmethod
    def load_languages():
        try:
            config_path = os.path.join(os.path.dirname(__file__), "config.json")
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)["whisper_languages"]
        except:
            return {
                "auto": "Auto Detect",
                "en": "English",
                "zh": "Chinese",
                "ja": "Japanese"
            }
    
    LANGUAGES = load_languages.__func__()
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "audio": ("AUDIO",),
                "model_size": (s.WHISPER_MODELS, {
                    "default": "base",
                    "tooltip": "Whisper model size - larger = more accurate but slower"
                }),
                "language": (list(s.LANGUAGES.keys()), {
                    "default": "auto",
                    "tooltip": "Select language or auto for automatic detection"
                })
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "stt"
    CATEGORY = "🧪AILab/🔊Audio"

    def stt(self, audio, model_size="base", language="auto"):
        temp_file = f"temp_stt_{os.getpid()}.wav"
        try:
            waveform = audio["waveform"]
            if waveform.dim() == 3:
                waveform = waveform.squeeze(0)
            torchaudio.save(temp_file, waveform, audio["sample_rate"])
            
            model = whisper.load_model(model_size)
            result = model.transcribe(
                temp_file,
                language=None if language == "auto" else language
            )

            if language == "auto":
                detected_lang = result.get("language", "unknown")
                confidence = result.get("language_probability", 0.0)
                print(f"[Whisper STT] Detected: {detected_lang} (conf: {confidence:.2f})")
            
            return (result["text"].strip(),)
                
        except Exception as e:
            print(f"[Whisper STT] Error: {str(e)}")
            raise e
            
        finally:
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except:
                    pass

NODE_CLASS_MAPPINGS = {
    "WhisperSTT": WhisperSTT
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WhisperSTT": "Whisper STT 👂"
} 