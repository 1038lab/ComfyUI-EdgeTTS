import os
import edge_tts
import asyncio
import re
import torch
import torchaudio
import nest_asyncio
import json

nest_asyncio.apply()

class EdgeTTS:
    """
    A simplified Edge TTS node for ComfyUI
    Uses Microsoft Edge's online text-to-speech service
    Outputs standard ComfyUI audio format
    """
    
    @staticmethod
    def load_voices():
        """Load available voices from config file"""
        try:
            config_path = os.path.join(os.path.dirname(__file__), "config.json")
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                voices = []
                tooltips = {}
                
                default_voice = config.get("default_voice")
                
                for language, voice_list in config["edge_tts_voices"].items():
                    for voice, description in voice_list:
                        voices.append(voice)
                        tooltips[voice] = f"{language}: {description}"

                if default_voice in voices:
                    voices.remove(default_voice)
                    voices.insert(0, default_voice)
                
                return voices, tooltips
        except:
            return (
                ["zh-CN-XiaoxiaoNeural", "en-US-JennyNeural", "ja-JP-NanamiNeural"],
                {
                    "zh-CN-XiaoxiaoNeural": "Chinese: Female, cheerful",
                    "en-US-JennyNeural": "English: Female, casual",
                    "ja-JP-NanamiNeural": "Japanese: Female, natural"
                }
            )
    
    DEFAULT_VOICES, VOICE_TOOLTIPS = load_voices.__func__()
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "placeholder": "Enter text to convert to speech"}),
                "voice": (s.DEFAULT_VOICES, {"default": s.DEFAULT_VOICES[0], "tooltip": "Select a voice for text-to-speech"}),
            },
            "optional": {
                "speed": ("FLOAT", {"default": 1.0, "min": 0.5, "max": 2.0, "step": 0.1, "tooltip": "Speech rate (0.5 to 2.0)"}),
                "pitch": ("INT", {"default": 0, "min": -20, "max": 20, "step": 1, "tooltip": "Voice pitch adjustment (-20 to +20 Hz)"})
            }
        }
    
    RETURN_TYPES = ("AUDIO",)
    FUNCTION = "tts"
    CATEGORY = "🧪AILab/🔊Audio"

    async def generate_speech(self, text, voice, speed, pitch):
        """Generate speech from text using Edge TTS"""
        speed_percent = int((speed - 1.0) * 100)
        rate = "+0%" if speed_percent == 0 else f"{speed_percent:+d}%"
        
        temp_file = f"temp_tts_{os.getpid()}.wav"
        try:
            communicate = edge_tts.Communicate(
                text=text,
                voice=voice,
                rate=rate,
                pitch=f"{pitch:+d}Hz"
            )
            await communicate.save(temp_file)
            
            waveform, sample_rate = torchaudio.load(temp_file)
            if waveform.shape[0] > 1:
                waveform = waveform.mean(dim=0, keepdim=True)
            waveform = waveform / (waveform.abs().max() + 1e-6)
            return {"waveform": waveform.unsqueeze(0), "sample_rate": sample_rate}
                
        finally:
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except:
                    pass

    def tts(self, text, voice, speed=1.0, pitch=0):
        """Convert text to speech"""
        if not text.strip():
            raise ValueError("Text is empty")
            
        # Clean text
        text = re.sub(r'\s+', ' ', text).strip()
        
        try:
            audio_data = asyncio.run(self.generate_speech(text, voice, speed, pitch))
            return (audio_data,)
        except Exception as e:
            print(f"TTS Error: {str(e)}")
            raise e

NODE_CLASS_MAPPINGS = {
    "EdgeTTS": EdgeTTS
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EdgeTTS": "Edge TTS 🔊"
} 