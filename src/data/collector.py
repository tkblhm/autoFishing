from pyautogui import screenshot
from pynput import keyboard, mouse
from time import sleep

# 0: init, 1: to-fish, 2: fishing, 3: catched, 4: quit
state = 0
catches = []
capacity = 3
pause = 0.1

def on_press(key):
    global state
    print("on_press: ", key)
    if (key == '[' and state == 0):
        state = 1
    elif (key == ']' and state != 0):
        state = 0
    elif (key == keyboard.Key.esc and state == 0):
        state = 4

def on_click(x, y, button, pressed):
    global state
    print("on_click: ", x, y, button, pressed)
    if (state == 1 or state == 3) and button == mouse.Button.right:
        state = 2

    elif (state == 2 and button == mouse.Button.right):
        state = 3
        catches.append(str(last))


with open("../record.txt", "r") as file:
    last = int(file.readline().rstrip("\n"))
    catches.append(file.readline())

with mouse.Listener(on_click=on_click) as mouse_listener:
    with keyboard.Listener(on_press=on_press) as key_listener:
        while True:
            if state == 2:
                screenshot(f"../imgs/{last}.png")
                last += 1
            elif state == 4:
                with open("../record.txt", "w") as file:
                    file.write(str(last) + "\n")
                    file.write(" ".join(catches) + "\n")
                break
            sleep(pause)




