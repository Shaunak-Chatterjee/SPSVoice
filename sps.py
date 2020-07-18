import random
import speech_recognition as sr
from time import sleep
u_score=0
c_score=0
def input_speech():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak your choice from stone,paper,scisssors\n")
        r.adjust_for_ambient_noise(source, duration=5)
        try:
            audio=r.listen()
            text=r.recognize_google(audio)
            print("{}".format(text))
            return format(text)
        except:
            print("\nSorry could not recognize your voice\n")
choice_list = ["stone","paper","scissors"]
def print_slow(txt):
    for x in txt:
        print(x,end="",flush=True)
        sleep(0.15)
def check_win(x,y):
    global u_score,c_score
    if (x==0 and y==1) or (x==1 and y==0):
        print_slow("\nPaper Wins \n")
        if(x==1):
            u_score=u_score+1
        else:
            c_score=c_score+1
    elif (x==1 and y==2) or (x==2 and y==1):
        print_slow("\nScissors Wins \n")
        if(x==2):
            u_score=u_score+1
        else:
            c_score=c_score+1
    elif (x==0 and y==2) or (x==2 and y==0):
        print_slow("\nStone Wins \n")
        if(x==0):
            u_score=u_score+1
        else:
            c_score=c_score+1
    else:
        print_slow("\nIts a Tie\n")

while u_score!=5 or c_score!=5:
    choice = input_speech()
    #input("\nEnter your choice from stone,paper,scisssors > ")
    try:
        usr=choice_list.index(choice)
        com=random.randint(0,2)
        print_slow(choice_list.__getitem__(usr)+" VS "+choice_list.__getitem__(com))
        check_win(usr,com)
        print_slow("Score\nUser: "+str(u_score)+"\nComputer: "+str(c_score)) 
    except ValueError as identifier:
        print("\nPlease enter input correctly\n")
    