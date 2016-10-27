import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcos_site.settings')

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage

from datetime import date
import re
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl import Workbook

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display

def getIDs():
    search_ids = []
    day_today = date.today()
    day_today = str(day_today)

    year = str(day_today[0:4])
    mo = str(day_today[5:7])
    day = str(day_today[8:11])

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

    #include_charge.click()
    search_button.click()

    response = driver.page_source
    soup = BeautifulSoup(response)

    #Searches for regular expression matching end of id attached
    #to inmate numbers

    inmate_numbers = soup.findAll("span", {"id" : re.compile('lblJMSNumber.*')})
    for num in inmate_numbers:
    	search_ids.append(num.text)

    #print("Finished running! Here's the inmate numbers")

    driver.quit()
    display.stop()

    return search_ids



def get_id_detail(test_id):

    display = Display(visible=0, size=(800,600))
    display.start()
    driver = webdriver.Firefox()

	#Appends inmate number to url to retrieve detailed info
	#on inmate, this is the target page to scrape

	#test_id = search_ids[0]	#Using first element as test id, will need to create loop
    test_id = test_id
    base_url = 'http://www.pcsoweb.com/inmatebooking/SubjectResults.aspx?id='
    target_url = base_url + test_id

    #print("About to visit  ", target_url)
    driver.get(target_url)
    #print("at this page" , driver.title)
    response = driver.page_source

    driver.quit()
    display.stop()

    return response

def parseTarget():

    master_data = {}
    search_ids = getIDs()

    for id_number in search_ids:

        detail_date = {}
    	results = []
    	charge_rows = []
    	charge_data = []

        target_html = get_id_detail(id_number)
    	soup = BeautifulSoup(target_html)

    	name = soup.find("span", {"id" : 'lblName1'}).text
    	print("oFFENDER IS : ", name)

    	docket = soup.find("span", {"id" : 'lblDocket1'}).text
    	arrest_date = soup.find("span", {"id" : 'lblArrestDate1'}).text
    	agency = soup.find("span", {"id" : 'lblAgency'}).text
    	address = soup.find("span", {"id" : 'lblAddress'}).text
    	city = soup.find("span", {"id" : 'lblCity'}).text
    	state = soup.find("span", {"id" : 'lblState'}).text
    	zipcode = soup.find("span", {"id" : 'lblZipCode'}).text
    	race = soup.find("span", {"id" : 'lblRace1'}).text
    	sex = soup.find("span", {"id" : 'lblSex1'}).text
    	dob = soup.find("span", {"id" : 'lblDOB1'}).text
    	pob = soup.find("span", {"id" : 'lblPOB'}).text
    	arrest_age = soup.find("span", {"id" : 'lblArrestAge'}).text
    	eyes = soup.find("span", {"id" : 'lblEyes'}).text
    	hair = soup.find("span", {"id" : 'lblHair'}).text
    	complexion = soup.find("span", {"id" : 'lblComplexion'}).text
    	height = soup.find("span", {"id" : 'lblHeight'}).text
    	weight = soup.find("span", {"id" : 'lblWeight'}).text
    	cell_location = soup.find("span", {"id" : 'CellLocation'}).text
    	account_balance = soup.find("span", {"id" : 'lblAccountBalance'}).text
    	spin = soup.find("span", {"id" : 'lblSPIN'}).text
    	booking_type = soup.find("span", {"id" : 'lblBookingType'}).text
    	alias = soup.find("span", {"id" : 'lblAKA'}).text


    	#Charge table is separate from other booking data

    	charge_table = soup.find("table", id='tblCharges')
    	rows = charge_table.findAll('td')
    	for row in rows:
    		charge_data.append(row.text)

    	#Iterates over every other because of headers
    	for i in range(1, len(charge_data),2):
    		if i == 1:
    			detail_date['charge_number'] = charge_data[i]
    			print("Grabbing charge number ", detail_date['charge_number'])
    		elif i == 3:
    			detail_date['agency_report_number'] = charge_data[i]
    		elif i == 5:
    			detail_date['offense'] = charge_data[i]
    		elif i == 7:
    			detail_date['statute'] = charge_data[i]
    		elif i == 9:
    			detail_date['case_number'] = charge_data[i]
    		elif i == 11:
    			detail_date['bond_assessed'] = charge_data[i]
    		elif i == 13:
    			detail_date['bond_amount_due'] = charge_data[i]
    		elif i == 15:
    			detail_date['charge_status'] = charge_data[i]
    		elif i == 17:
    			detail_date['arrest_type'] = charge_data[i]
    		elif i == 19:
    			detail_date['obts'] = charge_data[i]

    	detail_date['name'] = name
    	detail_date['docket'] = docket
    	detail_date['arrest_date'] = arrest_date
    	detail_date['agency'] = agency
    	detail_date['address'] = address
    	detail_date['city'] = city
    	detail_date['state'] = state
    	detail_date['zipcode'] = zipcode
    	detail_date['race'] = race
    	detail_date['sex'] = sex
    	detail_date['dob'] = dob
    	detail_date['pob'] = pob
    	detail_date['arrest_age'] = arrest_age
    	detail_date['eyes'] = eyes
    	detail_date['hair'] = hair
    	detail_date['complexion'] = complexion
    	detail_date['height'] = height
    	detail_date['weight'] = weight
    	detail_date['cell_location'] = cell_location
    	detail_date['account_balance'] = account_balance
    	detail_date['spin'] = spin
    	detail_date['booking_type'] = booking_type
    	detail_date['alias'] = alias


        master_data[docket] = detail_date


    for val in master_data.iteritems():
        print(val)
        print()
        print()

    return master_data

