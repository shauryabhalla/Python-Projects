import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
service = Service(executable_path=r"C:\Users\2121970\OneDrive - Cognizant\Desktop\py\Projects\msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Open the target webpage
driver.get("https://onecognizant.cognizant.com/")
TASK_ID = '000000000000027'

# Click on 'View Timesheet' link
XPATH_VIEW_TIMESHEET = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='View Timesheet Opens in a new tab']"))
)
XPATH_VIEW_TIMESHEET.click()

# Wait for the new tab to open
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

# Get the handle of the current window
original_window = driver.current_window_handle

# Get all window handles
all_windows = driver.window_handles

# Switch to the new window
for window in all_windows:
    if window != original_window:
        driver.switch_to.window(window)
        break

# Click on the latest timesheet
XPATH_LATEST_TIMESHEET = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@id='CTS_TS_LAND_PER_DESCR30$0']"))
)
XPATH_LATEST_TIMESHEET.click()

# We need to select the iframe before we can interact with elements inside it
iframe = WebDriverWait(driver, 20).until(
    EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='ptifrmtgtframe']"))
)

# Enter the task ID
XPATH_TASK = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='CTS_MSTASK_WRK_CTS_MSTASK_CODE$0']"))
)
XPATH_TASK.click()
XPATH_TASK.send_keys(TASK_ID)

# Function to set time values using JavaScript
def set_time_value(xpath, value):
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    # There might be some JavaScript on the page that is resetting the input field after we enter the value
    # That's why we dont use the simple XPATH_TIME3.click() & XPATH_TIME3.send_keys("9")
    driver.execute_script("arguments[0].value = arguments[1];", element, value)
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", element)

# Set time values for each day
set_time_value("//input[@id='TIME3$0']", "9")
set_time_value("//input[@id='TIME4$0']", "9")
set_time_value("//input[@id='TIME5$0']", "9")
set_time_value("//input[@id='TIME6$0']", "9")
set_time_value("//input[@id='TIME7$0']", "9")

# Optionally, click on update and submit buttons
# XPATH_UPDATE = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@id='PB_UPDATE_2']"))
# )
# XPATH_UPDATE.click()

# XPATH_SUBMIT = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@id='EX_TIME_HDR_WRK_PB_SUBMIT']"))
# )
# XPATH_SUBMIT.click()

# Wait for a few seconds before closing the browser
time.sleep(5)
driver.quit()
