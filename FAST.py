import threading
import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import mysql.connector
from datetime import datetime


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('FAST Scraper')
        self.geometry('680x430')
        self.resizable(0, 0)

        self.create_header_frame()
        self.create_body_frame()
        self.create_footer_frame()
        self.flag = True
        self.url = None
        self.thread = None

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="fastdb"
        )

        self.mycursor = self.mydb.cursor(buffered=True)

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

    def check_thread(self):
        if self.thread.is_alive():
            self.scrape_button['state'] = 'disabled'
            self.announcement_button['state'] = 'disabled'
            self.facility_button['state'] = 'disabled'
            self.stock_button['state'] = 'disabled'
            self.auction_button['state'] = 'disabled'

        else :
            self.scrape_button['state'] = 'normal'
            self.announcement_button['state'] = 'normal'
            self.facility_button['state'] = 'normal'
            self.stock_button['state'] = 'normal'
            self.auction_button['state'] = 'normal'

        # check again after 100ms
        self.after(100, self.check_thread)

    def scheduler(self):
        self.flag = True
        self.thread_scrape()

    def thread_scrape(self):
        if self.flag is True:
            self.thread = threading.Thread(target=self.handle_all)
            self.thread.start()
            self.after(300000, self.thread_scrape)
        else:
            self.text.insert(1.0, "Scraping Stopped")

    def handle_all(self):
        # list of URLs to be scrape
        FAST_urls = [
            "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB010400",
            "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030800",
            "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030900",
            "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB050500"
        ]

        # Scrape Urls
        for url in FAST_urls:
            self.url = url
            self.run()

    def run(self):
        self.check_thread()
        s = Service("C:\Program Files (x86)\chromedriver.exe")
        chrome_options = Options()
        chrome_options.headless = True  # selenium work in the background
        browser = webdriver.Chrome(service=s, options=chrome_options)
        browser.get(self.url)

        page = 1

        # Page title
        title = browser.find_element(By.CLASS_NAME, "styTitle").text
        print(title)
        self.text.insert(1.0, title + "\n")

        while True:

            try:
                self.text.insert(2.0, "Page:" + str(page) + "\n")
                print("Page:", page)

                # wait for the driver to find table
                WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.ID, "BrowseTable"))
                )

                # scrape table
                table = browser.find_elements(By.CSS_SELECTOR, "#BrowseTable")

                for i in table:
                    th = i.find_elements(By.CSS_SELECTOR, "th + th")
                    tr = i.find_elements(By.CSS_SELECTOR, "tr + tr")
                    for j in tr:
                        td = j.find_elements(By.CSS_SELECTOR, "td + td")
                        dicts = {}

                        for k in range(len(th)):
                            dicts[th[k].text.replace(" ", "_").lower()] = td[k].text

                        title = title.replace(" ", "_").lower()

                        if title == 'more_auction_calendar':
                            issue_date = '-'
                            if td[4].text != '-':
                                datetime_str = td[4].text
                                issue_date = datetime.strptime(datetime_str, '%d/%m/%Y').strftime('%Y-%m-%d')
                            # check if already exist in database
                            sql1 = "SELECT * FROM " + title + " WHERE issues LIKE '" + td[0].text + "' AND issue_date LIKE '" + issue_date + "'"
                            # print(sql1)
                            self.mycursor.execute(sql1)
                            result = self.mycursor.fetchone()
                            # print(result)

                        else:
                            # check if already exist in database
                            sql1 = "SELECT * FROM " + title + " WHERE " + th[0].text.replace(" ", "_").lower() + " LIKE '" + td[0].text + "'"
                            # print(sql)
                            self.mycursor.execute(sql1)
                            result = self.mycursor.fetchone()
                            # print(result)

                        if not result:
                            # Insert into database
                            now = datetime.now()
                            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                            print(dt_string)
                            self.text.insert(3.0, dt_string + ": saving " + th[0].text + ": " + td[0].text + "\n")
                            print("saving " + th[0].text + ": " + td[0].text)

                            for x in dicts.keys():
                                if x == "maturity_date" or x == "issue_date":
                                    if dicts[x] != '-':
                                        datetime_str = dicts[x]
                                        dicts[x] = datetime.strptime(datetime_str, '%d/%m/%Y').strftime('%Y-%m-%d')
                                if x == "embargo_date":
                                    if dicts[x] != '-':
                                        datetime_str = dicts[x].strip(" APM")
                                        dicts[x] = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

                            columns = ', '.join("`" + str(x).replace("**_", "").replace("_(rm_million)", "") + "`" for x in dicts.keys()) + ",`created_at`"
                            values = ', '.join("'" + str(x).replace("'", "") + "'" for x in dicts.values()) + ",'" + dt_string + "'"
                            sql2 = "INSERT INTO %s ( %s ) VALUES ( %s );" % (title, columns, values)
                            # print(sql2)
                            self.mycursor.execute(sql2)
                            self.mydb.commit()
                            print(self.mycursor.rowcount, "record inserted.")

                # wait for driver to find next button
                next_page = WebDriverWait(browser, 10).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "[Next]"))
                )

                # as it will go the next page, the count will increase to indicates the next page
                page += 1
                # Max pages to scrape
                if page <= 2:
                    next_page.click()
                else:
                    self.text.insert(2.0, 'Scraping Completed!\n')
                    print("Complete")
                    break

            except TimeoutException:
                self.text.insert(2.0, 'Scraping Completed!\n')
                # if the driver could not find next clickable, it will end the loop
                break

        browser.quit()

    def handle_announcement(self):
        # Scrape Urls
        self.url = 'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB010400'
        self.thread = threading.Thread(target=self.run)
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
        self.footer.columnconfigure(0,weight=1)
        # exit button
        self.exit_button = ttk.Button(self.footer, text='Stop Scheduling', command=self.stop)

        self.exit_button.grid(column=0, row=0, sticky=tk.E)

        # attach the footer frame
        self.footer.grid(column=0, row=2, sticky=tk.NSEW, padx=10, pady=10)

    def stop(self):
        self.flag = False


if __name__ == "__main__":
    app = App()
    app.mainloop()
