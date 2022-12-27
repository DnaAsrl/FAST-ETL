from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import os

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


def row(xpath, tr, td):
    item = []

    while True:
        try:
            if td == '':
                x = browser.find_element(By.XPATH, xpath + '[' + str(tr) + ']').text
            else:
                x = browser.find_element(By.XPATH, xpath + '[' + str(tr) + ']/td[' + str(td) + ']').text

            tr += 1
            item.append(x)

        except NoSuchElementException:
            break

    return item


for index, val in enumerate(links):
    # get the links again after getting back to the initial page in the loop
    links = browser.find_elements(By.CSS_SELECTOR, "#BrowseTable td:nth-child(2) a")

    # scroll to the n-th link, it may be out of the initially visible area
    actions.move_to_element(links[index]).perform()
    code = links[index].find_element(By.CSS_SELECTOR, "u").text
    links[index].click()

    # Check whether the json exists or not
    if not os.path.exists("Facility Information/" + code + ".json"):
        f = open("Facility Information/" + code + ".json", "a")
    else:
        # Create a new json because it does not exist
        print("Rewriting file")
        f = open("Facility Information/" + code + ".json", "w")

    print(code + '\n')
    f.write("Facility Code: " + code + "\n")

    # scrape the data on the new page and get back with the following command
    details = {'general': {'description': browser.find_element(By.XPATH,
                                                               "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td[4]").text,

                           'principle': browser.find_element(By.XPATH,
                                                             "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td[8]").text,

                           'maturity date': browser.find_element(By.XPATH,
                                                                 "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td[4]").text,

                           'mode of offer': browser.find_element(By.XPATH,
                                                                 "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td[8]").text,

                           'acronym': browser.find_element(By.XPATH,
                                                           "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[3]/td[4]").text,

                           'currency': browser.find_element(By.XPATH,
                                                            "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[3]/td[8]").text,

                           'issuer': browser.find_element(By.XPATH,
                                                          "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[4]/td[4]").text,

                           'Spread Against Reference/Source': browser.find_element(By.XPATH,
                                                                                   '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td[3]').text,

                           'Form': browser.find_element(By.XPATH,
                                                        '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td[3]').text,

                           'Lead Arranger (LA) /Facility Agent (FA)': {
                               'FA': browser.find_element(By.XPATH,
                                                          '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[1]/td[4]').text,
                               'LA': browser.find_element(By.XPATH,
                                                          '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[2]/td[4]').text
                           },

                           'Facility Amount': {
                               'Facility Limit': browser.find_element(By.XPATH,
                                                                      '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[1]/td[4]').text,
                               'Availability Period': browser.find_element(By.XPATH,
                                                                           '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[2]/td[4]').text,
                               'Available Limit': browser.find_element(By.XPATH,
                                                                       '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[4]/td[4]').text,
                               'Outstanding': browser.find_element(By.XPATH,
                                                                   '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[5]/td[4]').text,
                           },

                           'Facility Approval': {
                               'Facility Approval Date (BNM)': browser.find_element(By.XPATH,
                                                                                    '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[1]/td[4]').text,
                               'Facility Approval Date (SC)': browser.find_element(By.XPATH,
                                                                                   '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[2]/td[4]').text,
                               'DPA Agreement Signed': browser.find_element(By.XPATH,
                                                                            '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[3]/td[4]').text,
                               'Approval Expiry': browser.find_element(By.XPATH,
                                                                       '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[4]/td[4]').text
                           },

                           'Other': {
                               'Authorised Depository': browser.find_element(By.XPATH,
                                                                             '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,
                               'Paying Agent': browser.find_element(By.XPATH,
                                                                    '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,
                               'Trustee/Security Agent': browser.find_element(By.XPATH,
                                                                              '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,
                           },
                           'co-arranger': row(
                               '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[3]/td/table/tbody/tr', 2,
                               ''),

                           'Islamic Concept': row(
                               '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/table[1]/tbody/tr', 2,
                               ''),

                           'Selling Restriction': row(
                               '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/table[2]/tbody/tr', 2,
                               '')

                           },

               'instruments': {'Instrument Code': browser.find_element(By.XPATH,
                                                                       '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[1]/td[3]').text,

                               'Instrument Type': browser.find_element(By.XPATH,
                                                                       '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td[3]').text,

                               'Instrument Description': browser.find_element(By.XPATH,
                                                                              '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[1]/td[6]').text,

                               'Instrument Transaction Type': browser.find_element(By.XPATH,
                                                                                   '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td[6]').text,

                               'Principle': browser.find_element(By.XPATH,
                                                                 '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[3]/td[3]').text,

                               'Bullet / Revolving': browser.find_element(By.XPATH,
                                                                          '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td').text,

                               'Instrument Amount': {
                                   'Instrument Limit': browser.find_element(By.XPATH,
                                                                            '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td[4]').text,
                                   'Maturity Date': browser.find_element(By.XPATH,
                                                                         '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td[4]').text,
                                   'Available Limit': browser.find_element(By.XPATH,
                                                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td[4]').text,
                                   'Outstanding': browser.find_element(By.XPATH,
                                                                       '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td[4]').text
                               },

                               'Instrument Participants': {
                                   'Underwritten': {
                                       'Underwritten': browser.find_element(By.XPATH,
                                                                            '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/legend').text,
                                       'Auto Deduction': browser.find_element(By.XPATH,
                                                                              '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td').text,
                                       'Total Original Commitment(RM)': browser.find_element(By.XPATH,
                                                                                             '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,
                                       'Total Present Available Commitment (RM)': browser.find_element(By.XPATH,
                                                                                                       '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,
                                       'organisation': row(
                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[4]/td/table/tbody/tr', 2,
                                           1),
                                       'Original Commitment': row(
                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[4]/td/table/tbody/tr', 2,
                                           1),
                                       'Present Available Commitment (RM)': row(
                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[4]/td/table/tbody/tr', 2,
                                           1),

                                   },

                                   'Guaranteed': {

                                       'Guaranteed': browser.find_element(By.XPATH,
                                                                          '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/legend').text,
                                       'Total Guaranteed (RM)': browser.find_element(By.XPATH,
                                                                                     '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr[1]/td[3]').text,
                                       'Remarks': browser.find_element(By.XPATH,
                                                                       '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr[3]/td[3]').text,
                                       'Organisation': row(
                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr[2]/td/table/tbody/tr', 2,
                                           1),
                                       'Guaranteed Amount (RM)': row(
                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr[2]/td/table/tbody/tr', 2,
                                           2)
                                   },

                                   'Direct Bidder': {
                                       'Organisation': row(
                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr/td/table/tbody/tr', 2,
                                           '')
                                   },

                                   'Primary Subscribers': {
                                       'Organisation': row(
                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr/td/table/tbody/tr', 2,
                                           '')
                                   },

                                   'Suspended Direct Bidder': {
                                       'Organisation': row(
                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/table/tbody/tr/td/table/tbody/tr', 2,
                                           '')
                                   },

                                   'Restricted Organisation': {
                                       'Organisation': row(
                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[3]/td[2]/fieldset/table/tbody/tr/td/table/tbody/tr', 2,
                                           '')
                                   },

                                   'Market Maker': {
                                       'Organisation': row(
                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr', 2,
                                           '')
                                   },

                                   'ABS Details': {
                                       'Originator': browser.find_element(By.XPATH,
                                                                          '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[1]/td[4]').text,
                                       'Servicer': browser.find_element(By.XPATH,
                                                                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[2]/td[4]').text,
                                       'Special Purpose Vehicle (SPV)': browser.find_element(By.XPATH,
                                                                                             '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[3]/td[4]').text,
                                       'Underlying Assets': row(
                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[4]/td/table/tbody/tr', 2, ''),
                                   },
                               }
                               },
               'Rating': {
                   'Government Guarantee': browser.find_element(By.XPATH,
                                                                '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[1]/td').text,
                   'Indicator': browser.find_element(By.XPATH,
                                                     '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td').text,
                   'facility rating': {
                       'Instrument': row(
                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2, 1),
                       'Rating Agency': row(
                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2, 2),
                       'Effective Date': row(
                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2, 3),
                       'Current Rating Tenure': row(
                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2, 4),
                       'Initial Rating': row(
                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2, 5),
                       'Current Rating': row(
                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2, 6),
                       'Rating Action': row(
                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2, 7),
                       'Rating Outlook': row(
                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2, 8),
                       'Rating Watch': row(
                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2, 9),
                   },
               },

               'Facility Sectors': {
                   'FISS': row('/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[5]/td/fieldset/table[3]/tbody/tr', 1, 1),
                   'Sector': row('//*[@id="tblSector"]/tbody/tr[1]/td[2]/table/tbody/tr', 1, 2),
                   'Amount (RM)': row('//*[@id="tblSector"]/tbody/tr', 1, 3)

               },

               'Facility Utilisation': {
                   'FISS': row('//*[@id="tblUtilise"]/tbody/tr', 1, 1),
                   'Utilisation': row('//*[@id="tblUtilise"]/tbody/tr', 1, 2),
                   'Amount (RM)': row('//*[@id="tblUtilise"]/tbody/tr', 1, 3)
               }
               }

    json_object = json.dumps(details, indent=1)
    print(code + '\n' + json_object)
    f.write(json_object)

    # back to main page
    browser.execute_script("window.history.go(-1)")

    # wait driver to find the link table
    WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#BrowseTable td:nth-child(2) a")))
    time.sleep(1)

browser.quit()
