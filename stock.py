from selenium.webdriver.common.by import By
import time
import json
import os


def run(self):
    code = self.code
    browser = self.browser
    timestr = time.strftime("%Y-%m-%d-%H%M%S")
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
        'general': {'inst_id': browser.find_element(By.CSS_SELECTOR,
                                                    'tr:nth-child(2) tr tr:nth-child(1) td:nth-child(4)').text,

                    'stk_code': browser.find_element(By.CSS_SELECTOR,
                                                     'tr:nth-child(2) tr tr:nth-child(2) td:nth-child(4)').text,

                    'serial': browser.find_element(By.CSS_SELECTOR,
                                                   'tr:nth-child(2) tr tr:nth-child(3) td:nth-child(4)').text,

                    'this_yr_series': browser.find_element(By.CSS_SELECTOR,
                                                           'tr:nth-child(2) tr tr:nth-child(4) td:nth-child(4)').text,

                    'isin_code': browser.find_element(By.CSS_SELECTOR,
                                                      'tr:nth-child(2) tr tr:nth-child(5) td:nth-child(4)').text,

                    'stk_desc': browser.find_element(By.CSS_SELECTOR,
                                                     'tr:nth-child(2) tr tr:nth-child(6) td:nth-child(4)').text,

                    'stk_cat': browser.find_element(By.CSS_SELECTOR,
                                                    'tr:nth-child(2) tr tr:nth-child(7) td:nth-child(4)').text,

                    'principle': browser.find_element(By.CSS_SELECTOR,
                                                      'tr:nth-child(2) tr tr:nth-child(8) td:nth-child(4)').text,

                    'iss_date': browser.find_element(By.CSS_SELECTOR,
                                                     'tr:nth-child(2) tr tr:nth-child(9) td:nth-child(4)').text,

                    'mat_date': browser.find_element(By.CSS_SELECTOR,
                                                     'tr:nth-child(2) tr tr:nth-child(10) td:nth-child(4)').text,

                    'pri_stk': browser.find_element(By.CSS_SELECTOR,
                                                    'tr:nth-child(2) tr tr:nth-child(11) td:nth-child(4)').text,

                    'opt_pro_date': browser.find_element(By.CSS_SELECTOR,
                                                         'tr:nth-child(2) tr tr:nth-child(12) td:nth-child(4)').text,

                    'iss_amt': browser.find_element(By.CSS_SELECTOR,
                                                    'tr:nth-child(2) tr tr:nth-child(13) td:nth-child(4)').text,

                    'LA': browser.find_element(By.CSS_SELECTOR,
                                               'tr:nth-child(2) tr tr:nth-child(14) td:nth-child(4)').text,

                    'FA': browser.find_element(By.CSS_SELECTOR,
                                               'tr:nth-child(2) tr tr:nth-child(15) td:nth-child(4)').text,

                    'detach': browser.find_element(By.CSS_SELECTOR,
                                                   'tr:nth-child(2) tr tr:nth-child(16) td:nth-child(4)').text,

                    'fac_code': browser.find_element(By.CSS_SELECTOR,
                                                     'tr:nth-child(2) tr tr:nth-child(1) td:nth-child(8)').text,

                    'shrt_name': browser.find_element(By.CSS_SELECTOR,
                                                      'tr:nth-child(2) tr tr:nth-child(2) td:nth-child(8)').text,

                    'pay_acct': browser.find_element(By.CSS_SELECTOR,
                                                     'tr:nth-child(2) tr tr:nth-child(7) td:nth-child(8)').text,

                    'sto_sta': browser.find_element(By.CSS_SELECTOR,
                                                    'tr:nth-child(2) tr tr:nth-child(8) td:nth-child(8)').text,

                    'opt_mat_date': browser.find_element(By.CSS_SELECTOR,
                                                         'tr:nth-child(2) tr tr:nth-child(10) td:nth-child(8)').text,

                    'stk_ind': browser.find_element(By.CSS_SELECTOR,
                                                    'tr:nth-child(2) tr tr:nth-child(11) td:nth-child(8)').text,

                    'fin_red_price': browser.find_element(By.CSS_SELECTOR,
                                                          'tr:nth-child(2) tr tr:nth-child(12) td:nth-child(8)').text,

                    'out_amt': browser.find_element(By.CSS_SELECTOR,
                                                    'tr:nth-child(2) tr tr:nth-child(13) td:nth-child(8)').text,

                    'curr': browser.find_element(By.CSS_SELECTOR,
                                                 'tr:nth-child(2) tr tr:nth-child(14) td:nth-child(8)').text,

                    'issuer': browser.find_element(By.CSS_SELECTOR,
                                                   'tr:nth-child(2) tr tr:nth-child(15) td:nth-child(8)').text,

                    'sn_sec_amt': browser.find_element(By.CSS_SELECTOR,
                                                       'fieldset td tr~ tr+ tr legend+ table tr:nth-child(1) td~ td+ td').text,

                    'sn_pri_amt': browser.find_element(By.CSS_SELECTOR,
                                                       'fieldset td tr~ tr+ tr legend+ table tr:nth-child(2) td~ td+ td').text,

                    'type': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[19]/td[2]/table/tbody/tr/td[1]/table/tbody/tr',
                        2,
                        1),

                    'alt_id': self.row(
                        '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td/table/tbody/tr[19]/td[2]/table/tbody/tr/td[1]/table/tbody/tr',
                        2,
                        2),

                    }
    }

    if details['general']['principle'] == 'ISLAMIC':
        details['profit'] = {
            'pft_type': browser.find_element(By.CSS_SELECTOR,
                                             'tr~ tr+ tr td > table > tbody > tr:nth-child(1) td:nth-child(4)').text,

            'ren_pft_pay_cat': browser.find_element(By.CSS_SELECTOR,
                                                    'tr~ tr+ tr td > table > tbody > tr:nth-child(2) td:nth-child(4)').text,

            'Floating Rate Information': {

                'flo_ref_src': browser.find_element(By.XPATH,
                                                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

                'flo_margin': browser.find_element(By.XPATH,
                                                   '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,

                'flo_exday_fix_date': browser.find_element(By.XPATH,
                                                           '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,

                'flo_cap_rate': browser.find_element(By.XPATH,
                                                     '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[4]/td[3]').text,

                'flo_flr_rate': browser.find_element(By.XPATH,
                                                     '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[5]/td[3]').text,

                'reset_date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[6]/td/table/tbody/tr',
                    2,
                    ''),

            },

            'pft_date': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr',
                2, ''),

            'Profit Setting': {

                'Profit End Date Rule': {

                    'shft_end_date': browser.find_element(By.XPATH,
                                                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

                    'shft_end_date_norm': browser.find_element(By.CSS_SELECTOR,
                                                               '#SpanPrint td td fieldset tr:nth-child(1) tr .tableHeader+ tr td+ td').text,

                    'shft_end_date_eom': browser.find_element(By.CSS_SELECTOR,
                                                              '#SpanPrint td td fieldset tr:nth-child(1) tr .evenrow td+ td').text,

                    'shft_end_date_eoy': browser.find_element(By.CSS_SELECTOR,
                                                              '#SpanPrint td td fieldset tr:nth-child(1) .evenrow+ tr td+ td').text,

                },

                'Calculation of No of Days in Profit Period': {

                    'pro_per_start_date': browser.find_element(By.CSS_SELECTOR,
                                                               '#SpanPrint td td fieldset fieldset br+ table .tableHeader+ tr td+ td').text,

                    'pro_per_end_date': browser.find_element(By.CSS_SELECTOR,
                                                             '#SpanPrint td td fieldset fieldset br+ table .evenrow td+ td').text,

                },

                'Profit Payment Date Rule': {

                    'Shift Payment Date': browser.find_element(By.XPATH,
                                                               '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td[3]').text,

                    'shft_pay_date_norm': browser.find_element(By.CSS_SELECTOR,
                                                               '#SpanPrint td td tr+ tr tr .tableHeader+ tr td+ td').text,

                    'shft_pay_date_eom': browser.find_element(By.CSS_SELECTOR,
                                                              '#SpanPrint td td tr+ tr tr .evenrow td+ td').text,

                    'shft_pay_date_eoy': browser.find_element(By.CSS_SELECTOR,
                                                              '#SpanPrint td td tr+ tr tr .evenrow+ tr td+ td').text,

                }
            },

            'fre_pft_pay': browser.find_element(By.XPATH,
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
            'coupun_type': browser.find_element(By.CSS_SELECTOR,
                                                'tr~ tr+ tr td > table > tbody > tr:nth-child(1) td:nth-child(4)').text,

            'ren_intr_pay_cat': browser.find_element(By.CSS_SELECTOR,
                                                     'tr~ tr+ tr td > table > tbody > tr:nth-child(2) td:nth-child(4)').text,

            'intr_accr_sta_date': browser.find_element(By.CSS_SELECTOR,
                                                       'tr~ tr+ tr td > table > tbody > tr:nth-child(3) td:nth-child(4)').text,

            'fir_intr_pay_date': browser.find_element(By.CSS_SELECTOR,
                                                      'tr~ tr+ tr td > table > tbody > tr:nth-child(4) td:nth-child(4)').text,

            'las_intr_pay_date': browser.find_element(By.CSS_SELECTOR,
                                                      'tr~ tr+ tr td > table > tbody > tr:nth-child(5) td:nth-child(4)').text,

            'coupon_rate': browser.find_element(By.CSS_SELECTOR,
                                                'tr~ tr+ tr td > table > tbody > tr:nth-child(7) td:nth-child(4)').text,

            'ex-day': browser.find_element(By.CSS_SELECTOR,
                                           'tr~ tr+ tr td > table > tbody > tr:nth-child(4) td:nth-child(9)').text,

            'day_cnt_bas': browser.find_element(By.CSS_SELECTOR,
                                                'tr~ tr+ tr td > table > tbody > tr:nth-child(5) td:nth-child(9)').text,

            'Floating Rate Information': {

                'flo_ref_src': browser.find_element(By.XPATH,
                                                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

                'flo_margin': browser.find_element(By.XPATH,
                                                   '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,

                'flo_exday_fix_date': browser.find_element(By.XPATH,
                                                           '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,

                'flo_cap_rate': browser.find_element(By.XPATH,
                                                     '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[4]/td[3]').text,

                'flo_flr_rate': browser.find_element(By.XPATH,
                                                     '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[5]/td[3]').text,

                'reset_date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[1]/fieldset/table/tbody/tr[6]/td/table/tbody/tr',
                    2,
                    ''),

            },

            'intr_date': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr',
                2, ''),

            'Interest Setting': {

                'Interest End Date Rule': {

                    'shft_end_date': browser.find_element(By.XPATH,
                                                          '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

                    'shft_end_date_norm': browser.find_element(By.CSS_SELECTOR,
                                                               '#SpanPrint td td fieldset tr:nth-child(1) tr .tableHeader+ tr td+ td').text,

                    'shft_end_date_eom': browser.find_element(By.CSS_SELECTOR,
                                                              '#SpanPrint td td fieldset tr:nth-child(1) tr .evenrow td+ td').text,

                    'shft_end_date_eoy': browser.find_element(By.CSS_SELECTOR,
                                                              '#SpanPrint td td fieldset tr:nth-child(1) .evenrow+ tr td+ td').text,

                },

                'Calculation of No of Days in Interest Period': {

                    'pro_per_start_date': browser.find_element(By.CSS_SELECTOR,
                                                               '#SpanPrint td td fieldset fieldset br+ table .tableHeader+ tr td+ td').text,

                    'pro_per_end_date': browser.find_element(By.CSS_SELECTOR,
                                                             '#SpanPrint td td fieldset fieldset br+ table .evenrow td+ td').text,

                },

                'Interest Payment Date Rule': {

                    'Shift Payment Date': browser.find_element(By.XPATH,
                                                               '//*[@id="SpanPrint"]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td[3]').text,

                    'shft_pay_date_norm': browser.find_element(By.CSS_SELECTOR,
                                                               '#SpanPrint td td tr+ tr tr .tableHeader+ tr td+ td').text,

                    'shft_pay_date_eom': browser.find_element(By.CSS_SELECTOR,
                                                              '#SpanPrint td td tr+ tr tr .evenrow td+ td').text,

                    'shft_pay_date_eoy': browser.find_element(By.CSS_SELECTOR,
                                                              '#SpanPrint td td tr+ tr tr .evenrow+ tr td+ td').text,

                }
            },

            'fre_intr_pay': browser.find_element(By.XPATH,
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
        'redm_date': self.row(
            '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[1]/tbody/tr/td/table/tbody/tr',
            2, 1),

        'redm_amt': self.row(
            '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[1]/tbody/tr/td/table/tbody/tr/td[2]', 2, 2),

        'Call Details': {
            'call_det': browser.find_element(By.XPATH,
                                             '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/legend').text.replace(
                'Call Details : ', ''),

            'call_part': browser.find_element(By.XPATH,
                                              '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[1]/tbody/tr[1]/td').text.replace(
                'Allow Partial Call : ', ''),

            'call_round_denom': browser.find_element(By.XPATH,
                                                     '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[1]/tbody/tr[2]/td').text.replace(
                '    Redeem to the nearest denomination : ', ''),

            # 'Acc.': browser.find_element(By.XPATH,
            #                              '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[1]/tbody/tr[3]/td[2]').text,

            # 'Profit On Profit Rate': browser.find_element(By.XPATH,
            #                                               '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[1]/tbody/tr[3]/td[5]').text,

            'Call Schedule': {

                'call_sta_date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 1),
                'call_end_date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 2),
                'call_price': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 3)
            },

            'Lockout Period': {

                'lp_sta_date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[3]/fieldset/table/tbody/tr',
                    2, 1),
                'lp_end_date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[1]/td/fieldset/table[2]/tbody/tr/td[3]/fieldset/table/tbody/tr/td[2]',
                    2, 2),
            }
        },

        'Put Details': {

            'put_det': browser.find_element(By.XPATH,
                                            '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/legend').text.replace(
                'Put Details : ', ''),

            'put_part': browser.find_element(By.XPATH,
                                             '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[1]/tbody/tr[1]/td').text.replace(
                'Allow Partial Put : ', ''),

            'put_round_denom': browser.find_element(By.XPATH,
                                                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[1]/tbody/tr[2]/td').text.replace(
                '    Redeem to the nearest denomination : ', ''),

            'Put Schedule': {

                'put_sta_date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 1),
                'put_end_date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 2),
                'put_price': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr',
                    2, 3)
            },

            'Lockout Period': {

                'lp_sta_date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[3]/fieldset/table/tbody/tr',
                    2, 1),
                'lp_end_date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[4]/td/fieldset/table[2]/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td[3]/fieldset/table/tbody/tr',
                    2, 2),
            }
        }

    }

    details['rating'] = {
        'Government Guarantee': browser.find_element(By.XPATH,
                                                     '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[1]/td').text.replace(
            'Government Guarantee : ', ''),

        'indicator': browser.find_element(By.XPATH,
                                          '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr[2]/td').text.replace(
            'Indicator : ', ''),

        'stock rating': {
            'rat_agent': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                1),

            'eff_date': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                2),

            'curr_rate_tnr': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                3),

            'init_rate': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                4),

            'curr_rate': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                5),

            'rat_action': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                6),

            'rat_outlook': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                7),

            'rat_watch': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[5]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr', 2,
                8),
        }
    }

    details['miscellaneous'] = {
        'Trading Details': {
            'tradable': browser.find_element(By.XPATH,
                                             '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

            'trade_basis': browser.find_element(By.XPATH,
                                                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,
        },

        'bullet_revolving': browser.find_element(By.XPATH,
                                                 '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td[2]/fieldset/table/tbody/tr/td').text,

        'Asset Backed': {
            'abs_originator': browser.find_element(By.XPATH,
                                                   '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

            'abs_spv': browser.find_element(By.XPATH,
                                            '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,

            'abs_servicer': browser.find_element(By.XPATH,
                                                 '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,

            'und_assets': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[1]/fieldset/table/tbody/tr[4]/td/table/tbody/tr',
                2, 1),
        },

        'Islamic Securities': {
            'purchase_pr_assets': browser.find_element(By.XPATH,
                                                       '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr[1]/td[3]').text,

            'selling_pr_assets': browser.find_element(By.XPATH,
                                                      '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr[2]/td[3]').text,

            'value_assets': browser.find_element(By.XPATH,
                                                 '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr[3]/td[3]').text,

            'und_assets': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td[2]/fieldset/table/tbody/tr[4]/td/table/tbody/tr',
                2, 1)
        },

        'Inflation Protected': {

            'inflat_prtc': browser.find_element(By.XPATH,
                                                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/legend').text.replace(
                'Inflation Protected : ', ''),

            'ref_source': browser.find_element(By.XPATH,
                                               '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/table/tbody/tr[1]/td[3]').text,

            'indices': browser.find_element(By.XPATH,
                                            '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/table/tbody/tr[2]/td[3]').text,

            'remarks': browser.find_element(By.XPATH,
                                            '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[1]/fieldset/table/tbody/tr[3]/td[3]').text,
        },

        'Indicative Market Price': {

            'mid_price': browser.find_element(By.XPATH,
                                              '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[2]/fieldset/table/tbody/tr[1]/td[3]').text,

            'mid_yield': browser.find_element(By.XPATH,
                                              '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[2]/fieldset/table/tbody/tr[2]/td[3]').text,

            'mid_disc_rate': browser.find_element(By.XPATH,
                                                  '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[3]/td[2]/fieldset/table/tbody/tr[3]/td[3]').text,
        },

        'Convertible': {

            'convertible': browser.find_element(By.XPATH,
                                                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[1]/fieldset/legend').text.replace(
                'Convertible : ', ''),

            'Conversion Period': {

                'start_date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[1]/fieldset/table/tbody/tr[1]/td[3]/table/tbody/tr',
                    2, 1),

                'end_date': self.row(
                    '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[5]/td[1]/fieldset/table/tbody/tr[1]/td[3]/table/tbody/tr',
                    2, 2),
            },

            'remarks': browser.find_element(By.XPATH,
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
            'file_name': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr',
                2, 1),
            'file_desc': self.row(
                '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr',
                2, 2),
            'remarks': browser.find_element(By.XPATH,
                                            '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[6]/td/fieldset/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td').text
        }

    }

    self.download(
        self.row(
            '//*[@id="SpanPrint"]/table/tbody/tr[6]/td/fieldset/table/tbody/tr[6]/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr',
            2, 1),
        'Stock Information', self.code)

    json_object = json.dumps(details, indent=1)
    # print(code + '\n' + json_object)
    f.write(json_object)

    return dir_path
