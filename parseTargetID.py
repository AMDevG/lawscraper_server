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
        counter = 0
    	for row in rows:
    		charge_data.append(row.text)


        for item in charge_data:
            print(str(counter) + "  " +item)
            print()

            counter += 1


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


        if len(charge_data) > 19:
            number_of_charges = len(charge_data)/21
            print("The Offender has : " + str(number_of_charges) + " charges")

            charge_key_counter = 2

            if number_of_charges == 2:

                i = 22

                while i < 41:

                    if i == 22:
                        key = 'charge_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 24:
                        key  = 'agency_report_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 26:
                        key  = 'offense' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 28:
                        key  = 'statute' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 30:
                        key  = 'case_number' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 32:
                        key  = 'bond_assessed' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 34:
                        key  = 'bond_amount_due' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 36:
                        key  = 'charge_status' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 38:
                        key  = 'arrest_type' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 40:
                        key  = 'obts' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]

                        charge_key_counter+=1

                    i += 2



            elif number_of_charges == 3:

                i = 22

                while i < 62:

                    if i == 22:
                        key = 'charge_number' + str(charge_key_counter)
                        print("In second charge : Here is the number ", charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 24:
                        key  = 'agency_report_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 26:
                        key  = 'offense' + str(charge_key_counter)
                        print("here is the sec offense and key : ", key)
                        print(charge_data[i])
                        detail_date[key] = charge_data[i]
                    elif i == 28:
                        key  = 'statute' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 30:
                        key  = 'case_number' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 32:
                        key  = 'bond_assessed' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 34:
                        key  = 'bond_amount_due' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 36:
                        key  = 'charge_status' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 38:
                        key  = 'arrest_type' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 40:
                        key  = 'obts' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]

                        charge_key_counter+=1

                        print("Just increased key counter ", charge_key_counter)

                        i = 41

                        print ("I is at ", i)

        
                    elif i == 43:
                        print("i is at ", i)

                        key = 'charge_number' + str(charge_key_counter)
                        print ("Third charge num should be Charge_number3")
                        print ("It is ", key)

                        detail_date[key] = charge_data[i]
                    elif i == 45:
                        key  = 'agency_report_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 47:
                        key  = 'offense' + str(charge_key_counter)
                        print("here is 3rd offense ", charge_data[i])
                        detail_date[key] = charge_data[i]
                    elif i == 49:
                        key  = 'statute' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 51:
                        key  = 'case_number' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 53:
                        key  = 'bond_assessed' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 55:
                        key  = 'bond_amount_due' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 57:
                        key  = 'charge_status' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 59:
                        key  = 'arrest_type' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 61:
                        detail_date['obts'] = charge_data[i]

                        charge_key_counter += 1

                    i += 2
                    print i 

            elif number_of_charges == 4:

                i = 22

                while i < 83:

                    if i == 22:
                        key = 'charge_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 24:
                        key  = 'agency_report_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 26:
                        key  = 'offense' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 28:
                        key  = 'statute' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 30:
                        key  = 'case_number' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 32:
                        key  = 'bond_assessed' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 34:
                        key  = 'bond_amount_due' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 36:
                        key  = 'charge_status' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 38:
                        key  = 'arrest_type' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 40:
                        key  = 'obts' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]

                        charge_key_counter+=1

                        i = 41

                    elif i == 43:
                        key = 'charge_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 45:
                        key  = 'agency_report_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 47:
                        key  = 'offense' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 49:
                        key  = 'statute' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 51:
                        key  = 'case_number' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 53:
                        key  = 'bond_assessed' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 55:
                        key  = 'bond_amount_due' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 57:
                        key  = 'charge_status' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 59:
                        key  = 'arrest_type' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 61:
                        detail_date['obts'] = charge_data[i]

                        charge_key_counter += 1

                        i = 62

                    if i == 64:
                        key = 'charge_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 66:
                        key  = 'agency_report_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 68:
                        key  = 'offense' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 70:
                        key  = 'statute' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 72:
                        key  = 'case_number' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 74:
                        key  = 'bond_assessed' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 76:
                        key  = 'bond_amount_due' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 78:
                        key  = 'charge_status' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 80:
                        key  = 'arrest_type' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 82:
                        key  = 'obts' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]

                        charge_key_counter+= 1

                    i += 2

            elif number_of_charges == 5:

                i = 22
    
                while i < 104:

                    if i == 22:
                        key = 'charge_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 24:
                        key  = 'agency_report_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 26:
                        key  = 'offense' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 28:
                        key  = 'statute' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 30:
                        key  = 'case_number' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 32:
                        key  = 'bond_assessed' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 34:
                        key  = 'bond_amount_due' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 36:
                        key  = 'charge_status' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 38:
                        key  = 'arrest_type' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 40:
                        key  = 'obts' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]

                        charge_key_counter+=1

                        i = 41

                    elif i == 43:
                        key = 'charge_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 45:
                        key  = 'agency_report_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 47:
                        key  = 'offense' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 49:
                        key  = 'statute' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 51:
                        key  = 'case_number' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 53:
                        key  = 'bond_assessed' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 55:
                        key  = 'bond_amount_due' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 57:
                        key  = 'charge_status' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 59:
                        key  = 'arrest_type' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 61:
                        detail_date['obts'] = charge_data[i]

                        charge_key_counter += 1

                        i = 62


                    if i == 64:
                        key = 'charge_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 66:
                        key  = 'agency_report_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 68:
                        key  = 'offense' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 70:
                        key  = 'statute' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 72:
                        key  = 'case_number' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 74:
                        key  = 'bond_assessed' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 76:
                        key  = 'bond_amount_due' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 78:
                        key  = 'charge_status' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 80:
                        key  = 'arrest_type' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 82:
                        key  = 'obts' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]

                        charge_key_counter+= 1

                        i = 83


                    if i == 85:
                        key = 'charge_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 87:
                        key  = 'agency_report_number' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 89:
                        key  = 'offense' + str(charge_key_counter)
                        detail_date[key] = charge_data[i]
                    elif i == 91:
                        key  = 'statute' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 93:
                        key  = 'case_number' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]

                    elif i == 95:
                        key  = 'bond_assessed' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 97:
                        key  = 'bond_amount_due' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 99:
                        key  = 'charge_status' + str(charge_key_counter)
                        
                        detail_date[key] = charge_data[i]
                    elif i == 101:
                        key  = 'arrest_type' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]
                    elif i == 103:
                        key  = 'obts' + str(charge_key_counter)
                      
                        detail_date[key] = charge_data[i]

                    i +=2

        master_data[docket] = detail_date

    stop = time.time()
    length = int(stop - start)
    print("It took this long to process IDs in parsetarget : ", length)

    return master_data

