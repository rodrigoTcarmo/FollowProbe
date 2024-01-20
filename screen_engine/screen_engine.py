import webbrowser


class WebpageEngine:
    def __init__(self, target_account, followers_qty):
        self.target_account = target_account
        self.followers_qty = followers_qty

    def start_webpage_engine(self):
        print("Starting webpage engine...")
        self.open_webpage(url="www.instagram.com")

    def open_webpage(self, url):
        print("Abrindo navegador...")
        webbrowser.open(url)
