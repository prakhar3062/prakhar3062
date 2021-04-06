import pywhatkit 
import pyttsx3
import speech_recognition as sr

listener=sr.Recognizer()
engine=pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait() 

def get_info():
     try:
         with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
     except:
        pass  
phone_list={'bhai':'+916307132218','suryash':'+917518321657','moshi':'+917651883102','himanshu':'+919695161972','manager':'+917906399125',}

def get_email_info():
    talk('To Whom you want to send message')
    name = get_info()
    recceiver= phone_list[name] 
    print(recceiver) 
    talk('what message you want to sent')
    message=get_info() 
    send(recceiver,message) 
    talk('Hey lazy ass. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()  
def send(recceiver,message):
 pywhatkit.sendwhatmsg(recceiver,message,18,55,wait_time=3,print_waitTime=True) 


get_email_info()
