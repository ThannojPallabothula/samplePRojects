import googletrans
import speech_recognition
import speech_recognition as sr
import gtts
import playsound


#print(googletrans.LANGUAGES)
recognizer = speech_recognition.Recognizer()
with sr.Microphone() as source:
    print("speak now")
    voice = recognizer.listen(source)
    listen = recognizer.recognize_google(voice,language = "en")
    print(listen)

translator = googletrans.Translator()
translate = translator.translate(listen,dest = "fr")
print(translate.text)

converted_audio = gtts.gTTS(translate.text,lang="fr")
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")



