import tkinter as tk


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

        # Layout
        self.label_target_accounts.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_target_accounts.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.label_accounts_qtys.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_accounts_qty.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=20)
        
        self.window = tk.Tk()
        self.entry = tk.Entry()

    def window_starter(self):
        target_account = self.entry_target_accounts.get()
        qty_accounts_to_follow = int(self.entry_accounts_qty.get())

        # TODO: Implement the logic to start the process using the provided values
        print(f"Target Account: {target_account}")
        print(f"Number of Accounts to Follow: {qty_accounts_to_follow}")


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