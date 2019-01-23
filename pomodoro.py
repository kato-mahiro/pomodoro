#coding:utf-8

import sys
import time
import emoji

args = sys.argv

def get_args(string = '-4'):
    return abs(int(string))

def get_focus():
    print('\a')
    for i in range(3):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        time.sleep(1)

def pomodoro(times):
    done = 0
    while(True):
        print ('Focus on your task',done+1, '/', times,'...')
        for count in range(5):
            time.sleep(1)
            print(emoji.emojize(':tomato:',use_aliases=True))
        done += 1

        if times == done:
            print("You've done!")
            break

        get_focus()

        print ('5 min break time...')
        for count in range(5):
            time.sleep(1)
            print(emoji.emojize(':zzz:',use_aliases=True))

        get_focus()

if __name__ == '__main__':
    try:
        times = get_args(args[1])
    except:
        times = get_args()

    pomodoro(times)

