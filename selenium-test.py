from selenium import webdriver
from selenium.webdriver.common.by import By

#option to keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#initialize chromium driver
driver = webdriver.Chrome(options=chrome_options)

#open webpage
driver.get("https://www.python.org/")

#get the dates
dates =[]

events_elements = driver.find_elements(By.CSS_SELECTOR, "div.event-widget div.shrubbery ul.menu li")

for date in events_elements:
  time_element = date.find_element(By.TAG_NAME, "time")
  time = time_element.get_attribute("datetime").split("T")[0]
  dates.append(time)

print(dates)

#get the events
events = []

for event in events_elements:
  event_element = event.find_element(By.TAG_NAME, "a").text
  events.append(event_element)

#Create a dictionary with dates and events
python_events = {}
for x in range(0, len(events)-1):
  python_events[x] = {dates[x]:events[x]}

print(python_events)
driver.quit()