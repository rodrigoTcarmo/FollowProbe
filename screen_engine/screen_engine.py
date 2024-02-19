import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class WebpageEngine:
    def __init__(self, log_text, tk, master):
        self.follow_btn = None
        self.driver = webdriver.Chrome()
        self.log_text = log_text
        self.tk = tk
        self.master = master
        self.message_printed = False

    def start_webpage_engine(self, target_account, followers_qty):
        url = f"http://www.instagram.com/{target_account}/followers/"
        self.log_text.insert(self.tk.END, "Abrindo perfil escolhido...\n")
        self.log_text.insert(self.tk.END, url + "\n")

        self.driver.get(url=url)
        time.sleep(5)

        success_followed = 0
        failure_followed = 0
        for _ in range(followers_qty):
            try:
                # self.follow_btn = self.driver.find_element(By.XPATH, "//*[text()='Seguir']")
                self.follow_btn = self.driver.find_elements(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
                for element in self.follow_btn:
                    btn = element.find_element(By.XPATH, ".//*[text()='Seguir']")
                    print(btn.parent)
                    action = ActionChains(self.driver)
                    action.move_to_element(btn).click().perform()

                success_followed += 1
                self.log_text.insert(self.tk.END, f"Conta seguida com sucesso!\n")
                self.master.update()
                time.sleep(2)
            except Exception as follow_error:
                if "Unable to locate element" in str(follow_error):
                    print("Fim da lista de seguidores.")
                    self.log_text.insert(self.tk.END, f"FIM DA LISTA DE SEGUIDORES!\n")
                    self.log_text.insert(self.tk.END, f"Total de solicitadas para seguir: {followers_qty}\n")
                    self.log_text.insert(self.tk.END, f"Total de contas seguidas com erro: {failure_followed}\n")
                    self.log_text.insert(self.tk.END, f"Total de contas seguidas com sucesso: {success_followed}\n")
                    self.message_printed = True
                    break
                else:
                    failure_followed += 1
                    print(f"erro ao seguir: {follow_error}")
                    self.log_text.insert(self.tk.END, f"Erro ao tentar seguir conta!")
                    self.log_text.insert(self.tk.END, f"Error: {follow_error}\n\n")
                    self.master.update()
                    continue

        if not self.message_printed:
            self.log_text.insert(self.tk.END, f"Total de solicitadas para seguir: {followers_qty}\n")
            self.log_text.insert(self.tk.END, f"Total de contas seguidas com erro: {failure_followed}\n")
            self.log_text.insert(self.tk.END, f"Total de contas seguidas com sucesso: {success_followed}\n")
    def open_login_page(self, login_url):
        print("Opening instagram login page")
        self.driver.get(login_url)

    def is_logged_in(self):
        try:
            # Look for an element that indicates the user is logged in
            self.driver.find_element(By.XPATH, "//span[text()='Perfil']")
            return True
        except:
            return False
