# COPYRIGHTED SANDHU INDUSTRIES

# Import the necessary modules (Selnium, it a bot making/webscraping lib, we imported a function)

from selenium import webdriver # Allows us to use chrome driver
from selenium.webdriver.chrome.service import Service # Getting a file path and putting it in the function
from selenium.webdriver.common.by import By # Selecting HTML elements
import pandas as pd # Data sciecne librares

TIME_OUT = 10 # According to robots.txt

# Initialize the webdriver
sel_service = Service(r"C:\Users\Dilshaan Sandhu\Downloads\chromedriver_win32 (1)\chromedriver.exe") #
option = webdriver.ChromeOptions()
option.add_argument('--incognito')
option.add_argument('--disable-geolocation')
driver = webdriver.Chrome(service=sel_service, options=option)

# Open the webpage
driver.get("http://metroathletics.ca/master_sched_league.php")

# Find the element using the class name
dates_table = driver.find_element(By.CLASS_NAME, "hc-table")

dates_tables_headers = [i.text for i in dates_table.find_element(By.TAG_NAME, "thead").find_elements(By.TAG_NAME, "td")]
print(dates_tables_headers)

dates_tables_dict = {k: [] for k in dates_tables_headers}


for i in dates_table.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
    for j, k in zip(i.find_elements(By.TAG_NAME, "td"), dates_tables_headers):
        dates_tables_dict[k].append(j.text)

dates_tables_df = pd.DataFrame(dates_tables_dict)
dates_tables_df.to_csv("dates_tables.csv", index=False)

