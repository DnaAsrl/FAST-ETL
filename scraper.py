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


def thread_scrape(self):
    self.thread = threading.Thread(target=self.handle_all)
    self.thread.start()


# testing one by one
def handle_announcement(self):
    # Scrape Urls
    self.url = 'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB010400'
    self.thread = threading.Thread(target=run(self))
    self.thread.start()


def handle_facility(self):
    # Scrape Urls
    self.url = 'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030800'
    self.thread = threading.Thread(target=self.run)
    self.thread.start()


def handle_stock(self):
    # Scrape Urls
    self.url = 'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030900'
    self.thread = threading.Thread(target=self.run)
    self.thread.start()


def handle_auction(self):
    # Scrape Urls
    self.url = 'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB050500'
    self.thread = threading.Thread(target=self.run)
    self.thread.start()


def handle_all(self):
    urls = [
        "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB010400",
        "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030800",
        "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030900",
        "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB050500"
    ]

    while self.flag:
        # execute extraction in a loop
        for url in urls:
            # start scraping
            self.check_thread()
            self.url = url
            self.run()

        self.after(1200000, self.handle_all())

    raise Exception("Scheduler stopped!")


def run(self):
    s = Service("C:\Program Files (x86)\chromedriver.exe")
    self.chrome_options = Options()

    downloadFilepath = "C:\\Users\\User\\Documents\\GitHub\\ETL\\BPAM-ETL\\Download"
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
                # get the links again after getting back to the initial page in the loop
                links = self.browser.find_elements(By.CSS_SELECTOR, "#BrowseTable td:nth-child(2) a")
                th = self.browser.find_elements(By.CSS_SELECTOR, "#BrowseTable th + th")
                tr = self.browser.find_elements(By.CSS_SELECTOR, "#BrowseTable tr + tr")
                td = tr[index].find_elements(By.CSS_SELECTOR, "td + td")

                # scroll to the n-th link, it may be out of the initially visible area
                actions.move_to_element(links[index]).perform()
                self.code = links[index].find_element(By.CSS_SELECTOR, "u").text

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
                    sql1 = "SELECT * FROM " + title + " WHERE " + th[0].text.replace(" ", "_").lower() + " LIKE '" + td[
                        0].text + "'"
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

                links[index].click()

                if title == 'more_auction_calendar':
                    try:
                        WebDriverWait(self.browser, 3).until(
                            EC.alert_is_present())  # this will wait 5 seconds for alert to appear
                        alert = self.browser.switch_to.alert  # or self.driver.switch_to_alert() depends on your selenium version
                        alert.accept()
                    except TimeoutException:
                        pass

                else:
                    if title == 'all_announcements':
                        announcement.run(self)
                    if title == 'facility_information':
                        facility.run(self)
                    if title == 'stock_information':
                        stock.run(self)

                    # self.insert_filepath()
                    # back to main page
                    self.browser.execute_script("window.history.go(-1)")

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
                break

        except TimeoutException:
            self.text.insert(2.0, 'Scraping stopped as there is no more pages found!\n')
            # if the driver could not find next clickable, it will end the loop
            break

    self.browser.quit()
