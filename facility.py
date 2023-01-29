from selenium.webdriver.common.by import By
import time
import json
import os


def run(self):
    code = self.code
    browser = self.browser
    timestr = time.strftime("%Y-%m-%d-%H%M%S")
    path = 'Facility Information/' + code
    isExist = os.path.exists(path)
    if not isExist:
        os.mkdir(path)
    dir_path = path + '/' + timestr + ".json"
    f = open(dir_path, "a")
    f.write("Facility Information: " + code + "\n")

    # print(code + '\n')
    f.write("Facility Code: " + code + "\n")
    f.write(browser.find_element(By.CSS_SELECTOR, '.tableHeader td+td b').text + "\n")

    # scrape the data on the new page and get back with the following command
    details = {

        'general': {
            'fac_desc': browser.find_element(By.XPATH,
                                             '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td[4]').text,

            'principle': browser.find_element(By.XPATH,
                                              "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td[8]").text,

            'mat_date': browser.find_element(By.XPATH,
                                             "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td[4]").text,

            'mode_of_offer': browser.find_element(By.XPATH,
                                                  "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td[8]").text,

            'acronym': browser.find_element(By.XPATH,
                                            "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[3]/td[4]").text,

            'curr': browser.find_element(By.XPATH,
                                         "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[3]/td[8]").text,

            'issuer': browser.find_element(By.XPATH,
                                           "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[4]/td[4]").text,

            'spread_ref_source': browser.find_element(By.XPATH,
                                                      '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td[3]').text,

            'form_type': browser.find_element(By.XPATH,
                                              '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td[3]').text,

            'FA': browser.find_element(By.XPATH,
                                       '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[1]/td[4]').text,
            'LA': browser.find_element(By.XPATH,
                                       '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[2]/td[4]').text,

            'auth_depository': browser.find_element(By.XPATH,
                                                    '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,
            'paying_agent': browser.find_element(By.XPATH,
                                                 '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,
            'security_agent': browser.find_element(By.XPATH,
                                                   '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,

            'fac_limit': browser.find_element(By.XPATH,
                                              '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[1]/td[4]').text,
            'avai_period': browser.find_element(By.XPATH,
                                                '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[2]/td[4]').text,
            'avai_limit': browser.find_element(By.XPATH,
                                               '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[4]/td[4]').text,
            'outstanding': browser.find_element(By.XPATH,
                                                '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[5]/td[4]').text,

            'fac_app_date_bnm': browser.find_element(By.XPATH,
                                                     '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[1]/td[4]').text,
            'fac_app_date_sc': browser.find_element(By.XPATH,
                                                    '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[2]/td[4]').text,
            'dpa_agr_sign': browser.find_element(By.XPATH,
                                                 '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[3]/td[4]').text,
            'app_expiry': browser.find_element(By.XPATH,
                                               '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[4]/td[4]').text,

            'co_arranger': self.row(
                '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[3]/td/table/tbody/tr',
                2,
                ''),

            'islamic_concept': self.row(
                '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/table[1]/tbody/tr',
                2,
                ''),

            'sell_restriction': self.row(
                '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr[6]/td/table/tbody/tr/td[3]/table[2]/tbody/tr',
                2,
                '')

        },

        'instruments': {

            'inst_code': browser.find_element(By.CSS_SELECTOR, 'tr~ tr+ tr tr tr:nth-child(1) td:nth-child(3) b').text,

            'inst_type': browser.find_element(By.XPATH,
                                              '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td[3]').text,

            'inst_desc': browser.find_element(By.XPATH,
                                              '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[1]/td[6]').text,

            'inst_trx_type': browser.find_element(By.XPATH,
                                                  '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td[6]').text,

            'principle': browser.find_element(By.XPATH,
                                              '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[3]/td[3]').text,

            'bullet_revolving': browser.find_element(By.XPATH,
                                                     '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td').text,

            'inst_limit': browser.find_element(By.XPATH,
                                               '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td[4]').text,
            'mat_date': browser.find_element(By.XPATH,
                                             '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td[4]').text,
            'avai_limit': browser.find_element(By.XPATH,
                                               '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td[4]').text,
            'outstanding': browser.find_element(By.XPATH,
                                                '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td[4]').text,

            'Instrument Participants': {
                'Underwritten': {
                    'underwritten': browser.find_element(By.XPATH,
                                                         '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/legend').text.replace(
                        'Underwritten : ', ''),
                    'auto_deduction': browser.find_element(By.XPATH,
                                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td').text.replace(
                        'Auto deduction of underwriter commitment amount : ', ''),
                    'total_ori_commit': browser.find_element(By.XPATH,
                                                             '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,
                    'total_av_commit': browser.find_element(By.XPATH,
                                                            '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,
                    'organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[4]/td/table/tbody/tr',
                        2,
                        1),
                    'ori_commit': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[4]/td/table/tbody/tr',
                        2,
                        1),
                    'present_avai_comm': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[4]/td/table/tbody/tr',
                        2,
                        1),

                },

                'Guaranteed': {

                    'Guaranteed': browser.find_element(By.XPATH,
                                                       '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/legend').text.replace(
                        'Guaranteed : ', ''),
                    'total_guaranteed': browser.find_element(By.XPATH,
                                                             '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr[1]/td[3]').text,
                    'remarks': browser.find_element(By.XPATH,
                                                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr[3]/td[3]').text,
                    'organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                        2,
                        1),
                    'guaranteed_amount': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr[2]/td/table/tbody/tr',
                        2,
                        2)
                },

                'Direct Bidder': {
                    'organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr/td/table/tbody/tr',
                        2,
                        '')
                },

                'Primary Subscribers': {
                    'organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr/td/table/tbody/tr',
                        2,
                        '')
                },

                'Suspended Direct Bidder': {
                    'organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/table/tbody/tr/td/table/tbody/tr',
                        2,
                        '')
                },

                'Restricted Organisation': {
                    'organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td/fieldset/table/tbody/tr[3]/td[2]/fieldset/table/tbody/tr/td/table/tbody/tr',
                        2,
                        '')
                },

                'Market Maker': {
                    'organisation': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr',
                        2,
                        '')
                },

                'ABS Details': {
                    'abs_originator': browser.find_element(By.XPATH,
                                                           '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[1]/td[4]').text,
                    'abs_servicer': browser.find_element(By.XPATH,
                                                         '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[2]/td[4]').text,
                    'abs_spv': browser.find_element(By.XPATH,
                                                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[3]/td[4]').text,
                    'und_assets': self.row(
                        '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[5]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[4]/td/table/tbody/tr',
                        2, ''),
                },
            }
        },

        'rating': {

            'gov_guarantee_flag': browser.find_element(By.XPATH,
                                                       '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[1]/td').text.replace(
                'Government Guarantee : ', ''),
            'rat_indicator': browser.find_element(By.XPATH,
                                                  '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td').text.replace(
                'Indicator :', ''),
            'facility rating': {
                'inst': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 1),
                'rat_agent': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 2),
                'eff_date': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 3),
                'curr_rate_tnr': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 4),
                'init_rate': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 5),
                'curr_rate': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 6),
                'rat_action': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 7),
                'rat_outlook': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 8),
                'rat_watch': self.row(
                    '/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[4]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr',
                    2, 9),
            },
        },

        'utilisation': {

            'Facility Sectors': {
                'fiss': self.row('//*[@id="tblSector"]/tbody/tr', 1, 1),
                'sector': self.row('//*[@id="tblSector"]/tbody/tr', 1, 2),
                'amount': self.row('//*[@id="tblSector"]/tbody/tr', 1, 3)

            },

            'Facility Utilisation': {
                'fiss': self.row('//*[@id="tblUtilise"]/tbody/tr', 1, 1),
                'util': self.row('//*[@id="tblUtilise"]/tbody/tr', 1, 2),
                'amount': self.row('//*[@id="tblUtilise"]/tbody/tr', 1, 3)
            }
        },

        'attachment': {
            'file_name': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr', 2, 1),
            'file_desc': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr', 2, 2),
            'remarks': browser.find_element(By.XPATH,
                                                                          '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td').text
        }
    }

    self.download(
        self.row('//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr', 2, 1),
        'Facility Information', self.code)

    json_object = json.dumps(details, indent=1)
    # print(code + '\n' + json_object)
    f.write(json_object)

    return dir_path