def write_to_excel():


### Data ROWS NEEDS TO BE DYNAMIC

    data_rows = ['Name', 'Docket', 'Arrest Date', 'Agency',
    			 'Address', 'City','State','Zipcode','Race',
    			 'Sex', 'Date of Birth', 'Place of Birth', 'Arrest Age',
    			 'Eye Color', 'Hair Color', 'Complexion', 'Height',
    			 'Weight', 'Cell Location', 'Account Balance', 'SPIN', 'Booking Type',
    			 'Alias', 'Charge Number', 'Agency Report Number', 'Offense',
    			 'Statute', 'Case Number', 'Bond Assessed', 'Bond Amount Due',
    			 'Charge Status', 'Arrest Type', 'OBTS']

    detail_data  = parseTarget()
    target_wb = Workbook()

    for key in detail_data.keys():
        target_ws = target_wb.create_sheet()
        target_ws.title = key
    	target_ws.cell(row = 1, column = 1).value = data_rows[0]

    	for i in range(1,len(data_rows)):
    		target_ws.cell(row = i + 1, column = 1 ).value = data_rows[i]

    		if i == 1:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['name']
    			print("Made it to master data here is name: ", detail_data[key]['name'])
    		elif i == 2:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['docket']
    		elif i == 3:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['arrest_date']
    		elif i == 4:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['agency']
    		elif i == 5:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['address']
    		elif i == 6:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['city']
    		elif i == 7:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['state']
    		elif i == 8:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['zipcode']
    		elif i == 9:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['race']
    		elif i == 10:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['sex']
    		elif i == 11:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['dob']
    		elif i == 12:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['pob']
    		elif i == 13:
    			target_ws.cell(row = i , column = 2 ).value = detail_data[key]['arrest_age']
    		elif i == 14:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['eyes']
    		elif i == 15:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['hair']
    		elif i == 16:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['complexion']
    		elif i == 17:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['height']
    		elif i == 18:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['weight']
    		elif i == 19:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['cell_location']
    		elif i == 20:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['account_balance']
    		elif i == 21:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['spin']
    		elif i == 22:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['booking_type']
    		elif i == 23:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['alias']
    		elif i == 24:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['charge_number']
    		elif i == 25:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['agency_report_number']
    		elif i == 26:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['offense']
    		elif i == 27:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['statute']
    		elif i == 28:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['case_number']
    		elif i == 29:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['bond_assessed']
    		elif i == 30:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['bond_amount_due']
    		elif i == 31:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['charge_status']
    		elif i == 32:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['arrest_type']
    		elif i == 33:
    			target_ws.cell(row = i, column = 2 ).value = detail_data[key]['obts']

    workbook_name = "Booking Statement Report.xlsx"
    target_wb.save("/home/lawscraper/reports/"+workbook_name)
    email_attachment()

def email_attachment():

    mail = EmailMessage("Hello", "testemail", 'bprecosheet@gmail.com', ['jeberry308@gmail.com'])
    mail.attach_file("/home/lawscraper/reports/Booking Statement Report.xlsx")
    mail.send()
    print("sent mail!")


write_to_excel()