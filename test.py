import os
import re
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
url = 'https://fast.bnm.gov.my/fastweb/public/PublicInfoServlet.do?chkBox=202200000035&mode=DISPLAY&info=FACILITY&screenId=PB030800'
browser.get(url)

# Check whether the specified path exists or not
isExist = os.path.exists('Test')

if not isExist:
    # Create a new directory because it does not exist
    os.mkdir('Test')
    print("The new directory is created!")

# Check whether the txt exists or not

table = browser.find_element(By.CSS_SELECTOR, "#SpanPrint > table > tbody > tr:nth-child(2) > td > fieldset")
# table = browser.find_elements(By.CSS_SELECTOR, "#SpanPrint > table > tbody > tr:nth-child(7) > td > fieldset")

# for data in table:
legend = table.find_element(By.TAG_NAME, "legend").text

if not os.path.exists("Test/"+str(legend)+".txt"):
    f = open("Test/"+str(legend)+".txt", "w")
else:
    # Create a new txt because it does not exist
    print("Rewriting file")
    f = open("Test/"+str(legend)+".txt", "w")

# ideas:
# - buang &nsbp
# - baca pdf

# attr = table.find_elements(By.CSS_SELECTOR, "td:nth-child(6) , tr+ tr > td > fieldset > table > tbody > tr > "
#                                             "td:nth-child(2)")

# f.write(table.text.replace("^\d+(\.\d+)*$", "\n"))

# for td in table.:


# box = table.find_elements(By.CSS_SELECTOR, "#SpanPrint td td fieldset")
# for i in box:
#     table.text.replace(i.text, ' ')

# for td in table.find_elements(By.CSS_SELECTOR, "tr td"):
#     f.write(td.text.strip() + "\n")

f.close()

browser.quit()
