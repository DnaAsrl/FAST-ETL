import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time

s = Service("C:\Program Files (x86)\chromedriver.exe")
browser = webdriver.Chrome(service=s)
url = 'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030800'
browser.get(url)

# Check whether the specified path exists or not
isExist = os.path.exists('Facility Information')

if not isExist:
    # Create a new directory because it does not exist
    os.mkdir('Facility Information')
    print("The new directory is created!")

actions = ActionChains(browser)

# wait for the first link in the table
WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#BrowseTable td:nth-child(2) a")))

# extra wait to make all the links loaded
time.sleep(1)

# get the total links amount
links = browser.find_elements(By.CSS_SELECTOR, "#BrowseTable td:nth-child(2) a")

for index, val in enumerate(links):

    # get the links again after getting back to the initial page in the loop
    links = browser.find_elements(By.CSS_SELECTOR, "#BrowseTable td:nth-child(2) a")

    # scroll to the n-th link, it may be out of the initially visible area
    actions.move_to_element(links[index]).perform()
    code = links[index].find_element(By.CSS_SELECTOR, "u").text
    links[index].click()

    # Check whether the txt exists or not
    if not os.path.exists("Facility Information/" + code + ".txt"):
        f = open("Facility Information/" + code + ".txt", "a")
    else:
        # Create a new txt because it does not exist
        print("Rewriting file")
        f = open("Facility Information/" + code + ".txt", "w")

    print(code)
    f.write("Facility Code: " + code + "\n")

    # scrape the data on the new page and get back with the following command
    fieldsets = browser.find_elements(By.TAG_NAME, "fieldset")
    # !! fieldset dalam fieldset huhuhuhuh
    for fieldset in fieldsets:
        f.write(fieldset.text)

    f.close()
    # back to main page
    browser.execute_script("window.history.go(-1)")

    # wait driver to find the link table
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#BrowseTable td:nth-child(2) a")))
    time.sleep(1)

browser.quit()
