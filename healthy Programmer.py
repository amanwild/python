from datetime import datetime
from time import time
from pygame import init, mixer

def music_on_loop(file ,s):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    print("hello")
    while True:
        a=str(input())
        if a==s:
            mixer.music.stop()
            break

def log_now(msg):
    with open("health.txt" ,"a")as f:
        f.write(f"{msg} {datetime.now()} \n")

if __name__=='__main__':  
    init_water = time()
    init_eye = time()
    init_ex = time()
    watersecs= 45*60
    eyesecs= 60*60
    exsecs= 50*60
    print("here")
    while True:
        if time()-init_water > watersecs:
            print("water time")
            music_on_loop("music.mp3","s")
            init_water = time()
            log_now("drank water at ")
        if time()-init_eye > eyesecs:
            print("eye time")
            music_on_loop("music.mp3","s")
            init_eye = time()
            log_now("eye care at ")
        if time()-init_ex > exsecs:
            print("exercise  time")
            music_on_loop("music.mp3","s")
            init_ex = time()
            log_now("drank exsecs at ")


