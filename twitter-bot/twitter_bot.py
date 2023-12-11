from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()

twitter_login = os.getenv("EMAIL")
twitter_pass = os.getenv("TWITTER_PASS")

class TwitterBot:
  def __init__(self):
    # keep browser opened
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # initialize chromium driver
    self.driver = webdriver.Chrome(options=chrome_options)

    # open website
    self.driver.get("https://twitter.com/")
    
  def sign_in(self):
    self.driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"][class*="r-30o5oe"]').send_keys(twitter_login)
    time.sleep(1)
    self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(twitter_pass)
    time.sleep(1)
    self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()
    time.sleep(1)
    self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys('Test')
    time.sleep(2)
    self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span').click()