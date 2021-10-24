import pynput
from pynput.keyboard import Key, Listener
import pandas as pd
import time

global userName
global lastKeyTime
userFilePath = 'Collecting_keyStorke.csv'
keys = []
lastKey = ''

def getResult():
    data = pd.read_csv(userFilePath)
    averageTime = data.groupby(['username', 'key1', 'key2']).mean().time
    allUsers = data.username.drop_duplicates().reset_index(drop=True)
    result = ''
    minDistance = float('inf')
    for i in allUsers:
        distance = 0
        for j in range(len(keys)):
            distance += (keys[j][2] - averageTime[i, str(keys[0][0]), str(keys[0][1])])**2
        if distance < minDistance:
            minDistance = distance
            result = i

    print('you are', result)
   
def on_press(key):
    if key == Key.enter:
        getResult()
        return False
    
    global lastKey
    global lastKeyTime

    if lastKey != '':
        keys.append((lastKey, key, time.time() - lastKeyTime))
    lastKey = key
    lastKeyTime = time.time()

print("Enter your text: ")
with Listener(on_press = on_press) as listener:
    listener.join()
