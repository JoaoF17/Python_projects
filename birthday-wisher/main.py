from dotenv import load_dotenv
import os
import smtplib
import pandas as pd
import datetime as dt
from random import randint

load_dotenv()

MY_EMAIL = "test@gmail.com"
MY_PASS = os.getenv("EMAIL_PASS")

# 1. Get the birthdays.csv
data = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.month, now.day)

birthday_dic = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today in birthday_dic:
  birthday_person = birthday_dic[today]
  file_path = f"letter_templates/letter_{randint(1,3)}.txt"
  with open(file_path) as letter_file:
    contents = letter_file.read()
    contents = contents.replace("[NAME]", birthday_person["name"])
    
# 4. Send the letter generated in step 3 to that person's email address.
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASS)
    connection.sendmail(
      from_addr=MY_EMAIL,
      to_addrs=birthday_person["email"],
      msg=f"Subject:Happy Birthday {birthday_person['name']}!\n\n{contents}")