from datetime import date
import re
import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display



def getIDs():
    start = time.time()
    search_ids = []

    day_today = date.today()
    day_today = str(day_today)
    year = str(day_today[0:4])
    mo = str(day_today[5:7])
    day = str(day_today[8:11])

    #day_today = mo+"/"+day+"/"+year
    day_today = "10/31/2016"

    display = Display(visible=0, size=(800,600))
    display.start()
    driver = webdriver.Firefox()

    driver.get('http://www.pcsoweb.com/InmateBooking/')
    date_input = driver.find_element_by_id("txtBookingDate")
    search_button = driver.find_element_by_id("btnSearch")
    page_size = Select(driver.find_element_by_id("drpPageSize"))

    date_input.send_keys(day_today)
    page_size.select_by_value('100')
    search_button.click()

    sort_selection = Select(driver.find_element_by_id("drpSortBy"))
    sort_selection.select_by_value('Docket')

    response = driver.page_source
    soup = BeautifulSoup(response)
    inmate_numbers = soup.findAll("span", {"id" : re.compile('lblJMSNumber.*')})

    for num in inmate_numbers:
    	search_ids.append(num.text)

    driver.quit()
    display.stop()

    stop = time.time()
    length = int(stop-start)

    print("Get IDs ran for seconds: ", length)
    return search_ids


def get_id_detail():
    html_dict = {}

    test_ids = getIDs()
    display = Display(visible=0, size=(800,600))
    display.start()
    driver = webdriver.Firefox()

    for ID in test_ids:
        base_url = 'http://www.pcsoweb.com/inmatebooking/SubjectResults.aspx?id='
        target_url = base_url + ID
        driver.get(target_url)
        response = driver.page_source
        html_dict[ID] = response

    driver.quit()
    display.stop()

    return html_dict


def runParser():
    start = time.time()
    print("RUNNING PARSER! GATHER ARREST DATA HTML!")
    html_pages = get_id_detail()

    stop = time.time()
    length = int(stop - start)

    print("DONE GATHERING TOOK SECONDS: ", length)
    return html_pages

