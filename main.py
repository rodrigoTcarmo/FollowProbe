import tkinter
from window_engine.window_engine import InterfaceEngine


def welcome_back():
    return "Hi sir, welcome back yo python!"


def init_window():
    InterfaceEngine(tkinter.Tk()).window_starter()


if __name__ == "__main__":
    init_window()
    # url="www.instagram.com"
    # print(welcome_back())
    # open_webpage(url)
