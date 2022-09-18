from gtts import gTTS
from playsound import playsound

#영어 문장
# text = 'Can I help you?'
file_name = 'sample.mp3'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)

#한글 문장
text = '안녕하세요'
tts_ko = gTTS(text=text,lang='ko')
tts_ko.save(file_name)


playsound(file_name) #.mp3 파일 재생