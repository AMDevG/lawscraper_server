import sys
import os
import time

from bs4 import BeautifulSoup

def parseTarget(html_pages):

    master_data = {}
    print("Entering parse target")
    start = time.time()

    for key, val in html_pages.iteritems():

        detail_date = {}
    	results = []
    	charge_rows = []
    	charge_data = []

    	soup = BeautifulSoup(val)

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
    	markings = soup.find("span", {"id" : 'lblSMT'}).text
    	cell_location = soup.find("span", {"id" : 'CellLocation'}).text
    	account_balance = soup.find("span", {"id" : 'lblAccountBalance'}).text
    	spin = soup.find("span", {"id" : 'lblSPIN'}).text
    	booking_type = soup.find("span", {"id" : 'lblBookingType'}).text
    	alias = soup.find("span", {"id" : 'lblAKA'}).text

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
        detail_date['markings'] = markings
        detail_date['cell_location'] = cell_location
        detail_date['account_balance'] = account_balance
        detail_date['spin'] = spin
        detail_date['booking_type'] = booking_type
        detail_date['alias'] = alias


    	charge_table = soup.find("table", id='tblCharges')
    	rows = charge_table.findAll('td')

        #### CHECK LENGTH OF CHARGE DATA IF GREATER THAN 19 MULTIPLE CHARGES

    	for row in rows:
    		charge_data.append(row.text)

    	if len(charge_data) > 19:
    	    number_of_charges = len(charge_data)/21
    	    print("The Offender has : " + str(number_of_charges) + " charges")

    	for i in range(1, len(charge_data),2):
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
        master_data[docket] = detail_date

    stop = time.time()
    length = int(stop - start)
    print("It took this long to process IDs in parsetarget : ", length)
    return master_data

