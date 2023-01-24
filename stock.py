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


def run(self):
    code = self.code
    browser = self.browser
    timestr = time.strftime("%Y-%m-%d%H%M%S")
    path = 'Stock Information/' + code
    isExist = os.path.exists(path)
    if not isExist:
        os.mkdir(path)
    dir_path = path + '/' + timestr + ".json"
    f = open(dir_path, "a")
    f.write("Stock Information: " + code + "\n")

    # print(code + '\n')
    f.write("Stock Code: " + code + "\n")

    # scrape the data on the new page and get back with the following command
    details = {
        'general': {'Instrument Code': browser.find_element(By.CSS_SELECTOR,
                                                            'tr:nth-child(2) tr tr:nth-child(1) td:nth-child(4)').text,

                    'Stock Code': browser.find_element(By.CSS_SELECTOR,
                                                       'tr:nth-child(2) tr tr:nth-child(2) td:nth-child(4)').text,

                    'Stock Serial': browser.find_element(By.CSS_SELECTOR,
                                                         'tr:nth-child(2) tr tr:nth-child(3) td:nth-child(4)').text,

                    'This Year Series': browser.find_element(By.CSS_SELECTOR,
                                                             'tr:nth-child(2) tr tr:nth-child(4) td:nth-child(4)').text,

                    'ISIN Code': browser.find_element(By.CSS_SELECTOR,
                                                      'tr:nth-child(2) tr tr:nth-child(5) td:nth-child(4)').text,

                    'Stock Description': browser.find_element(By.CSS_SELECTOR,
                                                              'tr:nth-child(2) tr tr:nth-child(6) td:nth-child(4)').text,

                    'Stock Category': browser.find_element(By.CSS_SELECTOR,
                                                           'tr:nth-child(2) tr tr:nth-child(7) td:nth-child(4)').text,

                    'Principle': browser.find_element(By.CSS_SELECTOR,
                                                      'tr:nth-child(2) tr tr:nth-child(8) td:nth-child(4)').text,

                    'Issue Date': browser.find_element(By.CSS_SELECTOR,
                                                       'tr:nth-child(2) tr tr:nth-child(9) td:nth-child(4)').text,

                    'Maturity Date': browser.find_element(By.CSS_SELECTOR,
                                                          'tr:nth-child(2) tr tr:nth-child(10) td:nth-child(4)').text,

                    'Primary Stock Code': browser.find_element(By.CSS_SELECTOR,
                                                               'tr:nth-child(2) tr tr:nth-child(11) td:nth-child(4)').text,

                    'Optional Profit Date': browser.find_element(By.CSS_SELECTOR,
                                                                 'tr:nth-child(2) tr tr:nth-child(12) td:nth-child(4)').text,

                    'Issue Amount': browser.find_element(By.CSS_SELECTOR,
                                                         'tr:nth-child(2) tr tr:nth-child(13) td:nth-child(4)').text,

                    'Lead Arranger': browser.find_element(By.CSS_SELECTOR,
                                                          'tr:nth-child(2) tr tr:nth-child(14) td:nth-child(4)').text,

                    'Facility Agent': browser.find_element(By.CSS_SELECTOR,
                                                           'tr:nth-child(2) tr tr:nth-child(15) td:nth-child(4)').text,

                    'Detachable': browser.find_element(By.CSS_SELECTOR,
                                                       'tr:nth-child(2) tr tr:nth-child(16) td:nth-child(4)').text,

                    'Facility Code': browser.find_element(By.CSS_SELECTOR,
                                                          'tr:nth-child(2) tr tr:nth-child(1) td:nth-child(8)').text,

                    'Short Name': browser.find_element(By.CSS_SELECTOR,
                                                       'tr:nth-child(2) tr tr:nth-child(2) td:nth-child(8)').text,

                    'Payment Account': browser.find_element(By.CSS_SELECTOR,
                                                            'tr:nth-child(2) tr tr:nth-child(7) td:nth-child(8)').text,

                    'Stock Status': browser.find_element(By.CSS_SELECTOR,
                                                         'tr:nth-child(2) tr tr:nth-child(8) td:nth-child(8)').text,

                    'Optional Maturity Date': browser.find_element(By.CSS_SELECTOR,
                                                                   'tr:nth-child(2) tr tr:nth-child(10) td:nth-child(8)').text,

                    'Stock Indicator': browser.find_element(By.CSS_SELECTOR,
                                                            'tr:nth-child(2) tr tr:nth-child(11) td:nth-child(8)').text,

                    'Final Redemption Price': browser.find_element(By.CSS_SELECTOR,
                                                                   'tr:nth-child(2) tr tr:nth-child(12) td:nth-child(8)').text,

                    'Outstanding Amount': browser.find_element(By.CSS_SELECTOR,
                                                               'tr:nth-child(2) tr tr:nth-child(13) td:nth-child(8)').text,

                    'Currency': browser.find_element(By.CSS_SELECTOR,
                                                     'tr:nth-child(2) tr tr:nth-child(14) td:nth-child(8)').text,

                    'Issuer': browser.find_element(By.CSS_SELECTOR,
                                                   'tr:nth-child(2) tr tr:nth-child(15) td:nth-child(8)').text,

                    'Secondary Amount': browser.find_element(By.CSS_SELECTOR,
                                                             'fieldset td tr~ tr+ tr legend+ table tr:nth-child(1) td~ td+ td').text,

                    'Primary Amount': browser.find_element(By.CSS_SELECTOR,
                                                           'fieldset td tr~ tr+ tr legend+ table tr:nth-child(2) td~ td+ td').text,

                    'Type (Eg.CUSIP)': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[19]/td[2]/table/tbody/tr/td[1]/table/tbody/tr',
                        2,
                        1),

                    'Alternate ID': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[19]/td[2]/table/tbody/tr/td[1]/table/tbody/tr',
                        2,
                        2),

                    }
    }

    if details['general']['Principle'] == 'ISLAMIC':
        details['profit'] = {
            'Profit Type': browser.find_element(By.CSS_SELECTOR,
                                                'tr~ tr+ tr td > table > tbody > tr:nth-child(1) td:nth-child(4)').text,

            'RENTAS Profit Payment Category': browser.find_element(By.CSS_SELECTOR,
                                                                   'tr~ tr+ tr td > table > tbody > tr:nth-child(2) td:nth-child(4)').text,

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

                'Reset Date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[6]/td/table/tbody/tr',
                    2,
                    ''),

            },

            'Profit Date': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr',
                2, ''),

            'Profit Setting': {

                'Profit End Date Rule': {

                    'Shift End Date': browser.find_element(By.XPATH,
                                                           '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

                    'If Holiday On': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                        2, 1),

                    'Rules': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                        2, 2),

                },

                'Calculation of No of Days in Profit Period': {

                    'For Each Profit Period': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr',
                        2, 1),

                    'Option': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr',
                        2, 2),

                },

                'Profit Payment Date Rule': {

                    'Shift Payment Date': browser.find_element(By.XPATH,
                                                               '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td[3]').text,

                    'If Holiday On': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                        2, 1),

                    'Rules': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                        2, 2),

                }
            },

            'Frequency of Profit Payment': browser.find_element(By.XPATH,
                                                                '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr/td[3]').text,

            'Profit Payment Schedule': {
                'Seq.': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 1),

                'Start Date': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 2),

                'End Date': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 3),

                'Payment Date': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 4),

                'Ex-Date': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 5),

                'Profit Rate (%)': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 6),

                'Tenor': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 7),

                'Entitle for Profit': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 8),

                'Payment Type': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 9),

                'Skip': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 10),

                'If Skip, Allow Profit on Profit (POP)': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 11),

                'Profit on Profit Rate (%)': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 12),

                'Fixing Date': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 13),

                'Reference Rate': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 14),

                'Adjustment Date': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 15),

            }
        }

    else:
        details['coupon'] = {
            'Coupon Type': browser.find_element(By.CSS_SELECTOR,
                                                'tr~ tr+ tr td > table > tbody > tr:nth-child(1) td:nth-child(4)').text,

            'RENTAS Interest Payment Category': browser.find_element(By.CSS_SELECTOR,
                                                                     'tr~ tr+ tr td > table > tbody > tr:nth-child(2) td:nth-child(4)').text,

            'Interest Accrual Start Date': browser.find_element(By.CSS_SELECTOR,
                                                                'tr~ tr+ tr td > table > tbody > tr:nth-child(3) td:nth-child(4)').text,

            'First Interest Date': browser.find_element(By.CSS_SELECTOR,
                                                        'tr~ tr+ tr td > table > tbody > tr:nth-child(4) td:nth-child(4)').text,

            'Last Interest Date': browser.find_element(By.CSS_SELECTOR,
                                                       'tr~ tr+ tr td > table > tbody > tr:nth-child(5) td:nth-child(4)').text,

            'Coupon Rate': browser.find_element(By.CSS_SELECTOR,
                                                'tr~ tr+ tr td > table > tbody > tr:nth-child(7) td:nth-child(4)').text,

            'Ex-Day': browser.find_element(By.CSS_SELECTOR,
                                           'tr~ tr+ tr td > table > tbody > tr:nth-child(4) td:nth-child(9)').text,

            'Day Count Basis': browser.find_element(By.CSS_SELECTOR,
                                                    'tr~ tr+ tr td > table > tbody > tr:nth-child(5) td:nth-child(9)').text,

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

                'Reset Date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[6]/td/table/tbody/tr',
                    2,
                    ''),

            },

            'Interest Date': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr',
                2, ''),

            'Interest Setting': {

                'Interest End Date Rule': {

                    'Shift End Date': browser.find_element(By.XPATH,
                                                           '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

                    'If Holiday On': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                        2, 1),

                    'Rules': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                        2, 2),

                },

                'Calculation of No of Days in Interest Period': {

                    'For Each Interest Period': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr',
                        2, 1),

                    'Option': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr',
                        2, 2),

                },

                'Interest Payment Date Rule': {

                    'Shift Payment Date': browser.find_element(By.XPATH,
                                                               '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td[3]').text,

                    'If Holiday On': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                        2, 1),

                    'Rules': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                        2, 2),

                }
            },

            'Frequency of Interest Payment': browser.find_element(By.XPATH,
                                                                  '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr/td[3]').text,

            'Interest Payment Schedule': {

                'Seq.': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 1),

                'Start Date': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 2),

                'End Date': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 3),

                'Payment Date': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 4),

                'Ex-Date': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 5),

                'Coupon Rate (%)': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 6),

                'Tenor': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 7),

                'Entitle for Coupon': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 8),

                'Payment Type': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 9),

                'Skip': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 10),

                'If Skip, Allow Int. on Int. (IOI)': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 11),

                'Int. on Int. Rate (%)': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 12),

                'Fixing Date': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 13),

                'Reference Rate': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 14),

                'Adjustment Date': self.payment(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr',
                    2, 15),

            }
        }

    details['redemption'] = {
        'Redemption Date': self.row(
            '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[1]/tbody/tr/td/table/tbody/tr',
            2, 1),

        'Redemption Amount (RM)': self.row(
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

                'Start Date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 1),
                'End Date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 2),
                'Call Price': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 3)
            },

            'Lockout Period': {

                'Start Date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[3]/fieldset/table/tbody/tr',
                    2, 1),
                'End Date': self.row(
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

                'Start Date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 1),
                'End Date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 2),
                'Put Price': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 3)
            },

            'Lockout Period': {

                'Start Date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[3]/fieldset/table/tbody/tr',
                    2, 1),
                'End Date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[3]/fieldset/table/tbody/tr',
                    2, 2),
            }
        }

    }

    details['rating'] = {
        'Government Guarantee': browser.find_element(By.XPATH,
                                                     '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[1]/td').text,

        'Indicator': browser.find_element(By.XPATH,
                                          '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td').text,

        'stock rating': {
            'Rating Agency': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                1),

            'Effective Date': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                2),

            'Current Rating Tenure': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                3),

            'Initial Rating': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                4),

            'Current Rating': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                5),

            'Rating Action': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                6),

            'Rating Outlook': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                7),

            'Rating Watch': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                8),
        }
    }

    details['miscellaneous'] = {
        'Trading Details': {
            'Tradable': browser.find_element(By.XPATH,
                                             '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

            'Trading Basis': browser.find_element(By.XPATH,
                                                  '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,
        },

        'Bullet/Revolving': browser.find_element(By.XPATH,
                                                 '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr/td').text,

        'Asset Backed': {
            'Originator': browser.find_element(By.XPATH,
                                               '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

            'SPV': browser.find_element(By.XPATH,
                                        '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,

            'Servicer': browser.find_element(By.XPATH,
                                             '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,

            'Underlying Assets': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr[4]/td/table/tbody/tr',
                2, 1),
        },

        'Islamic Securities': {
            'Purchase Price of Assets': browser.find_element(By.XPATH,
                                                             '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr[1]/td[3]').text,

            'Selling Price of Assets': browser.find_element(By.XPATH,
                                                            '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr[2]/td[3]').text,

            'Value of Assets': browser.find_element(By.XPATH,
                                                    '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr[3]/td[3]').text,

            'Underlying Assets': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr[4]/td/table/tbody/tr',
                2, 1)
        },

        'Inflation Protected': {

            'Inflation Protected': browser.find_element(By.XPATH,
                                                        '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/legend').text,

            'Reference Source': browser.find_element(By.XPATH,
                                                     '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

            'Indices for Benchmark': browser.find_element(By.XPATH,
                                                          '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,

            'Remarks': browser.find_element(By.XPATH,
                                            '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,
        },

        'Indicative Market Price': {

            'Mid Price': browser.find_element(By.XPATH,
                                              '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[2]/fieldset/table/tbody/tr[1]/td[3]').text,

            'Mid Yield (%)': browser.find_element(By.XPATH,
                                                  '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[2]/fieldset/table/tbody/tr[2]/td[3]').text,

            'Mid Discount Rate (%)': browser.find_element(By.XPATH,
                                                          '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[2]/fieldset/table/tbody/tr[3]/td[3]').text,
        },

        'Convertible': {

            'Convertible': browser.find_element(By.XPATH,
                                                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[1]/fieldset/legend').text,

            'Conversion Period': {

                'Start Date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[1]/fieldset/table/tbody/tr[1]/td[3]/table/tbody/tr',
                    2, 1),

                'End Date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[1]/fieldset/table/tbody/tr[1]/td[3]/table/tbody/tr',
                    2, 2),
            },

            'Remarks': browser.find_element(By.XPATH,
                                            '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,
        },

        'Regulatory Status': {

            'code': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[2]/fieldset/table/tbody/tr', 2,
                1),

            'description': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[2]/fieldset/table/tbody/tr', 2,
                2),
        },

        'attachment': {
            'file name': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr', 2, 1),
            'file description': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr', 2, 2),
            'Lead Arranger/ Facility Agent Remarks': browser.find_element(By.XPATH,
                                                                          '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td').text
        }

    }

    self.download(
        self.row('//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr', 2, 1),
        'Facility Information', self.code)

    json_object = json.dumps(details, indent=1)
    # print(code + '\n' + json_object)
    f.write(json_object)

    return dir_path
