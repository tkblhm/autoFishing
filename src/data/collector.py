from pyautogui import screenshot
from pynput import keyboard, mouse

# 0: init, 1: to-fish, 2: fishing, 3: catched
state = 0
buffer = []
def on_press(key):
    print("on_press: ", key)
    if (key == keyboard.Key.esc):
        return False

def on_click(x, y, button, pressed):
    print("on_click: ", x, y, button, pressed)

with mouse.Listener(on_click=on_click) as mouse_listener:
    with keyboard.Listener(on_press=on_press) as key_listener:
        # while True:
        #     if state == 2:
        #         screenshot().
        #         screenshot("../imgs/no-action")
        key_listener.join()



