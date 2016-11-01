import openpyxl as xl
from openpyxl import Workbook
import time


def write_to_excel(detail_data):

    print("WRITING TO EXCEL")
    start = time.time()

    target_wb = Workbook()
    data_rows = ['Name', 'Docket', 'Arrest Date', 'Agency',
    			 'Address', 'City','State','Zipcode','Race',
    			 'Sex', 'Date of Birth', 'Place of Birth', 'Arrest Age',
    			 'Eye Color', 'Hair Color', 'Complexion', 'Height',
    			 'Weight', 'Markings', 'Cell Location', 'Account Balance', 'SPIN', 'Booking Type',
    			 'Alias', 'Charge Number', 'Agency Report Number', 'Offense',
    			 'Statute', 'Case Number', 'Bond Assessed', 'Bond Amount Due',
    			 'Charge Status', 'Arrest Type', 'OBTS',"-"]

    for key in detail_data.keys():
        target_ws = target_wb.create_sheet()
        target_ws.title = key
    	target_ws.cell(row = 1, column = 1).value = data_rows[0]

        for i in range(1,len(data_rows)):
            target_ws.cell(row = i + 1, column = 1 ).value = data_rows[i]
            if i == 1:
                try:
            	    target_ws.cell(row = i, column = 2 ).value = detail_data[key]['name']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 2:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['docket']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 3:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['arrest_date']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 4:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['agency']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 5:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['address']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 6:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['city']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 7:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['state']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 8:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['zipcode']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 9:
                try:
            	    target_ws.cell(row = i, column = 2 ).value = detail_data[key]['race']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 10:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['sex']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 11:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['dob']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 12:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['pob']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 13:
                try:
                	target_ws.cell(row = i , column = 2 ).value = detail_data[key]['arrest_age']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 14:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['eyes']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 15:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['hair']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 16:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['complexion']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 17:
                try:
            	    target_ws.cell(row = i, column = 2 ).value = detail_data[key]['height']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 18:
                try:
            	    target_ws.cell(row = i, column = 2 ).value = detail_data[key]['weight']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 19:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['markings']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 20:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['cell_location']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 21:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['account_balance']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 22:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['spin']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 23:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['booking_type']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 24:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['alias']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 25:
                try:
                    target_ws.cell(row = i, column = 2 ).value = detail_data[key]['charge_number']
                except KeyError:
                    target_ws.cell(row = i, column = 2 ).value = "1"
            elif i == 26:
                try:
                    target_ws.cell(row = i, column = 2 ).value = detail_data[key]['agency_report_number']
                except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 27:
                try:
                    target_ws.cell(row = i, column = 2 ).value = detail_data[key]['offense']
                except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 28:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['statute']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 29:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['case_number']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 30:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['bond_assessed']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 31:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['bond_amount_due']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 32:
                try:
                	target_ws.cell(row = i, column = 2 ).value = detail_data[key]['charge_status']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 33:
                try:
                    target_ws.cell(row = i, column = 2 ).value = detail_data[key]['arrest_type']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"
            elif i == 34:
                try:
                    target_ws.cell(row = i, column = 2 ).value = detail_data[key]['obts']
            	except:
            	    target_ws.cell(row = i, column = 2 ).value = "-"

    stop = time.time()
    length = int(stop-start)
    print("Writing portion of writeXL took  ", length)

    workbook_name = "Booking Statement Report.xlsx"
    target_wb.save("/home/lawscraper/reports/"+workbook_name)