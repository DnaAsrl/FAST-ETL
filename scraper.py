import os
import pandas as pd
import time
from sqlalchemy import create_engine
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def select(table, th, td):
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fastdb"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM " + table + " WHERE " + th + " LIKE '" + td + "'"
    # print(sql)

    mycursor.execute(sql)

    result = mycursor.fetchall()
    # print(result)

    if result:
        return False
    else:
        return True


def scrape(url):
    # Check whether the specified path exists or not
    isExist = os.path.exists("FAST")

    if not isExist:
        # Create a new directory because it does not exist
        os.mkdir("FAST")

    s = Service("C:\Program Files (x86)\chromedriver.exe")
    chrome_options = Options()
    chrome_options.headless = True  # selenium work in the background
    browser = webdriver.Chrome(service=s, options=chrome_options)
    browser.get(url)

    page = 1
    templist = []

    # Page title
    title = browser.find_element(By.CLASS_NAME, "styTitle").text
    print(title)

    # # Check whether the txt exists or not
    # if not os.path.exists("FAST/"+title+".txt"):
    #     f = open("FAST/"+title+".txt", "a")
    # else:
    #     # Create a new txt because it does not exist
    #     print("Rewriting file")
    #     f = open("FAST/"+title+".txt", "w")

    # # Sort by ascending
    # browser.find_element(By.CSS_SELECTOR,  "th:nth-child(2) font").click()

    # create sqlalchemy engine
    db = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="",
                               db="fastdb"))

    while True:

        try:
            print("Page ", page)
            # f.write("\nPage " + str(count) + "\n")

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

                    if select(title, th[0].text.replace(" ", "_").lower(), td[0].text):
                        # saving the dataframe to a csv
                        templist.append(dicts)
                        df = pd.DataFrame(templist)
                        df.to_csv("FAST/" + title + '.csv', index=False)

                        # Insert whole DataFrame into MySQL
                        print("saving " + th[0].text + ": " + td[0].text)
                        df.to_sql(title, con=db, if_exists='replace', chunksize=1000, index=False)

                        # # Save to txt
                        # f.write(str(Table_dict))
                        # f.write("\n")

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
                print("Complete")
                break

        except TimeoutException:
            # if the driver could not find next clickable, it will end the loop
            db.close()
            break

    # # saving the list to txt
    # f.write(str(templist))
    # f.close()

    # print("")
    browser.quit()


def start():

    while True:
        main()
        time.sleep(300)


def main():
    # list of URLs to be scrape
    FAST_urls = [
        "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB010400",
        "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030800",
        "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030900",
        "https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB050500"
    ]

    # Scrape Urls
    for url in FAST_urls:
        scrape(url)


if __name__ == '__main__':
    main()
