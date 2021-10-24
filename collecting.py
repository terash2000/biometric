import pynput
from pynput.keyboard import Key, Listener
import csv
import time
from os import path

global userName
global lastKeyTime
userFilePath = 'Collecting_keyStorke.csv'
keys = []
lastKey = ''
   
def on_press(key):
    if key == Key.enter:
        print(keys)
        userRecordData(keys)
        return False

    global lastKey
    global lastKeyTime

    if lastKey != '':
        keys.append((userName, lastKey, key, time.time() - lastKeyTime))
    lastKey = key
    lastKeyTime = time.time()

def userRecordData(eventList):
    with open(userFilePath,'a',newline='\n') as f:
        writer = csv.writer(f)
        writer.writerows(eventList)
    f.close()   
    
def getUserName():
    global userName
    userName = input('Enter your Name: ')

def initCsv():
    if not path.exists(userFilePath):
        userRecordData([('username', 'key1', 'key2', 'time')])

initCsv()
getUserName()
print('Enter your text: ')
with Listener(on_press = on_press) as listener:
    listener.join()
