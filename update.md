# ComfyUI-EdgeTTS Update Log

## v1.2.1 (2025/7/23)

### Voice ID Compatibility Fix
- Fixed 12 invalid voice IDs that were no longer available in Edge TTS API
- Updated multilingual voices to their standard counterparts:
  - `en-GB-AdaMultilingualNeural` → `en-GB-LibbyNeural`
  - `en-GB-OllieMultilingualNeural` → `en-GB-RyanNeural`
  - `en-AU-WilliamNeural` → `en-AU-WilliamMultilingualNeural`
  - `ja-JP-MasaruMultilingualNeural` → `ja-JP-KeitaNeural`
  - `es-ES-IsidoraMultilingualNeural` → `es-ES-XimenaNeural`
  - `es-ES-ArabellaMultilingualNeural` → `es-ES-XimenaNeural`
  - `es-ES-TristanMultilingualNeural` → `es-ES-XimenaNeural`
  - `es-MX-PelayoNeural` → `es-MX-DaliaNeural`
  - `it-IT-IsabellaMultilingualNeural` → `it-IT-GiuseppeMultilingualNeural`
  - `it-IT-MarcelloMultilingualNeural` → `it-IT-GiuseppeMultilingualNeural`
  - `it-IT-AlessioMultilingualNeural` → `it-IT-GiuseppeMultilingualNeural`
  - `pt-BR-MacerioMultilingualNeural` → `pt-BR-ThalitaMultilingualNeural`

### Event Loop Handling Improvement
- Fixed issue with asyncio event loop in EdgeTTS node
- Improved compatibility with ComfyUI's main event loop
- Added thread isolation for TTS processing
- Resolved deadlock issues when generating speech

### Documentation Update
- Added complete voice list documentation
- Updated voice compatibility information
- Added detailed voice characteristics for all languages
- Improved troubleshooting section
- 
## v1.2.0 (2025/6/20)

### Voice Display Enhancement
- Improved voice name format for better readability
  - Before: `zh-CN-XiaoxiaoNeural` → After: `[Chinese] zh-CN Xiaoxiao`
  - Before: `en-US-JennyNeural` → After: `[English] en-US Jenny`
- All voices now display in `[Language] locale VoiceName` format

### Performance Optimization
- Added lazy loading for voice data
- Faster ComfyUI startup time
- Reduced memory usage when EdgeTTS not in use
- Voice data cached after first load

### Added Multilingual Voices
- Chinese-Mainland:
  - zh-CN-XiaoxiaoMultilingualNeural: Female, Friendly, Positive
  - zh-CN-YunfanMultilingualNeural: Male, Friendly, Positive
  - zh-CN-YunxiaoMultilingualNeural: Male, Friendly, Positive
- English-US:
  - en-US-AvaMultilingualNeural: Female, Expressive, Caring, Pleasant, Friendly
  - en-US-AndrewMultilingualNeural: Male, Warm, Confident, Authentic, Honest
  - en-US-EmmaMultilingualNeural: Female, Cheerful, Clear, Conversational
  - en-US-BrianMultilingualNeural: Male, Approachable, Casual, Sincere
- English-GB:
  - en-GB-AdaMultilingualNeural: Female, Friendly, Positive
  - en-GB-OllieMultilingualNeural: Male, Friendly, Positive
- Japanese:
  - ja-JP-MasaruMultilingualNeural: Male, Friendly, Positive
- Korean:
  - ko-KR-HyunsuMultilingualNeural: Male, Friendly, Positive
    
## v1.1.0 (2025/1/24)

### Voice Statistics
- This update adds 19 new languages and 38 new voices.
- A total of 46 language categories and 114 voices are now supported.
- The proportion of new voices accounts for approximately a 33.3% increase.

### Voice Categories Restructuring
- Reorganized Chinese voices into more specific categories:
  - Chinese-Mainland: Standard Mandarin
  - Chinese-Cantonese: Hong Kong Cantonese
  - Chinese-Taiwan: Taiwan Mandarin
  - Chinese-Dialect: Regional dialects

- Split English voices into regional variants:
  - English-US: American English
  - English-GB: British English
  - English-AU: Australian English

- Split French voices into regional variants:
  - French-FR: France French
  - French-CA: Canadian French
  - French-CH: Swiss French

- Split German voices into regional variants:
  - German-DE: Germany German
  - German-AT: Austrian German
  - German-CH: Swiss German

- Split Spanish voices into regional variants:
  - Spanish-ES: Spain Spanish
  - Spanish-MX: Mexican Spanish

- Split Portuguese voices into regional variants:
  - Portuguese-BR: Brazilian Portuguese
  - Portuguese-PT: Portugal Portuguese

### Chinese Voice Updates
- Added more detailed characteristics for existing Chinese voices
  - XiaoxiaoNeural: Added "News, Novel" traits
  - XiaoyiNeural: Added "Cartoon, Novel" traits
  - YunjianNeural: Added "Sports, Novel" traits
  - YunxiNeural: Added "Novel" trait
  - YunxiaNeural: Added "Cartoon, Novel" traits
  - YunyangNeural: Added "News" trait
  - liaoning-XiaobeiNeural: Added "Dialect" trait
  - shaanxi-XiaoniNeural: Added "Dialect" trait

### New Language Support
- Added support for new languages:
  1. Bengali (India)
     - BashkarNeural (Male)
     - TanishaaNeural (Female)
  
  2. Malay
     - OsmanNeural (Male)
     - YasminNeural (Female)
  
  3. Tamil (India and Singapore)
     - PallaviNeural (Female, IN)
     - ValluvarNeural (Male, IN)
     - AnbuNeural (Male, SG)
     - VenbaNeural (Female, SG)
  
  4. Telugu
     - MohanNeural (Male)
     - ShrutiNeural (Female)
  
  5. Marathi
     - AarohiNeural (Female)
     - ManoharNeural (Male)
  
  6. Swahili
     - ZuriNeural (Female)
     - RafikiNeural (Male)
  
  7. Persian
     - DilaraNeural (Female)
     - FaridNeural (Male)

2. Vietnamese
   - HoaiMyNeural (Female)
   - NamMinhNeural (Male)

2. Thai
   - NiwatNeural (Male)
   - PremwadeeNeural (Female)

3. Ukrainian
   - OstapNeural (Male)
   - PolinaNeural (Female)

4. Greek
   - AthinaNeural (Female)
   - NestorasNeural (Male)

5. Czech
   - AntoninNeural (Male)
   - VlastaNeural (Female)

6. Finnish
   - HarriNeural (Male)
   - NooraNeural (Female)

7. Danish
   - ChristelNeural (Female)
   - JeppeNeural (Male)

8. Norwegian
   - FinnNeural (Male)
   - PernilleNeural (Female)

9. Swedish
   - MattiasNeural (Male)
   - SofieNeural (Female)

10. Romanian
    - AlinaNeural (Female)
    - EmilNeural (Male)

11. Slovak
    - LukasNeural (Male)
    - ViktoriaNeural (Female)

12. Slovenian
    - PetraNeural (Female)
    - RokNeural (Male)

### Notes
- All new voices maintain consistent description format: "Friendly, Positive"
- Regional variants now clearly indicated in category names
- All voices support Neural engine technology
- Each language typically includes at least one male and one female voice
- Current voice distribution covers major world languages and regional variants 
