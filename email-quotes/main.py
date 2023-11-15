from dotenv import load_dotenv
import os
import smtplib
import datetime as dt
from random import choice

load_dotenv() 

my_email = "joao@gmail.com"
my_pass = os.getenv("EMAIL_PASS") #change pass in .env

#open quotes text file
with open("quotes.txt", "r") as file:
  quote_list = [line for line in file]

message = choice(quote_list)
print(message)

#setting the time condition
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
  #setting up the bot to send the email
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(
      from_addr=my_email, 
      to_addrs="joao_fernandess17@hotmail.com", 
      msg=f"Subject: Motivational Quote\n\n{message}"
    )




