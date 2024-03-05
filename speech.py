# # #pip install SpeechRecognition
# # #pip install pyaudio
import speech_recognition as sr

# # To list all available microphones
# index = 0
# for name in sr.Microphone.list_microphone_names():
#     print(index, name)
#     index = index + 1

def mic():
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=0) as source:
            if source is None:
                print("Microphone source is None")
                return
            
            print("Say something: ")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            print("Recognizing...")
            text = r.recognize_google(audio)
            print("TEXT: " + text)
            return text
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    except Exception as e:
        print("Exception: " + str(e))

#mic()
if __name__ == "__main__":
    mic() # Test the mic function