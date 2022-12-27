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
url = 'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030900'
browser.get(url)

# Check whether the specified path exists or not
isExist = os.path.exists('Stock Information')

if not isExist:
    # Create a new directory because it does not exist
    os.mkdir('Stock Information')
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


def payment(xpath, tr, td):
    item = []

    while True:
        try:
            if td == '':
                x = browser.find_element(By.XPATH, xpath + '[' + str(tr) + ']').text
            else:
                x = browser.find_element(By.XPATH, xpath + '[' + str(tr) + ']/td[' + str(td) + ']').text

            tr += 2
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
    if not os.path.exists("Stock Information/" + code + ".json"):
        f = open("Stock Information/" + code + ".json", "a")
    else:
        # Create a new json because it does not exist
        print("Rewriting file")
        f = open("Stock Information/" + code + ".json", "w")

    print(code + '\n')
    f.write("Stock Code: " + code + "\n")

    # scrape the data on the new page and get back with the following command
    general = {'Instrument Code': browser.find_element(By.XPATH,
                                                       '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[1]/td[4]').text,

               'Stock Code': browser.find_element(By.XPATH,
                                                  '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[2]/td[4]').text,

               'Stock Serial': browser.find_element(By.XPATH,
                                                    '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[3]/td[4]').text,

               'This Year Series': browser.find_element(By.XPATH,
                                                        '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[4]/td[4]').text,

               'ISIN Code': browser.find_element(By.XPATH,
                                                 '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[5]/td[4]').text,

               'Stock Description': browser.find_element(By.XPATH,
                                                         '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[6]/td[4]').text,

               'Stock Category': browser.find_element(By.XPATH,
                                                      '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[7]/td[4]').text,

               'Principle': browser.find_element(By.XPATH,
                                                 '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[8]/td[4]').text,

               'Issue Date': browser.find_element(By.XPATH,
                                                  '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[9]/td[4]').text,

               'Maturity Date': browser.find_element(By.XPATH,
                                                     '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[10]/td[4]').text,

               'Primary Stock Code': browser.find_element(By.XPATH,
                                                          '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[11]/td[4]').text,

               'Optional Profit Date': browser.find_element(By.XPATH,
                                                            '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[12]/td[4]').text,

               'Issue Amount': browser.find_element(By.XPATH,
                                                    '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[13]/td[4]').text,

               'Lead Arranger': browser.find_element(By.XPATH,
                                                     '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[14]/td[4]').text,

               'Facility Agent': browser.find_element(By.XPATH,
                                                      '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[15]/td[4]').text,

               'Detachable': browser.find_element(By.XPATH,
                                                  '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[16]/td[4]').text,

               'Facility Code': browser.find_element(By.XPATH,
                                                     '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[1]/td[8]').text,

               'Short Name': browser.find_element(By.XPATH,
                                                  '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[2]/td[8]').text,

               'Payment Account': browser.find_element(By.XPATH,
                                                       '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[7]/td[8]').text,

               'Stock Status': browser.find_element(By.XPATH,
                                                    '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[8]/td[8]').text,

               'Optional Maturity Date': browser.find_element(By.XPATH,
                                                              '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[10]/td[8]').text,

               'Stock Indicator': browser.find_element(By.XPATH,
                                                       '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[11]/td[8]').text,

               'Final Redemption Price': browser.find_element(By.XPATH,
                                                              '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[12]/td[8]').text,

               'Outstanding Amount': browser.find_element(By.XPATH,
                                                          '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[13]/td[8]').text,

               'Currency': browser.find_element(By.XPATH,
                                                '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[14]/td[8]').text,

               'Issuer': browser.find_element(By.XPATH,
                                              '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[15]/td[8]').text,

               'Secondary Amount': browser.find_element(By.XPATH,
                                                        '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[18]/td/fieldset/table/tbody/tr[1]/td[3]').text,

               'Primary Amount': browser.find_element(By.XPATH,
                                                      '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[18]/td/fieldset/table/tbody/tr[2]/td[3]').text,

               'Type (Eg.CUSIP)': row(
                   '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[19]/td[2]/table/tbody/tr/td[1]/table/tbody/tr',
                   2,
                   1),

               'Alternate ID': row(
                   '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[19]/td[2]/table/tbody/tr/td[1]/table/tbody/tr',
                   2,
                   2),

               }

    print(json.dumps(general, indent=1))
    f.write(json.dumps(general, indent=1) + "\n")

    if general['Principle'] == 'ISLAMIC':
        profit = {'Profit Type': browser.find_element(By.XPATH,
                                                      '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[1]/td[4]').text,
                  'RENTAS Profit Payment Category': browser.find_element(By.XPATH,
                                                                         '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td[4]').text,
                  'Profit Accrual Start Date': browser.find_element(By.XPATH,
                                                                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[3]/td[4]').text,
                  'First Profit Payment Date': browser.find_element(By.XPATH,
                                                                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[4]/td[4]').text,
                  'Last Profit Payment Date': browser.find_element(By.XPATH,
                                                                   '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[5]/td[4]').text,
                  'Profit Rate': browser.find_element(By.XPATH,
                                                      '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[7]/td[4]').text,
                  'Ex-Day': browser.find_element(By.XPATH,
                                                 '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[4]/td[9]').text,
                  'Day Count Basis': browser.find_element(By.XPATH,
                                                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[5]/td[9]').text,

                  'Floating Rate Information': {

                      'Reference Source': browser.find_element(By.XPATH,
                                                               '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

                      'Margin (b.p.)': browser.find_element(By.XPATH,
                                                            '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,

                      'Ex-day for Fixing Date': browser.find_element(By.XPATH,
                                                                     '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,

                      'Cap Rate': browser.find_element(By.XPATH,
                                                       '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[4]/td[3]').text,

                      'Floor Rate': browser.find_element(By.XPATH,
                                                         '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[5]/td[3]').text,

                      'Reset Date': row(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[6]/td/table/tbody/tr',
                          2,
                          ''),

                  },

                  'Profit Date': row(
                      '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr',
                      2, ''),

                  'Profit Setting': {

                      'Profit End Date Rule': {

                          'Shift End Date': browser.find_element(By.XPATH,
                                                                 '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

                          'If Holiday On': row(
                              '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                              2, 1),

                          'Rules': row(
                              '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                              2, 2),

                      },

                      'Calculation of No of Days in Profit Period': {

                          'For Each Profit Period': row(
                              '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr',
                              2, 1),

                          'Option': row(
                              '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr',
                              2, 2),

                      },

                      'Profit Payment Date Rule': {

                          'Shift Payment Date': browser.find_element(By.XPATH,
                                                                     '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td[3]').text,

                          'If Holiday On': row(
                              '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                              2, 1),

                          'Rules': row(
                              '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                              2, 2),

                      }
                  },

                  'Frequency of Profit Payment': browser.find_element(By.XPATH,
                                                                      '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr/td[3]').text,

                  'Profit Payment Schedule': {
                      'Seq.': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 1),

                      'Start Date': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 2),

                      'End Date': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 3),

                      'Payment Date': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 4),

                      'Ex-Date': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 5),

                      'Profit Rate (%)': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 6),

                      'Tenor': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 7),

                      'Entitle for Profit': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 8),

                      'Payment Type': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 9),

                      'Skip': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 10),

                      'If Skip, Allow Profit on Profit (POP)': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 11),

                      'Profit on Profit Rate (%)': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 12),

                      'Fixing Date': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 13),

                      'Reference Rate': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 14),

                      'Adjustment Date': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 15),

                  }
                  }

        print(json.dumps(profit, indent=1))
        f.write(json.dumps(profit, indent=1) + "\n")

    else:
        coupon = {'Coupon Type': browser.find_element(By.XPATH,
                                                      '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[1]/td[4]').text,
                  'RENTAS Interest Payment Category': browser.find_element(By.XPATH,
                                                                           '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td[4]').text,
                  'Interest Accrual Start Date': browser.find_element(By.XPATH,
                                                                      '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[3]/td[4]').text,
                  'First Interest Date': browser.find_element(By.XPATH,
                                                              '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[4]/td[4]').text,
                  'Last Interest Date': browser.find_element(By.XPATH,
                                                             '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[5]/td[4]').text,
                  'Coupon Rate': browser.find_element(By.XPATH,
                                                      '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[7]/td[4]').text,
                  'Ex-Day': browser.find_element(By.XPATH,
                                                 '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[4]/td[9]').text,
                  'Day Count Basis': browser.find_element(By.XPATH,
                                                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[5]/td[9]').text,

                  'Floating Rate Information': {

                      'Reference Source': browser.find_element(By.XPATH,
                                                               '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

                      'Margin (b.p.)': browser.find_element(By.XPATH,
                                                            '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,

                      'Ex-day for Fixing Date': browser.find_element(By.XPATH,
                                                                     '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,

                      'Cap Rate': browser.find_element(By.XPATH,
                                                       '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[4]/td[3]').text,

                      'Floor Rate': browser.find_element(By.XPATH,
                                                         '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[5]/td[3]').text,

                      'Reset Date': row(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[6]/td/table/tbody/tr',
                          2,
                          ''),

                  },

                  'Interest Date': row(
                      '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr',
                      2, ''),

                  'Interest Setting': {

                      'Interest End Date Rule': {

                          'Shift End Date': browser.find_element(By.XPATH,
                                                                 '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

                          'If Holiday On': row(
                              '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                              2, 1),

                          'Rules': row(
                              '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                              2, 2),

                      },

                      'Calculation of No of Days in Interest Period': {

                          'For Each Interest Period': row(
                              '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr',
                              2, 1),

                          'Option': row(
                              '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr',
                              2, 2),

                      },

                      'Interest Payment Date Rule': {

                          'Shift Payment Date': browser.find_element(By.XPATH,
                                                                     '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td[3]').text,

                          'If Holiday On': row(
                              '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                              2, 1),

                          'Rules': row(
                              '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                              2, 2),

                      }
                  },

                  'Frequency of Interest Payment': browser.find_element(By.XPATH,
                                                                        '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr/td[3]').text,

                  'Interest Payment Schedule': {

                      'Seq.': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 1),

                      'Start Date': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 2),

                      'End Date': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 3),

                      'Payment Date': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 4),

                      'Ex-Date': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 5),

                      'Coupon Rate (%)': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 6),

                      'Tenor': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 7),

                      'Entitle for Coupon': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 8),

                      'Payment Type': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 9),

                      'Skip': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 10),

                      'If Skip, Allow Int. on Int. (IOI)': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 11),

                      'Int. on Int. Rate (%)': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 12),

                      'Fixing Date': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 13),

                      'Reference Rate': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 14),

                      'Adjustment Date': payment(
                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                          2, 15),

                  }
                  }
        print(json.dumps(coupon, indent=1))
        f.write(json.dumps(coupon, indent=1) + "\n")

    redemption = {
        'Redemption Date': row('//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[1]/tbody/tr/td/table/tbody/tr',
                               2, 1),

        'Redemption Amount (RM)': row(
            '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[1]/tbody/tr/td/table/tbody/tr/td[2]', 2, 2),

        'Call Details': {
            'Call Details': browser.find_element(By.XPATH,
                                   '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/legend').text,

            'Allow Partial Call': browser.find_element(By.XPATH,
                                                       '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[1]/tbody/tr[1]/td').text,

            'Redeem to the nearest denomination': browser.find_element(By.XPATH,
                                                                       '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[1]/tbody/tr[2]/td').text,

            'Acc.': browser.find_element(By.XPATH,
                                         '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[1]/tbody/tr[3]/td[2]').text,

            'Profit On Profit Rate': browser.find_element(By.XPATH,
                                                          '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[1]/tbody/tr[3]/td[5]').text,

            'Call Schedule': {

                'Start Date': row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 1),
                'End Date': row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 2),
                'Call Price': row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 3)
            },

            'Lockout Period': {

                'Start Date': row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[3]/fieldset/table/tbody/tr',
                    2, 1),
                'End Date': row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[3]/fieldset/table/tbody/tr/td[2]',
                    2, 2),
            }
        },

        'Put Details': {

            'Put Details': browser.find_element(By.XPATH,
                                   '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/legend').text,

            'Allow Partial Put': browser.find_element(By.XPATH,
                                                      '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[1]/tbody/tr[1]/td').text,

            'Redeem to the nearest denomination': browser.find_element(By.XPATH,
                                                                       '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[1]/tbody/tr[2]/td').text,

            'Put Schedule': {

                'Start Date': row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 1),
                'End Date': row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 2),
                'Put Price': row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 3)
            },

            'Lockout Period': {

                'Start Date': row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[3]/fieldset/table/tbody/tr',
                    2, 1),
                'End Date': row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[3]/fieldset/table/tbody/tr',
                    2, 2),
            }
        }

    }

    print(json.dumps(redemption, indent=1))
    f.write(json.dumps(redemption, indent=1) + "\n")

    rating = {
        'Government Guarantee': browser.find_element(By.XPATH,
                                                     '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[1]/td').text,

        'Indicator': browser.find_element(By.XPATH,
                                          '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td').text,

        'stock rating': {
            'Rating Agency': row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                1),

            'Effective Date': row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                2),

            'Current Rating Tenure': row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                3),

            'Initial Rating': row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                4),

            'Current Rating': row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                5),

            'Rating Action': row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                6),

            'Rating Outlook': row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                7),

            'Rating Watch': row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                8),
        }
    }
    print(json.dumps(rating, indent=1))
    f.write(json.dumps(rating, indent=1) + "\n")

    miscellaneous = {
        'Trading Details': {
            'Tradable': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

            'Trading Basis': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,
        },

        'Bullet/Revolving': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr/td').text,

        'Asset Backed': {
            'Originator': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

            'SPV': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,

            'Servicer': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,

            'Underlying Assets': row('//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr[4]/td/table/tbody/tr', 2, 1),
        },

        'Islamic Securities': {
            'Purchase Price of Assets': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr[1]/td[3]').text,

            'Selling Price of Assets': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr[2]/td[3]').text,

            'Value of Assets': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr[3]/td[3]').text,

            'Underlying Assets': row('//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr[4]/td/table/tbody/tr', 2, 1)
        },

        'Inflation Protected': {

            'Inflation Protected':  browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/legend').text,

            'Reference Source': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

            'Indices for Benchmark': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,

            'Remarks': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,
        },

        'Indicative Market Price': {

            'Mid Price': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[2]/fieldset/table/tbody/tr[1]/td[3]').text,

            'Mid Yield (%)': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[2]/fieldset/table/tbody/tr[2]/td[3]').text,

            'Mid Discount Rate (%)': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[2]/fieldset/table/tbody/tr[3]/td[3]').text,
        },

        'Convertible': {

            'Convertible': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[1]/fieldset/legend').text,

            'Conversion Period': {

                'Start Date': row('//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[1]/fieldset/table/tbody/tr[1]/td[3]/table/tbody/tr', 2, 1),

                'End Date': row('//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[1]/fieldset/table/tbody/tr[1]/td[3]/table/tbody/tr', 2, 2),
            },

            'Remarks': browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,
        },

        'Regulatory Status': {

            'code': row('//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[2]/fieldset/table/tbody/tr', 2, 1),

            'description': row('//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[2]/fieldset/table/tbody/tr', 2, 2),
        },

    }
    print(json.dumps(miscellaneous, indent=1))
    f.write(json.dumps(miscellaneous, indent=1) + "\n")

    # back to main page
    browser.execute_script("window.history.go(-1)")

    # wait driver to find the link table
    WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#BrowseTable td:nth-child(2) a")))
    time.sleep(1)

browser.quit()
