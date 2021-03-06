import datetime
import re
import time
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display

def textMe():
    accountSID = 'ACe9203e47e2250788094f00add6fd80e4'
    authToken = 'fa7a2fbee81d6244aa90faa50b001978'
    twilioCli = TwilioRestClient(accountSID, authToken)
    myTwilioNumber = '+12162825543'
    cell = '+12169734568'
    message = twilioCli.messages.create(body='There was an error starting web driver!', from_=myTwilioNumber, to=cell)


def getIDs():
    search_ids = []
    x = datetime.datetime.now()
    day_today = x - datetime.timedelta(hours=6)

    day_today = str(day_today)
    year = str(day_today[0:4])
    mo = str(day_today[5:7])
    day = str(day_today[8:10])

    day_today = mo+"/"+day+"/"+year

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

    time.sleep(1)

    print("Driver load success and is at ", driver.title)

    response = driver.page_source
    soup = BeautifulSoup(response)

    time.sleep(1)

    inmate_numbers = soup.findAll("span", {"id" : re.compile('lblJMSNumber.*')})
    for num in inmate_numbers:
    	search_ids.append(num.text)

    if len(search_ids) == 0:
        print("Error gathering data!")
        driver.save_screenshot('/home/lawscraper/screenshots/error.png')
        #selenium4.error_handler()

    driver.quit()
    display.stop()

    return search_ids

def get_id_detail():
    html_dict = {}
    test_ids = getIDs()

    try:
        display = Display(visible=0, size=(800,600))
        display.start()
        driver = webdriver.Firefox()
    except:
        print("Error Starting Driver on ID Gathering")
        driver.quit()
        display.stop()
        print("Calling Again!")
        textMe()
        get_id_detail()

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
    html_pages = get_id_detail()
    return html_pages

