from pynput import keyboard
import pyautogui
import os

SCROLL_AMOUNT = 300

def on_press(key):
    try:
        # "=" scrolls down
        if key.char == "=":
            pyautogui.scroll(-SCROLL_AMOUNT)

        # "-" scrolls up
        elif key.char == "-":
            pyautogui.scroll(SCROLL_AMOUNT)

    except AttributeError:
        # END key exits the script
        if key == keyboard.Key.end:
            print("Closing...")
            os._exit(0)

print("Running...")
print("=  -> scroll down")
print("-  -> scroll up")
print("END -> exit")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
