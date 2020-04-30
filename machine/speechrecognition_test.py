import speech_recognition as sr
r=sr.Recognizer()
print(sr.__version__)
harvard=sr.AudioFile('C:/Users/CL/Desktop/学习/python/machine/English.wav')
with harvard as source:
    audio=r.record(source)
#输出audio文件类型
#type(audio)
#text=r.recognize_google(audio)
print(type(audio))