from selenium.webdriver.common.by import By
import time
import json
import os


def run(self):
    code = self.code
    browser = self.browser
    timestr = time.strftime("%Y-%m-%d %H%M%S")
    path = 'Facility Information/' + code
    isExist = os.path.exists(path)
    if not isExist:
        os.mkdir(path)
    f = open(path + '/' + timestr + ".json", "a")
    f.write("Facility Information: " + code + "\n")

    # print(code + '\n')
    f.write("Facility Code: " + code + "\n")

    # scrape the data on the new page and get back with the following command
    details = {

        'general': {
            'description': browser.find_element(By.XPATH,
                                                '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td[4]').text,

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
            'co-arranger': self.row(
                '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[3]/td/table/tbody/tr',
                2,
                ''),

            'Islamic Concept': self.row(
                '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/table[1]/tbody/tr',
                2,
                ''),

            'Selling Restriction': self.row(
                '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/table[2]/tbody/tr',
                2,
                '')

        },

        'instruments': {

            'Instrument Code': browser.find_element(By.XPATH,
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
                    'organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[4]/td/table/tbody/tr',
                        2,
                        1),
                    'Original Commitment': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[4]/td/table/tbody/tr',
                        2,
                        1),
                    'Present Available Commitment (RM)': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[4]/td/table/tbody/tr',
                        2,
                        1),

                },

                'Guaranteed': {

                    'Guaranteed': browser.find_element(By.XPATH,
                                                       '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/legend').text,
                    'Total Guaranteed (RM)': browser.find_element(By.XPATH,
                                                                  '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr[1]/td[3]').text,
                    'Remarks': browser.find_element(By.XPATH,
                                                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr[3]/td[3]').text,
                    'Organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                        2,
                        1),
                    'Guaranteed Amount (RM)': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                        2,
                        2)
                },

                'Direct Bidder': {
                    'Organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr/td/table/tbody/tr',
                        2,
                        '')
                },

                'Primary Subscribers': {
                    'Organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr/td/table/tbody/tr',
                        2,
                        '')
                },

                'Suspended Direct Bidder': {
                    'Organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/table/tbody/tr/td/table/tbody/tr',
                        2,
                        '')
                },

                'Restricted Organisation': {
                    'Organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[3]/td[2]/fieldset/table/tbody/tr/td/table/tbody/tr',
                        2,
                        '')
                },

                'Market Maker': {
                    'Organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr',
                        2,
                        '')
                },

                'ABS Details': {
                    'Originator': browser.find_element(By.XPATH,
                                                       '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[1]/td[4]').text,
                    'Servicer': browser.find_element(By.XPATH,
                                                     '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[2]/td[4]').text,
                    'Special Purpose Vehicle (SPV)': browser.find_element(By.XPATH,
                                                                          '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[3]/td[4]').text,
                    'Underlying Assets': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[4]/td/table/tbody/tr',
                        2, ''),
                },
            }
        },

        'rating': {

            'Government Guarantee': browser.find_element(By.XPATH,
                                                         '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[1]/td').text,
            'Indicator': browser.find_element(By.XPATH,
                                              '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td').text,
            'facility rating': {
                'Instrument': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 1),
                'Rating Agency': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 2),
                'Effective Date': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 3),
                'Current Rating Tenure': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 4),
                'Initial Rating': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 5),
                'Current Rating': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 6),
                'Rating Action': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 7),
                'Rating Outlook': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 8),
                'Rating Watch': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 9),
            },
        },

        'utilisation': {

            'Facility Sectors': {
                'FISS': self.row('//*[@id="tblSector"]/tbody/tr', 1, 1),
                'Sector': self.row('//*[@id="tblSector"]/tbody/tr', 1, 2),
                'Amount (RM)': self.row('//*[@id="tblSector"]/tbody/tr', 1, 3)

            },

            'Facility Utilisation': {
                'FISS': self.row('//*[@id="tblUtilise"]/tbody/tr', 1, 1),
                'Utilisation': self.row('//*[@id="tblUtilise"]/tbody/tr', 1, 2),
                'Amount (RM)': self.row('//*[@id="tblUtilise"]/tbody/tr', 1, 3)
            }
        },

        'attachment': {
            'file name': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr', 2, 1),
            'file description': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr', 2, 2),
            'Lead Arranger/ Facility Agent Remarks': browser.find_element(By.XPATH,
                                                                          '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td').text
        }
    }

    self.download(
        self.row('//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr', 2, 1),
        'Facility Information', self.code)

    json_object = json.dumps(details, indent=1)
    # print(code + '\n' + json_object)
    f.write(json_object)
