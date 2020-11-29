import pyttsx3

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)
# print(voices[].id)
# print(voices)
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
# print(rate)
engine.setProperty('rate', 170)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print(volume)                          #printing current volume level
engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1


def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.
    # engine.save_to_file("speakModule.mp3")
    engine.stop()

if __name__=="__main__" :
    speak("\nCode With Harry")