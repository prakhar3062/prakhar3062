import winsound 
from win10toast import ToastNotifier 

def timer(reminder,seconds):
    notification=ToastNotifier()
    notification.show_toast("Reminder","""Alarm will go off in (seconds) Seconds.""",duration=20) 
    notification.show_toast("Reminder",reminder,duration=20)
    #alarm
    frequency=2500
    duration=1000
    winsound.Beep(frequency,duration)

if __name__=='__main__':
    words=input("what do you want to remind of: ")
    sec=int(input("Enter seconds"))
    timer(words,sec) 
    a=input()
