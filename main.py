from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#add email address and password inside config.txt, seperated by new line
config = [line.strip() for line in open("config.txt")]

driver = webdriver.Firefox()
driver.get("http://www.bing.com")
time.sleep(1)

signIn = WebDriverWait(driver,10000).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='id_l']")))
signIn.click()

userId = WebDriverWait(driver,10000).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='i0116']")))
userId.send_keys(config[0])
userId.send_keys(Keys.RETURN)

password = WebDriverWait(driver,10000).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='i0118']")))
password.send_keys(config[1])
password.send_keys(Keys.RETURN)

search = WebDriverWait(driver,10000).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='sb_form_q']")))
search.send_keys("Java")
search.send_keys(Keys.RETURN)

time.sleep(1)

search = WebDriverWait(driver,10000).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='sb_form_q']")))
search.clear()
search.send_keys("Python")
search.send_keys(Keys.RETURN)


time.sleep(5)

driver.close()

