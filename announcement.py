from selenium.webdriver.common.by import By
import time
import json
import os


def run(self):
    code = self.code
    timestr = time.strftime("%Y-%m-%d %H%M%S")
    path = 'Announcement/' + code
    isExist = os.path.exists(path)
    if not isExist:
        os.mkdir(path)
    f = open(path + '/' + timestr + ".json", "a")
    f.write("Announcement: " + code + "\n")

    # scrape the data on the new page and get back with the following command
    rows = self.browser.find_elements(By.XPATH,
                                      "/html/body/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[2]/td/fieldset/table/tbody/tr")

    dicts = {
        'subject': self.browser.find_element(By.XPATH, '//*[@id="SpanPrint"]/table/tbody/tr[2]/td/fieldset/legend').text
    }

    for row in rows:
        key = row.find_element(By.XPATH, "td[1]").text.replace(":", "")
        value = row.find_element(By.XPATH, "td[2]").text
        dicts[key] = value

    dicts['content'] = self.browser.find_element(By.XPATH, '//*[@id="txtContent"]').text

    json_object = json.dumps(dicts, indent=1)
    f.write(json_object)
