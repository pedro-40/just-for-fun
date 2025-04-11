import time
import pygame
from os import system ,name,chdir
from colorama import Fore 

while True:

    if name=="nt":
        system("cls")
    else:
        system("clear")

    choice=input(Fore.RED+"Do you want to start the timer? (y/n)" )
    if 'y' == choice.lower():
        h=int(input(Fore.GREEN+"how many hours... "))
        m=int(input("a few minutes... "))
        s=int(input("a few seconds..."))
        i=input("enter music directory...")
        M=input("music name ...")

        if h < 0 or m < 0 or s < 0:
            print(Fore.RED+"please enter a positive number...")
            time.sleep(5)
            if name=="nt":
                system("cls")
            else:
                system("clear")
            continue
        
        if s >= 60:
            w = s // 60
            m += w
            s= s - (w*60)
      
        if m >= 60:
            e= m // 60
            h += e
            m = m -(e*60)
        print(Fore.CYAN+f"{h} hours : {m} minutes : {s} seconds")
        total=h*3600+m*60+s
        print("The timer starts after 10 seconds. :)")
        time.sleep(10)
        while total > 0 :
            if name =="nt":
                system("cls")
            else:
                system("clear")            
            print(Fore.MAGENTA+f"secondes :{total}")
            total -= 1
            time.sleep(1)
        while total == 0 :
            if name =="nt":
                system("cls")
            else:
                system("clear") 
            chdir(i)
            pygame.mixer.init()
            sound=pygame.mixer.Sound(M)
            sound.play()
            e=input(Fore.BLUE+"for off enter y ...")
            if "y"==e.lower() :
                pygame.mixer.quit()
                break
              
    elif 'n' == choice.lower() :
        if name=="nt":
            system("cls")
        else:
            system("clear")
        break
    
    else:
        print("this choice is not in choices ... ")
        time.sleep(5)
        if name=="nt":
            system("cls")
        else:
            system("clear")
