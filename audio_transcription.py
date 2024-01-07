import speech_recognition as sr
import random

kelime_cevap = {"papatya" : "Daisy", "bisiklet" : "bicycle", "çiçek" : "flower"}
kelimeler = ["papatya","bisiklet","çiçek"]
kelime = random.choice(kelimeler)

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Bu kelimeyi ingilizce telaffuz edin " + kelime)
    audio = r.listen(source)

try:
    if r.recognize_google(audio, language="en-Gb") == kelime_cevap[kelime]:
        print(f"Doğru telafuz ettiniz! {kelime} : {kelime_cevap[kelime]} " + "sizin cevabınız: " + str({r.recognize_google(audio, language="en-Gb")}))
    else:
        print(f"Yanlış telafuz ettiniz! {kelime} : {kelime_cevap[kelime]} " + "sizin cevabınız: " + str({r.recognize_google(audio, language="en-Gb")}))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
