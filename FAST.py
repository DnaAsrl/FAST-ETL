import shutil
import threading
import tkinter as tk
import os
import mysql.connector
import time
import announcement
import facility
import stock

from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from threading import Event
from jsoncomparison import Compare, NO_DIFF


def handle_file():
    isExist = os.path.exists('Announcement')
    if not isExist:
        os.mkdir('Announcement')

    isExist = os.path.exists('Download')
    if not isExist:
        os.mkdir('Download')

    isExist = os.path.exists('Facility Information')
    if not isExist:
        os.mkdir('Facility Information')

    isExist = os.path.exists('Stock Information')
    if not isExist:
        os.mkdir('Stock Information')

    isExist = os.path.exists('Download')
    if not isExist:
        os.mkdir('Download')


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('FAST Scraper')
        self.geometry('680x430')
        self.resizable(0, 0)

        self.create_header_frame()
        self.create_body_frame()
        self.create_footer_frame()
        self.event = Event()
        self.url = None
        self.thread = None
        self.stop_threads = Event()

        self.db_conn()
        self.browser = None
        self.code = None

    def db_conn(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="fastdb"
            )
            self.mycursor = self.mydb.cursor(buffered=True)
        except Exception as e:
            print("Error connecting to database!", e)

    def create_header_frame(self):

        self.header = ttk.Frame(self)

        # # configure the grid
        self.header.columnconfigure(4, weight=5)

        # scrape button
        self.scrape_button = ttk.Button(self.header, text='Scape All')
        self.scrape_button['command'] = self.thread_scrape
        self.scrape_button.grid(column=4, row=0, sticky=tk.E)

        # scrape button
        self.announcement_button = ttk.Button(self.header, text='All Announcement')
        self.announcement_button['command'] = self.handle_announcement
        self.announcement_button.grid(column=0, row=0, sticky=tk.W)

        # scrape button
        self.facility_button = ttk.Button(self.header, text='Facility Information')
        self.facility_button['command'] = self.handle_facility
        self.facility_button.grid(column=1, row=0, sticky=tk.W)

        # scrape button
        self.stock_button = ttk.Button(self.header, text='Stock Information')
        self.stock_button['command'] = self.handle_stock
        self.stock_button.grid(column=2, row=0, sticky=tk.W)

        # scrape button
        self.auction_button = ttk.Button(self.header, text='Auction Calendar')
        self.auction_button['command'] = self.handle_auction
        self.auction_button.grid(column=3, row=0, sticky=tk.W)

        # attach the header frame
        self.header.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)

    def create_body_frame(self):
        self.body = ttk.Frame(self)
        # text and scrollbar
        self.text = tk.Text(self.body, height=20)
        self.text.grid(column=0, row=1)

        scrollbar = ttk.Scrollbar(self.body, orient='vertical', command=self.text.yview)

        scrollbar.grid(column=1, row=1, sticky=tk.NS)
        self.text['yscrollcommand'] = scrollbar.set

        # attach the body frame
        self.body.grid(column=0, row=1, sticky=tk.NSEW, padx=10, pady=10)

    def create_footer_frame(self):
        self.footer = ttk.Frame(self)
        # configure the grid
        self.footer.columnconfigure(0, weight=1)
        # exit button
        self.exit_button = ttk.Button(self.footer, text='Stop Scheduling', command=self.stop)

        self.exit_button.grid(column=0, row=0, sticky=tk.E)

        # attach the footer frame
        self.footer.grid(column=0, row=2, sticky=tk.NSEW, padx=10, pady=10)

    def stop(self):
        self.stop_threads.set()
        self.thread = None

    def check_thread(self):
        if self.thread is not None:
            self.scrape_button['state'] = 'disabled'
            self.announcement_button['state'] = 'disabled'
            self.facility_button['state'] = 'disabled'
            self.stock_button['state'] = 'disabled'
            self.auction_button['state'] = 'disabled'

        else:
            self.scrape_button['state'] = 'normal'
            self.announcement_button['state'] = 'normal'
            self.facility_button['state'] = 'normal'
            self.stock_button['state'] = 'normal'
            self.auction_button['state'] = 'normal'

        # check again after 100ms
        self.after(100, self.check_thread)

    def thread_scrape(self):
        self.stop_threads.clear()
        self.thread = threading.Thread(target=self.handle_all)
        self.thread.start()

    def handle_all(self):
        urls = [
            "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB010400",
            "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030800",
            "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030900",
            "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB050500"
        ]

        while not self.stop_threads.is_set():
            # execute extraction in a loop
            for url in urls:
                # start scraping
                self.url = url
                self.run()

            if not self.stop_threads.is_set():
                time.sleep(1200)
                self.after(60000, self.handle_all())

        self.check_thread()
        self.text.insert(1.0, "Scheduler stopped!\n")
        raise Exception("Scheduler stopped!")

    def run(self):
        if not self.stop_threads.is_set():
            self.check_thread()
            s = Service("C:\Program Files (x86)\chromedriver.exe")
            self.chrome_options = Options()

            downloadFilepath = os.path.abspath(os.getcwd()) + '\\Download'
            prefs = {
                'download.default_directory': downloadFilepath}
            self.chrome_options.add_experimental_option('prefs', prefs)
            self.chrome_options.headless = True  # selenium work in the background
            self.browser = webdriver.Chrome(service=s, options=self.chrome_options)
            self.browser.get(self.url)

            page = 1

            # Page title
            title = self.browser.find_element(By.CLASS_NAME, "styTitle").text
            print(title)
            self.text.insert(1.0, title + "\n")
            title = title.replace(" ", "_").lower()

            while True:

                try:
                    self.text.insert(2.0, "Page:" + str(page) + "\n")
                    print("Page:", page)

                    # wait for the driver to find table
                    WebDriverWait(self.browser, 10).until(
                        EC.presence_of_element_located((By.ID, "BrowseTable"))
                    )

                    actions = ActionChains(self.browser)

                    # get the total links amount
                    links = self.browser.find_elements(By.CSS_SELECTOR, "#BrowseTable td:nth-child(2) a")

                    for index, val in enumerate(links):
                        if not self.stop_threads.is_set():
                            # get the links again after getting back to the initial page in the loop
                            links = self.browser.find_elements(By.CSS_SELECTOR, "#BrowseTable td:nth-child(2) a")
                            th = self.browser.find_elements(By.CSS_SELECTOR, "#BrowseTable th + th")
                            tr = self.browser.find_elements(By.CSS_SELECTOR, "#BrowseTable tr + tr")
                            td = tr[index].find_elements(By.CSS_SELECTOR, "td + td")

                            # scroll to the n-th link, it may be out of the initially visible area
                            actions.move_to_element(links[index]).perform()
                            self.code = links[index].find_element(By.CSS_SELECTOR, "u").text
                            child = links[index].get_attribute('href')

                            dicts = {}

                            for k in range(len(th)):
                                dicts[th[k].text.replace(" ", "_").lower()] = td[k].text

                            # print(dicts)

                            # check if already exist in database
                            if title == 'more_auction_calendar':
                                sql1 = "SELECT * FROM " + title + " WHERE issues LIKE '" + td[
                                    0].text + "' AND target_quarter LIKE '" + td[1].text + "' AND target_month LIKE '" + td[
                                           2].text + "' AND target_year LIKE '" + td[3].text + "'"
                                # print(sql1)
                                self.mycursor.execute(sql1)
                                result = self.mycursor.fetchone()
                                # print(result)

                            else:
                                sql1 = "SELECT * FROM " + title + " WHERE " + th[0].text.replace(" ", "_").lower() + " LIKE '" + td[0].text + "'"
                                # print(sql)
                                self.mycursor.execute(sql1)
                                result = self.mycursor.fetchone()
                                # print(result)

                            now = datetime.now()
                            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                            print(dt_string)
                            self.text.insert(3.0, dt_string + ": saving " + th[0].text + ": " + td[0].text + "\n")
                            print("saving " + th[0].text + ": " + td[0].text)

                            if not result:
                                # Insert into database
                                for x in dicts.keys():
                                    if x == "maturity_date" or x == "issue_date":
                                        if dicts[x] != '-':
                                            datetime_str = dicts[x]
                                            dicts[x] = datetime.strptime(datetime_str, '%d/%m/%Y').strftime('%Y-%m-%d')
                                    if x == "embargo_date":
                                        if dicts[x] != '-':
                                            datetime_str = dicts[x].strip(" APM")
                                            dicts[x] = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S').strftime(
                                                '%Y-%m-%d %H:%M:%S')
                                    if dicts[x] == '-':
                                        dicts[x] = None

                                insert = {
                                    key: value for key, value in dicts.items() if value is not None
                                }

                                try:
                                    columns = ', '.join(
                                        "`" + str(x).replace("**_", "").replace("_(rm_million)", "") + "`" for x in
                                        insert.keys()) + ",`created_at`"
                                    values = ', '.join(
                                        "'" + str(x).replace("'", "") + "'" for x in insert.values()) + ",'" + dt_string + "'"
                                    sql2 = "INSERT INTO %s ( %s ) VALUES ( %s );" % (title, columns, values)
                                    # print(sql2)
                                    self.mycursor.execute(sql2)
                                    self.mydb.commit()
                                    print(self.mycursor.rowcount, "record inserted.")
                                except mysql.connector.Error as err:
                                    print("Something went wrong: {}".format(err))
                                    self.text.insert(2.0, "Something went wrong when saving" + th[0].text + ": " + td[0].text)

                            # scrape inside details
                            if title == 'more_auction_calendar':
                                links[index].click()
                                try:
                                    WebDriverWait(self.browser, 3).until(
                                        EC.alert_is_present())  # this will wait 5 seconds for alert to appear
                                    alert = self.browser.switch_to.alert  # or self.driver.switch_to_alert() depends on your selenium version
                                    alert.accept()
                                except TimeoutException:
                                    pass

                            else:
                                self.browser.execute_script("window.open('');")
                                self.browser.switch_to.window(self.browser.window_handles[-1])
                                self.browser.get(child)
                                try:
                                    WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#SpanPrint td')))
                                    if title == 'all_announcements':
                                        dir_path = announcement.run(self)
                                        self.insert_filepath('announcement_dir', dt_string, dir_path, 'news_id')
                                    if title == 'facility_information':
                                        dir_path = facility.run(self)
                                        self.insert_filepath('facility_dir', dt_string, dir_path, 'facility_code')
                                    if title == 'stock_information':
                                        dir_path = stock.run(self)
                                        self.insert_filepath('stock_dir', dt_string, dir_path, 'stock_code')
                                except TimeoutException:
                                    print('Page not loaded!')
                                self.browser.close()
                                self.browser.switch_to.window(self.browser.window_handles[0])

                    # wait for driver to find next button
                    next_page = WebDriverWait(self.browser, 10).until(
                        EC.element_to_be_clickable((By.LINK_TEXT, "[Next]"))
                    )

                    # Max pages to scrape
                    # as it will go the next page, the count will increase to indicates the next page
                    page += 1
                    if page < 2:
                        next_page.click()
                    else:
                        self.text.insert(2.0, 'Scraping Completed!\n')
                        print("Complete")
                        self.thread = None
                        break

                except TimeoutException:
                    self.text.insert(2.0, 'Scraping stopped as there is no more pages found!\n')
                    # if the driver could not find next clickable, it will end the loop
                    break

            self.browser.quit()

    # testing one by one
    def handle_announcement(self):
        # Scrape Urls
        self.stop_threads.clear()
        self.url = 'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB010400'
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def handle_facility(self):
        # Scrape Urls
        self.stop_threads.clear()
        self.url = 'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030800'
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def handle_stock(self):
        # Scrape Urls
        self.stop_threads.clear()
        self.url = 'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030900'
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def handle_auction(self):
        # Scrape Urls
        self.stop_threads.clear()
        self.url = 'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB050500'
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def insert_filepath(self, table, dt_string, dir_path, code):
        try:
            values = "'" + self.code + "','" + dir_path + "','" + dt_string + "'"
            sql = "INSERT INTO %s (`%s`, `dir_path`, `created_at`) VALUES ( %s );" % (table, code, values)
            # print(sql2)
            self.mycursor.execute(sql)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    # child details scrape function
    def row(self, xpath, tr, td):
        item = []

        while True:
            try:
                if td == '':
                    x = self.browser.find_element(By.XPATH, xpath + '[' + str(tr) + ']').text
                else:
                    x = self.browser.find_element(By.XPATH, xpath + '[' + str(tr) + ']/td[' + str(td) + ']').text

                tr += 1
                item.append(x)

            except NoSuchElementException:
                break

        return item

    def download(self, attachment, title, code):

        for file in attachment:
            link = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, file))
            )
            link.click()
            time.sleep(5)

            # move file
            try:
                old_dir = os.path.abspath(os.getcwd()) + '\\Download\\' + file
                new_dir = os.path.abspath(os.getcwd()) + '\\' + title + '\\' + code
                isExist = os.path.exists(new_dir + '\\' + file)
                # delete previous downloaded file
                if isExist:
                    os.remove(new_dir + '\\' + file)
                shutil.move(old_dir, new_dir)
            except OSError as e:
                print('No such file or directory', e)
                pass

    def payment(self, xpath, tr, td):
        item = []

        while True:
            try:
                if td == '':
                    x = self.browser.find_element(By.XPATH, xpath + '[' + str(tr) + ']').text
                else:
                    x = self.browser.find_element(By.XPATH, xpath + '[' + str(tr) + ']/td[' + str(td) + ']').text

                tr += 2
                item.append(x)

            except NoSuchElementException:
                break

        return item


if __name__ == "__main__":
    handle_file()
    app = App()
    app.mainloop()
