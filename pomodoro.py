#coding:utf-8

WORK_TIME = 25
BREAK_TIME = 5

import sys
import time
import emoji
from mutagen.mp3 import MP3 as mp3
import pygame

args = sys.argv

def get_args(string = '-4'):
    return abs(int(string))

def get_attention():
    for i in range(3):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','\a')
        time.sleep(0.3)

def bell():
    filename = 'bell.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    mp3_length = mp3(filename).info.length
    pygame.mixer.music.play(1)
    time.sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

def pomodoro(times):
    done = 0
    while(True):
        input('Are you ready?? Press any key')
        print ('Focus on your task',done+1, '/', times,'...')
        for count in range(5):
            time.sleep(WORK_TIME * 60 / 5)
            print(emoji.emojize(':tomato:',use_aliases=True)*(count+1))
        done += 1

        if times == done:
            bell()
            print("You've done!")
            break

        bell()
        input('Have you done?? Press any key')
        print (BREAK_TIME,' min break time...')
        for count in range(5):
            time.sleep(BREAK_TIME * 60 / 5)
            print(emoji.emojize(':zzz:',use_aliases=True)*(count+1))
        bell()

if __name__ == '__main__':
    try:
        times = get_args(args[1])
    except:
        times = get_args()

    pomodoro(times)
