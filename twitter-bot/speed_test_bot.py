from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SpeedTestBot:
    def __init__(self):
        # keep browser opened
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        # initialize chromium driver
        self.driver = webdriver.Chrome(options=chrome_options)

        # open website
        self.driver.get("https://www.speedtest.net/")

    def click_go_button(self):
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(5)
        self.driver.find_element(
            By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'
        ).click()
        time.sleep(50)

    def get_download_speed(self):
        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        print(download_speed)
        return float(download_speed)

    def get_upload_speed(self):
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(upload_speed)
        return float(upload_speed)
