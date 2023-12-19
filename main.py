import wikipedia
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
wel= print("Welcome")
speak.Speak("welcome")

for i in range(10000000):
    pass
pgm=print("This program will provide you summary of any Hollywood Movie")
speak.Speak("This program will provide you summary of any Hollywood Movie")

for i in range(10000000):
    pass
prop=print("you should write the name properly")
speak.Speak("you should write the name properly")
for i in range(10000000):
    pass
try:
    while True:
        speak.Speak("Type the name of movie")
        a=input("Type the name of movie\n")
        print("wait for a sec")
        #speak.Speak("Type the name of movie")
        b= f"{a},'anime'"
        summ=wikipedia.summary(b,sentences=4)
        print(summ)
        speak.Speak(summ)
        check=input("press n to konw about another movie")
        if check=='n':
            continue
        print('have a good day \n project work by:\n vinit')
        break
except:
    print("you might have entered wrong name")

