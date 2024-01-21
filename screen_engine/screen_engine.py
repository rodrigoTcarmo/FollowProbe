import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebpageEngine:
    def __init__(self, log_text, tk, master):
        self.follow_btn = None
        self.driver = webdriver.Chrome()
        self.log_text = log_text
        self.tk = tk
        self.master = master

    def start_webpage_engine(self, target_account, followers_qty):
        url = f"http://www.instagram.com/{target_account}/followers/"
        self.log_text.insert(self.tk.END, "Abrindo perfil escolhido...\n")
        self.log_text.insert(self.tk.END, url + "\n")

        self.driver.get(url=url)
        time.sleep(5)

        # Use WebDriverWait to wait until the button is clickable
        # button_xpath = "//*[text()='Seguir']"  # Update this with the actual XPath of your button
        # button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        success_followed = 0
        failure_followed = 0
        scroll_count = 0
        for _ in range(followers_qty):
            try:
                self.follow_btn = self.driver.find_element(By.XPATH, "//*[text()='Seguir']")
                self.driver.execute_script("arguments[0].click();", self.follow_btn)
                success_followed += 1
                self.log_text.insert(self.tk.END, f"Conta seguida com sucesso!\n")
                self.master.update()
                if scroll_count > 4:
                    fbody = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div["
                                                     "2]/div/div/div[2]")

                    self.driver.execute_script(
                        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                        fbody)
                    scroll_count = 0
                    time.sleep(2)
                else:
                    scroll_count += 1
                    time.sleep(2)

            except Exception as follow_error:
                failure_followed += 1
                print(f"erro ao seguir: {follow_error}")
                self.log_text.insert(self.tk.END, f"Erro ao tentar seguir conta!")
                self.log_text.insert(self.tk.END, f"Error: {follow_error}\n\n")
                self.master.update()
                continue

        self.log_text.insert(self.tk.END, f"Total de solicitadas para seguir: {followers_qty}\n")
        self.log_text.insert(self.tk.END, f"Total de contas seguidas com erro: {failure_followed}\n")
        self.log_text.insert(self.tk.END, f"Total de contas seguidas com sucesso: {success_followed}\n")
        # for btn in buttons:
        #     pass

        # Click on the button
        # button.click()

        # driver.find_element()
        # follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
        # follow_Button.click()

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
