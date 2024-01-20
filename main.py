from screen_engine.screen_engine import open_webpage
from window_engine.window_engine import WindowEngine


def welcome_back():
    return "Hi sir, welcome back yo python!"


def init_window():
    WindowEngine().window_starter()


if __name__ == "__main__":
    init_window()
    # url="www.instagram.com"
    # print(welcome_back())
    # open_webpage(url)
