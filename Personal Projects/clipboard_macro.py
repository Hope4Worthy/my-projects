from pynput import keyboard
import os

keyboard_obj = keyboard.Controller()
write_flag = False

clip_1 = ""
clip_2 = ""
clip_3 = ""
clip_4 = ""
clip_5 = ""


def read_selection():
    return os.popen("xsel").read()


def copy_f1():
    global clip_1
    global write_flag
    if not write_flag:
        clip_1 = read_selection()


def paste_f1():
    global clip_1
    global write_flag
    write_flag = True
    keyboard_obj.type(clip_1)
    write_flag = False


def copy_f2():
    global clip_2
    global write_flag
    if not write_flag:
        clip_2 = read_selection()


def paste_f2():
    global clip_2
    global write_flag
    write_flag = True
    keyboard_obj.type(clip_2)
    write_flag = False


def copy_f3():
    global clip_3
    global write_flag
    if not write_flag:
        clip_3 = read_selection()


def paste_f3():
    global clip_3
    global write_flag
    write_flag = True
    keyboard_obj.type(clip_3)
    write_flag = False


def copy_f4():
    global clip_4
    global write_flag
    if not write_flag:
        clip_4 = read_selection()


def paste_f4():
    global clip_4
    global write_flag
    write_flag = True
    keyboard_obj.type(clip_4)
    write_flag = False


def copy_f5():
    global clip_5
    global write_flag
    if not write_flag:
        clip_5 = read_selection()


def paste_f5():
    global clip_5
    global write_flag
    write_flag = True
    keyboard_obj.type(clip_5)
    write_flag = False


with keyboard.GlobalHotKeys(
    {
        "<ctrl>+<alt>+1+c": copy_f1,
        "<ctrl>+<alt>+1+v": paste_f1,
        "<ctrl>+<alt>+2+c": copy_f2,
        "<ctrl>+<alt>+2+v": paste_f2,
        "<ctrl>+<alt>+3+c": copy_f3,
        "<ctrl>+<alt>+3+v": paste_f3,
        "<ctrl>+<alt>+4+c": copy_f4,
        "<ctrl>+<alt>+4+v": paste_f4,
        "<ctrl>+<alt>+5+c": copy_f5,
        "<ctrl>+<alt>+5+v": paste_f5,
    }
) as h:
    h.join()
