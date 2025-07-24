# ComfyUI-EdgeTTS V1.2.1
# A simplified Edge TTS node for ComfyUI
# Uses Microsoft Edge's online text-to-speech service
# Outputs standard ComfyUI audio format

import os
import edge_tts
import asyncio
import re
import torch
import torchaudio
import json

class EdgeTTS:
    _voice_data_cache = None

    @classmethod
    def get_voice_data(cls):
        if cls._voice_data_cache is None:
            cls._voice_data_cache = cls.load_voices()
        return cls._voice_data_cache

    @staticmethod
    def load_voices():

        try:
            config_path = os.path.join(os.path.dirname(__file__), "config.json")
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                voices = []
                tooltips = {}
                voice_ids = {}
                
                default_voice = config.get("default_voice")
                default_display_name = None
                
                for language, voice_list in config["edge_tts_voices"].items():
                    for voice, description in voice_list:
                        parts = voice.split('-')
                        if len(parts) >= 3:
                            lang_name = language.split('-')[0] if '-' in language else language
                            display_name = f"[{lang_name}] {parts[0]}-{parts[1]} {parts[-1].replace('Neural', '').replace('Multilingual', '')}"
                        else:
                            display_name = voice
                        voices.append(display_name)
                        tooltips[display_name] = f"{language}: {description}"
                        voice_ids[display_name] = voice
                        
                        if voice == default_voice:
                            default_display_name = display_name

                if default_display_name and default_display_name in voices:
                    voices.remove(default_display_name)
                    voices.insert(0, default_display_name)
                
                return voices, tooltips, voice_ids
        except:
            return (
                ["[English] en-US Jenny", "[Chinese] zh-CN Xiaoxiao", "[Japanese] ja-JP Nanami"],
                {"[English] en-US Jenny": "English-US: Female, casual", "[Chinese] zh-CN Xiaoxiao": "Chinese-Mainland: Female, cheerful", "[Japanese] ja-JP Nanami": "Japanese: Female, natural"},
                {"[English] en-US Jenny": "en-US-JennyNeural", "[Chinese] zh-CN Xiaoxiao": "zh-CN-XiaoxiaoNeural", "[Japanese] ja-JP Nanami": "ja-JP-NanamiNeural"}
            )
    
    @property
    def DEFAULT_VOICES(self):
        return self.get_voice_data()[0]

    @property
    def VOICE_TOOLTIPS(self):
        return self.get_voice_data()[1]

    @property
    def VOICE_IDS(self):
        return self.get_voice_data()[2]
    
    @classmethod
    def INPUT_TYPES(cls):
        voices, _, _ = cls.get_voice_data()
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "placeholder": "Enter text to convert to speech"}),
                "voice": (voices, {"default": voices[0], "tooltip": "Select a voice for text-to-speech"}),
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
            text = text.strip()
            if not text:
                raise ValueError("Input text cannot be empty")

            communicate = edge_tts.Communicate(
                text=text,
                voice=voice,
                rate=rate,
                pitch=f"{pitch:+d}Hz"
            )
            
            try:
                await communicate.save(temp_file)
            except edge_tts.exceptions.NoAudioReceived:

                default_display_name = self.DEFAULT_VOICES[0]
                default_voice = self.VOICE_IDS.get(default_display_name, default_display_name)
                
                if voice != default_voice:
                    print(f"Warning: Failed with voice {voice}, trying default voice {default_voice}")
                    communicate = edge_tts.Communicate(
                        text=text,
                        voice=default_voice,
                        rate=rate,
                        pitch=f"{pitch:+d}Hz"
                    )
                    await communicate.save(temp_file)
                else:
                    raise
            
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
            raise ValueError("Text cannot be empty")
            
        text = re.sub(r'\s+', ' ', text).strip()
        actual_voice = self.VOICE_IDS.get(voice, voice)
        
        try:
            import concurrent.futures
            
            def run_async_in_thread():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                return loop.run_until_complete(self.generate_speech(text, actual_voice, speed, pitch))
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                audio_data = executor.submit(run_async_in_thread).result()
                
            return (audio_data,)
        except Exception as e:
            print(f"TTS Error: {str(e)}")
            empty_waveform = torch.zeros((1, 1, 16000))
            return ({"waveform": empty_waveform, "sample_rate": 16000},)

NODE_CLASS_MAPPINGS = {
    "EdgeTTS": EdgeTTS
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EdgeTTS": "Edge TTS 🔊"
} 
