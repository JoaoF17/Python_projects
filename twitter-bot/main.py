from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
from speed_test_bot import SpeedTestBot
from twitter_bot import TwitterBot

load_dotenv()

PROMISE_DOWN = 150
PROMISE_UP = 50


# ------------ scrap data from speedtest ------------#
speed_bot = SpeedTestBot()

speed_bot.click_go_button()
if speed_bot.get_download_speed() < PROMISE_DOWN or speed_bot.get_upload_speed() < PROMISE_UP:
  # ------------ twitter bot ------------#
  twitter_bot = TwitterBot()

  twitter_bot.sign_in()