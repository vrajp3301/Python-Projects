import speech_recognition as sr

r=sr.Recognizer()

a=sr.AudioFile('2.wav')
with a as source :
	audio=r.record(source)

text=r.recognize_google(audio)


file1=open(r"C:\Users\ADMIN\Desktop\Python\2.txt","a")
file1.writelines(text)
file1.close()