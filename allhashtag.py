# entre the keyword and get the related hashtags
# and return source page of the result

import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd


def all_hashtag(driver,tagword):
    driver.get("http://www.all-hashtag.com/hashtag-generator.php")
    print("all-hashtag")
#enter tegs
    while True:
        try:
            elem=driver.find_element_by_xpath("//input[@id='keyword']")
            elem.send_keys(tagword)
            break
        except:
            print("try to entre tag")
            continue
#click top radio button
    radio=driver.find_element_by_xpath("//label[contains(text(),'top')]")
    radio.click()
#click generate button
    gene_button=driver.find_element_by_xpath("//button[@class='btn-gen']")
    gene_button.click()
#time.sleep(10)
    page=driver.find_element_by_tag_name("html")
    while True:
        try:
            page.send_keys(Keys.ARROW_DOWN)
            page.send_keys(Keys.ARROW_DOWN)
            print ("scroll Down")
            driver.find_element_by_xpath("//div[@id='copy-hashtags']")
            print("</html>")
            break
        except:
            time.sleep(0.5)
            continue    
    print("page loaded")
    source_page = driver.page_source

    soup=BeautifulSoup(source_page,"html.parser")
    copy=soup.find(id="copy-hashtags")
    data = copy.get_text()              #type str
    splited = data.split()
    df_tag = pd.DataFrame({"tags":splited})
    return df_tag
    