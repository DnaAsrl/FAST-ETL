import tkinter as tk
from tkinter import ttk
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import mysql.connector
import schedule
import time

class ScrapeFast(Thread):
    def __init__(self, url):
        super().__init__()

        self.text = None
        self.url = url

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sdproject"
        )

        self.mycursor = self.mydb.cursor()

    def run(self):

        s = Service("C:\Program Files (x86)\chromedriver.exe")
        chrome_options = Options()
        chrome_options.headless = True  # selenium work in the background
        browser = webdriver.Chrome(service=s, options=chrome_options)
        browser.get(self.url)

        page = 1

        # Page title
        title = browser.find_element(By.CLASS_NAME, "styTitle").text

        while True:

            try:
                print(title)
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

                        sql1 = "SELECT * FROM " + title + " WHERE " + th[0].text.replace(" ", "_").lower() + " LIKE '" + td[0].text + "'"
                        # print(sql)
                        self.mycursor.execute(sql1)
                        result = self.mycursor.fetchone()
                        # print(result)

                        if not result:
                            # Insert into database
                            print("saving " + th[0].text + ": " + td[0].text)
                            columns = ', '.join("`" + str(x) + "`" for x in dicts.keys())
                            values = ', '.join("'" + str(x).replace("'", "") + "'" for x in dicts.values())
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
                if page < 3:
                    next_page.click()
                else:
                    self.text += "Complete \n"
                    break

            except TimeoutException:
                # if the driver could not find next clickable, it will end the loop
                self.mycursor.close()
                break

        browser.quit()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('WebpageDownload')
        self.geometry('680x430')
        self.resizable(0,0)

        self.create_header_frame()
        self.create_body_frame()
        self.create_footer_frame()

    def create_header_frame(self):

        self.header = ttk.Frame(self)

        # # configure the grid
        self.header.columnconfigure(4, weight=5)

        # # label
        # self.label = ttk.Label(self.header, text='URL')
        # self.label.grid(column=0, row=0, sticky=tk.W)

        # # entry
        # self.url_var = tk.StringVar()
        # self.url_entry = ttk.Entry(self.header, textvariable=self.url_var, width=80)
        #
        # self.url_entry.grid(column=1, row=0, sticky=tk.EW)

        # scrape button
        self.scrape_button = ttk.Button(self.header, text='Scape All')
        self.scrape_button['command'] = self.handle_scrape
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

    def handle_scrape(self):
        # list of URLs to be scrape
        FAST_urls = [
            "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB010400",
            "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030800",
            "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030900",
            "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB050500"
        ]

        # Scrape Urls
        for url in FAST_urls:
            scrape_thread = ScrapeFast(url)
            scrape_thread.start()
            self.monitor(scrape_thread)

    def handle_announcement(self):
        self.text.insert("1.0", "Scraping")
        # Scrape Urls
        scrape_thread = ScrapeFast('https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB010400')
        scrape_thread.start()

        self.monitor(scrape_thread)

    def handle_facility(self):
        # Scrape Urls
        scrape_thread = ScrapeFast('https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030800')
        scrape_thread.start()

        self.monitor(scrape_thread)

    def handle_stock(self):
        # Scrape Urls
        scrape_thread = ScrapeFast('https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030900')
        scrape_thread.start()

        self.monitor(scrape_thread)

    def handle_auction(self):
        # Scrape Urls
        scrape_thread = ScrapeFast('https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB0505000')
        scrape_thread.start()

        self.monitor(scrape_thread)

    def monitor(self, thread):
        if thread.is_alive():
            # check the thread every 100ms
            self.after(100, lambda: self.monitor(thread))
        else:
            # self.text.insert(1.0, thread.text)
            self.scrape_button['state'] = tk.NORMAL

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
        self.exit_button = ttk.Button(self.footer, text='Exit', command=self.destroy)

        self.exit_button.grid(column=0, row=0, sticky=tk.E)

        # attach the footer frame
        self.footer.grid(column=0, row=2, sticky=tk.NSEW, padx=10, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
