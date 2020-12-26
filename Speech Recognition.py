import speech_recognition as sr

def recognize():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        # r.pause_threshold = 1
        # r.energy_threshold = 45.131829621150224
        # print(sr.Microphone.list_microphone_names())
        #print(r.energy_threshold)
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query= r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return None
    return query 

if __name__=="__main__":
    vishal=recognize()

    print(vishal)