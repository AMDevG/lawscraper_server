from django.shortcuts import render
from django.http import HttpResponse

import dryscrape
import re
from bs4 import BeautifulSoup
import sys

def home(request):

	#ids = getIDs()
	parseTarget()

	return HttpResponse("Done")


def getIDs():
	#search_ids holds all inmate numbers and is returned 
	#at end of function

	search_ids = []

	sess = dryscrape.Session()
	sess.visit('http://www.pcsoweb.com/inmatebooking/')

	#Selects submit button, check include, and results per page
	#Include charge must be selected to avoid clicking error since
	#calendar dropdown covers button when selected

	dateInput = sess.at_xpath('//*[@id="txtBookingDate"]')
	dateInput.set('10/6/2016')

	check = sess.at_css('#chkIncludeCharge')
	button = sess.at_css('#btnSearch')

	return_size = sess.at_css('#drpPageSize')
	return_size.set('100')

	check.click()
	button.click()

	response = sess.body()
	soup = BeautifulSoup(response)

	#Searches for regular expression matching end of id attached
	#to inmate numbers

	dates = soup.findAll("span", {"id" : re.compile('lblJMSNumber.*')})
	for d in dates:
		search_ids.append(d.text)

	#Passes ids to pull up inmate detail page
	return search_ids

def get_id_detail():
	search_ids = getIDs()
	#Appends inmate number to url to retrieve detailed info
	#on inmate, this is the target page to scrape

	sess = dryscrape.Session()

	test_id = search_ids[0]	#Using first element as test id, will need to create loop

	base_url = 'http://www.pcsoweb.com/inmatebooking/SubjectResults.aspx?id='
	target_url = base_url + test_id

	sess.visit(target_url)
	response = sess.body()

	return response

def parseTarget():

	# detail_date is the main dictionary containing all data for report
	
	detail_date = {}
	results = []
	charge_rows = []
	charge_data = []

	target_html = get_id_detail()

	soup = BeautifulSoup(target_html)

	
	name = soup.find("span", {"id" : 'lblName1'}).text
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



	charge_table = soup.find("table", id='tblCharges')
	rows = charge_table.findAll('td')
	for row in rows:	
		charge_data.append(row.text)

	
	for i in range(1, len(charge_data),2):
		print("i is at", i)
		if i == 1:
			detail_date['charge_number'] = charge_data[i]
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
	



	for key, val in detail_date.items():
		print(key,val)





