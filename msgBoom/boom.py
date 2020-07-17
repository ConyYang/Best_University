"""
1. How to enter msg How to choose object: control keyboard
2. Get location of the chat box: control mouse clip
3. Send message: mock enter key
4. send in loop:
"""

from pynput.keyboard import Key, Controller as key_cl
from pynput.mouse import Button, Controller as mouse_cl
import time


def keyboard_input(string):
    keyboard = key_cl()
    keyboard.type(string)


def mouse_click():
    mouse = mouse_cl()
    mouse.press(Button.left)
    mouse.release(Button.left)


def send_message(number, string):
    print('Will send message in 3s...')
    time.sleep(5)

    for i in range(number):
        keyboard = key_cl()

        keyboard_input(string)
        mouse_click()
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print('%d times'%i)


send_message(10, 'Laile')




