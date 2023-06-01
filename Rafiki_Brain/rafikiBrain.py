import json
import pyttsx3
import speech_recognition as sr
import pyaudio
import random
import os
from vosk import Model, KaldiRecognizer
from datetime import datetime
todays_time = datetime.now()
engine = pyttsx3.init()
# vosk-model-small-en-us-0.15
model = Model(r"D:\ypthon\umande AI\Rafiki_Brain\en-us-0.15")
recognizer = KaldiRecognizer(model,17000)
# recognizer = KaldiRecognizer(model,16000)
mic = pyaudio.PyAudio()
f = open('intents.json')
data = json.load(f)
# stream = mic.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
# stream = mic.open(format=pyaudio.paInt16, channels=1, rate=19000, input=True, frames_per_buffer=9192)
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
intentListData = data['intents']


class brain:
    # global greet
    greet = True
    yournames = ""
    def speak(variable):
        # rate = engine.getProperty('rate')
        engine.setProperty('rate', 180)
        # engine.setProperty('rate', 200)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        print("Speak..")
        engine.say(variable)
        engine.runAndWait()

    def answer_question(chekIndexResponses):
        count_index_responses = 0
        for i in intentListData:
            check_each_responses = i['responses']
            if chekIndexResponses == count_index_responses:
                listLen = len(check_each_responses) - 1
                chooseRandomResponse = random.randint(0,listLen)
                check_context = i['context']
                brain.speak(check_each_responses[chooseRandomResponse])
                if check_context[0] != "":
                    call_context = "brain." + check_context[0]
                    eval(call_context+"()")
                    break
            count_index_responses+=1
            # break

    def ask_question(chekIndexPatterns):
        count_index_patterns = 0
        for i in intentListData:
            check_each_patterns = i['patterns']
            for eachlistPatterns in check_each_patterns:
                eachList_patterns = eachlistPatterns.lower()
                if chekIndexPatterns == eachList_patterns:
                    brain.answer_question(count_index_patterns)
                    break
            count_index_patterns+=1 

    def to_do_list():
        todo_file = open("Rafiki_Brain/asset/todoList.txt","r")
        brain.speak("what do you want to do ")
        brain.speak("to read or to write ")
        
        while True:
            recognizerMyvoice = brain.voice_from_mic()
            print(recognizerMyvoice)
            if recognizerMyvoice == "read" or recognizerMyvoice == "to read":
                while True:
                    ToDo = todo_file.readline()
                    if ToDo == "":
                        brain.speak("your to do list is done")
                        brain.speak("do you need anything else from this to do list")
                        while True:
                            recognizerMyvoice = brain.voice_from_mic()
                            if recognizerMyvoice == "yes" or recognizerMyvoice == "yah" or recognizerMyvoice == "yap":
                                brain.speak("ok tell me")
                                break
                            elif recognizerMyvoice == "no" or recognizerMyvoice == "nop" or recognizerMyvoice == "no no":
                                brain.speak("ok ")
                                brain.main()
                            
                        
                    brain.speak(ToDo)
            if recognizerMyvoice =="to write" or recognizerMyvoice =="write":
                brain.speak("yuo whant to write what my frend")
                brain.main()
            
    def reboot():
        brain.speak("are you sure you want to reboot")
        while True:
            recognizerMyvoice = brain.voice_from_mic()
            print(recognizerMyvoice)
            if recognizerMyvoice == "yes" or recognizerMyvoice == "yap" or recognizerMyvoice == "yeah":
                brain.speak("your pc is going to restart now")
                brain.speak("see you next time")
                os.system('cmd /c "shutdown /r -t 0"')
                break
            if recognizerMyvoice == "no" or recognizerMyvoice == "nop":
                brain.speak("ok")
                break
               
    def bye():
        brain.speak("bye")
        os.system('cmd "exit()"')
    def welcome():
        if brain.greet == True:
            if todays_time.hour >=5 and todays_time.hour <= 11:
                brain.speak(" bye the way good morning")
                while True:
                    mic = brain.voice_from_mic()
                    print(mic)
                    if mic == "morning" or  mic == "good morning" or mic == "good morning to":
                        brain.speak("how do you feel")
                        brain.main()
                        # 
                    elif mic == "good morning how are you":
                        brain.speak("am also fine")
                        brain.main()
                brain.greet = False
            elif todays_time.hour >=9 and todays_time.hour <= 11:
                brain.speak("but is it morning or afternoon, but welcome again")
                brain.greet = False
            else:
                brain.speak("how is your day")
                while True:
                    mic = brain.voice_from_mic()
                    print(mic)
                    if mic == "it's fine" or mic == "it is fine"or mic == "fine" or mic == "it's good" or mic == "it is good" or mic == "are fine" or mic == "are good" or mic == "good" or mic == "nice":
                        brain.speak("am happy to hear that")
                        while True:
                            mic = brain.voice_from_mic()
                            if mic == "ok" or mic == "okay" or mic == "all right" or mic == "right":
                                brain.speak("ok what can i help you")
                                brain.greet = False
                                brain.main()
                            print(mic)
                            
                    if mic == "bad" or mic == "not good" or mic == "it's bad" or mic == "it is bad":
                        brain.speak("don't worry everything will be ok")
                        while True:
                            mic = brain.voice_from_mic()
                            if mic == "ok" or mic == "okay" or mic == "all right" or mic == "right":
                                brain.speak("ok what can i help you")
                                brain.greet = False
                                brain.main()
                            print(mic)
    def yourname():
        if brain.yournames == "":
            while True:
                brain.speak("what is your name ")
                name = brain.voice_from_mic()
                print(name)
                if name != "" or name != "huh":
                    brain.speak(f'so {name} is  your name')
                    while True:
                        mic = brain.voice_from_mic()
                        print(mic)
                        if mic =="yes" or mic =="yah" or mic =="yap" or mic =="yeah" or mic =="right":
                            brain.yournames = name
                            brain.speak(f'nice to know you {name}')
                            brain.speak(f'how can i help you {name}')
                            brain.main()
                        if mic =="no" or mic =="nop" or mic =="nai":
                            brain.speak(f'ok tell me again')
                            break
        else:
            brain.speak(f'are your ok {brain.yournames}')
                    
                
    def voice_from_mic():
        try:
            while True:
                data = stream.read(9096)
                if recognizer.AcceptWaveform(data):
                    text = recognizer.Result()
                    return text[14:-3]
        except sr.UnknownValueError:
            print("exit")
        except sr.RequestError:
            print(sr.RequestError)

    def main():
        try:
            while True:
                data = stream.read(9096)
                # data = stream.read(4096)
                if recognizer.AcceptWaveform(data):
                    text = recognizer.Result()
                    print(text[14:-3])
                    brain.ask_question(text[14:-3])
        except sr.UnknownValueError:
            print("exit")
        except sr.RequestError:
            print(sr.RequestError)


if __name__ == "__main__":
    brain.main()
f.close()
