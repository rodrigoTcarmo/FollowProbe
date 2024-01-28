import time
import tkinter as tk
from tkinter import scrolledtext
from screen_engine.screen_engine import WebpageEngine


class InterfaceEngine:
    def __init__(self, master):
        self.master = master
        master.title("Follow Probe Interface")

        # Labels
        self.label_target_accounts = tk.Label(master, text="Conta alvo:")
        self.label_accounts_qtys = tk.Label(master, text="Quantidade de contas para seguir:")

        # Entry widgets
        self.entry_target_accounts = tk.Entry(master)
        self.entry_accounts_qty = tk.Entry(master, validate="key",
                                                validatecommand=(master.register(self.validate_int), "%P"))

        # Button
        self.submit_button = tk.Button(master, text="Submit", command=self.window_starter)

        # Text widget for logging
        self.log_text = scrolledtext.ScrolledText(master, height=10, width=40, wrap=tk.WORD)

        # Layout
        self.label_target_accounts.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_target_accounts.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.label_accounts_qtys.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_accounts_qty.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=20)
        self.log_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.webpage_engine = WebpageEngine(log_text=self.log_text, tk=tk, master=self.master)
        self.log_text.insert(tk.END, "Iniciando follow probe bot...\n")
        self.log_text.insert(tk.END, "Aguardando o login ser efetuado...\n\n")
        self.webpage_engine.open_login_page(login_url="https://www.instagram.com")
        self.login_counter()
        self.log_text.insert(tk.END, "Insira nos campos acima a conta alvo e o número de seguidores desejado...\n")


    def login_counter(self):
        secs = 0
        while secs <= 120:
            self.master.update()
            if self.webpage_engine.is_logged_in():
                self.log_text.insert(tk.END, "Login realizado com sucesso!\n")
                break
            secs += 1
            time.sleep(1)

    def window_starter(self):
        target_account = self.entry_target_accounts.get()
        qty_accounts_to_follow = int(self.entry_accounts_qty.get())

        # Log the information
        log_message = f"CONTA ALVO: {target_account}\nNUMERO DE SEGUIDORES DESEJADO: {qty_accounts_to_follow}\nINICIANDO AUTOMAÇÃO...\n\n"
        self.log_text.insert(tk.END, log_message)

        # TODO: Implement the logic to start the process using the provided values
        self.webpage_engine.start_webpage_engine(target_account=target_account, followers_qty=qty_accounts_to_follow)

    def validate_int(self, new_value):
        try:
            if new_value == "":
                return True
            int(new_value)
            return True
        except ValueError:
            return False

root = tk.Tk()
# Create an instance of the FollowAccountsInterface class
follow_accounts_interface = InterfaceEngine(root)

# Start the Tkinter event loop
root.mainloop()