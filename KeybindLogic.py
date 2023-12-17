from pynput import keyboard
from pynput.keyboard import Key, Listener
import os
import sys


openTheWindow=False #variable for when to launch the window
defaultKeys=[Key.cmd, Key.ctrl_l, Key.alt_l]
customKeys=[Key.cmd, Key.ctrl_l, Key.alt_l] #TODO-make custom keys a list saved in the device
areCustomKeysEnabled=False #variable for whether custom keys are enabled or not

pressed={} #declare the list with all the pressed keys-and whether they are set to True or False
print("starting the program") #for debug stuff

def IsKeyPressed(key): #check if key is in in the list, then return it's value to avoid null references
    if key in pressed:
        return pressed[key]
    return False
    
def AreAllKeysPressed(listToCheck): #returns True if all the keys in the given list were pressed, and False otherwise
    for keys in listToCheck:
        if not IsKeyPressed(keys):
            return False
    return True     
  
def OnPress(key): #gets called whenever a key of from the keyboard is pressed
    if key not in pressed: #key was never pressed before, add it to the pressed variable
        pressed[key] = False
    
    if not pressed[key]: #if the key was not already set to pressed, set it to True
        pressed[key] = True
        print('Key %s was pressed' % key)
    
    isCustomKeyPressed = AreAllKeysPressed(customKeys)
    isDefaultKeyPressed = AreAllKeysPressed(defaultKeys)
    isKeybindPressed = isCustomKeyPressed if areCustomKeysEnabled else isDefaultKeyPressed

    if isKeybindPressed:
        print("open window")

def OnRelease(key): #gets called whenever a key from the keyboard is released
    pressed[key]=False
    print('Key %s released' %key)

with keyboard.Listener(on_press=OnPress, on_release=OnRelease) as listener:
    listener.join()