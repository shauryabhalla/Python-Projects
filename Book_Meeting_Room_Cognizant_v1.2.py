import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

service = Service(executable_path=r"C:\Users\2121970\OneDrive - Cognizant\Desktop\py\Projects\msedgedriver.exe")
driver = webdriver.Edge(service=service)
current_date = datetime.now().day
# DATE = str(input("Input Date: "))
days_from_now = 20

def get_future_date(days):
    # Get the current date
    current_date = datetime.now().date()
    # Calculate the future date
    future_date = current_date + timedelta(days=days)
    future_date_str = str(future_date)
    return future_date_str[8:]

day_of_booking = get_future_date(days_from_now)

# Open One Cognizant
driver.get("https://onecognizant.cognizant.com/")
driver.fullscreen_window()


# Open Book Meeting Room Option
XPATH_BMR = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Book Meeting Room Opens a dialog']"))
)
XPATH_BMR.click()
time.sleep(10)

# Open City Dropdown Option
CSS_CITY_DROPDOWN = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label='Select City']"))
)
CSS_CITY_DROPDOWN.click()

# Select City
XPATH_CITY = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='IN - Kolkata']"))
)
XPATH_CITY.click()

# Select Facility Dropdown
CSS_FACILITY_DROPDOWN = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label='Select Location']"))
)
CSS_FACILITY_DROPDOWN.click()

# Select Facility
XPATH_FACILITY = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Unitech Infospace (G2 and C1)']"))
)
XPATH_FACILITY.click()

# Date Dropdown
XPATH_DATE_DROPDOWN = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='date']"))
)
XPATH_DATE_DROPDOWN.click()

# If date is greater than today then select the same month otherwise change to next month
if int(day_of_booking) >= current_date:
    date_element = driver.find_element(By.XPATH, f"//button[normalize-space()='{day_of_booking}']")
    date_element.click()

if int(day_of_booking) < current_date:
    nxt_mnth = driver.find_element(By.XPATH, "//button[@class='month-next']//*[name()='svg']")
    nxt_mnth.click()
    date_element = driver.find_element(By.XPATH, f"//button[normalize-space()='{day_of_booking}']")
    date_element.click()

# Redundant part
# Date Select
# DATE_LIST = []
# DATES = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//tbody"))
# )
# DATE_LIST.append(DATES.text)

# # Clean the dates list
# DATES_CLEAN = [date for sublist in DATE_LIST for date in sublist.split('\n')]


# Date OK
XPATH_DATE_OK = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Ok']"))
)
XPATH_DATE_OK.click()

# From Dropdown
XPATH_FROM = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='fromTimepicker']"))
)
XPATH_FROM.click()

# From Hour
XPATH_FROM_H = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='mdtimepicker']//div[@class='mdtp__hour_holder']//span[contains(text(),'10')]"))
)
XPATH_FROM_H.click()

# From Minute
XPATH_FROM_M = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='mdtp__minute_holder']//span[contains(text(),'00')]"))
)
XPATH_FROM_M.click()

# From AM/PM
# XPATH_FROM_TZ = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//div[@class='mdtimepicker']//span[@class='mdtp__am'][normalize-space()='AM']"))
# )
# XPATH_FROM_TZ.click()

# OK
XPATH_FROM_OK = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='mdtimepicker']//span[@class='mdtp__button ok'][normalize-space()='Ok']"))
)
XPATH_FROM_OK.click()

# To Dropdown
XPATH_TO = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='toTimepicker']"))
)
XPATH_TO.click()
time.sleep(1)
# To Hour
XPATH_TO_H = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='mdtimepicker']//span[contains(text(),'8')]"))
)
XPATH_TO_H.click()

# To Minutes
XPATH_TO_M = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='mdtp__digit rotate-90 marker']//span[contains(text(),'00')]"))
)
XPATH_TO_M.click()

# To AM/PM
XPATH_TO_TZ = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='mdtimepicker']//span[@class='mdtp__pm'][normalize-space()='PM']"))
)
XPATH_TO_TZ.click()


# OK
XPATH_TO_OK = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='mdtimepicker']//span[@class='mdtp__button ok'][normalize-space()='Ok']"))
)
XPATH_TO_OK.click()

# BOOK MEETING ROOM
XPATH_SELECT_ROOM = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='BOOK MEETING ROOM']"))
)
XPATH_SELECT_ROOM.click()

# Book Milan
XPATH_BOOK_MILAN = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//body[1]/div[2]/div[7]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form[2]/div[1]/div[2]/div[1]/div[7]/div[1]/div[2]/div[2]"))
)
XPATH_BOOK_MILAN.click()

# "//body[1]/div[2]/div[7]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form[2]/div[1]/div[2]/div[1]/div[7]/div[1]/div[2]/div[2]"
# selectors"//body/div/div[@aria-label='Launching Activity']/div/div/div/div/div/div/form/div/div/div/div/div[2]/div[2]"undefined
# //*[@id="bookMyMeetingForm"]/div/div[2]/div/div[7]/div/div[2]/div[2]
# selectors"//div[14]//div[1]//div[2]//div[2]"undefined
# selectors"//body"undefined
# selectors"//body"undefined
# selectors"//body"undefined
# selectors"//body"undefined
# selectors"(//body)[1]"undefined

time.sleep(10)
driver.quit()