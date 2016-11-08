import os

from openpyxl import Workbook
from openpyxl.cell import get_column_letter
from openpyxl.styles import Alignment
import datetime

from django.core.mail import send_mail, EmailMessage
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcos_site.settings')

def write_to_excel(detail_data):

    target_wb = Workbook()
    data_rows = ['Name', 'Docket', 'Arrest Date', 'Agency',
    			 'Address', 'City','State','Zipcode','Race',
    			 'Sex', 'Date of Birth', 'Place of Birth', 'Arrest Age',
    			 'Eye Color', 'Hair Color', 'Complexion', 'Height',
    			 'Weight', 'Markings', 'Cell Location', 'Account Balance', 'SPIN', 'Booking Type',
    			 'Alias', 'Charge Number', 'Agency Report Number', 'Offense',
    			 'Statute', 'Case Number', 'Bond Assessed', 'Bond Amount Due',
    			 'Charge Status', 'Arrest Type', 'OBTS',  'Charge Number 2', 'Agency Report Number 2', 'Offense 2',
                 'Statute 2', 'Case Number 2', 'Bond Assessed 2', 'Bond Amount Due 2',
                 'Charge Status 2', 'Arrest Type 2', 'OBTS 2', 'Charge Number 3', 'Agency Report Number 3', 'Offense 3',
                 'Statute 3', 'Case Number 3', 'Bond Assessed 3', 'Bond Amount Due 3',
                 'Charge Status 3', 'Arrest Type 3', 'OBTS 3',  'Charge Number 4', 'Agency Report Number 4', 'Offense 4',
                 'Statute 4', 'Case Number 4', 'Bond Assessed 4', 'Bond Amount Due 4',
                 'Charge Status 4', 'Arrest Type 4', 'OBTS 4',  'Charge Number 5', 'Agency Report Number 5', 'Offense 5',
                 'Statute 5', 'Case Number 5', 'Bond Assessed 5', 'Bond Amount Due 5',
                 'Charge Status 5', 'Arrest Type 5', 'OBTS 5',  "-"]

    target_ws = target_wb.create_sheet()
    target_ws.title = "Arrest Data"

    for i in range(1, 101):
        col_letter = get_column_letter(i)
        target_ws.column_dimensions[col_letter].width = 30

    for col in target_ws.columns:
        for cell in col:
            alignment_obj = cell.alignment.copy(horizontal='center', vertical='center')
            cell.alignment = alignment_obj

    counter = 1
    for item in data_rows:
        target_ws.cell(row = counter, column = 1).value = item
        counter+=1

    col_counter = 1
    for key in detail_data.keys():
        col_counter +=1
        for i in range(1,len(data_rows)):
            if i == 1:
                try:
            	    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['name']
                except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 2:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['docket']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 3:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['arrest_date']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 4:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['agency']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 5:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['address']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 6:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['city']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 7:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['state']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 8:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['zipcode']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 9:
                try:
            	    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['race']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 10:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['sex']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 11:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['dob']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 12:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['pob']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 13:
                try:
                	target_ws.cell(row = i , column = col_counter ).value = detail_data[key]['arrest_age']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 14:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['eyes']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 15:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['hair']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 16:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['complexion']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 17:
                try:
            	    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['height']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 18:
                try:
            	    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['weight']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 19:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['markings']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 20:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['cell_location']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 21:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['account_balance']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 22:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['spin']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 23:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['booking_type']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 24:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['alias']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 25:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['charge_number']  ### BEGIN IF CHARGE DATA
                except KeyError:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 26:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['agency_report_number']
                except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 27:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['offense']
                except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 28:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['statute']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 29:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['case_number']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 30:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['bond_assessed']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 31:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['bond_amount_due']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 32:
                try:
                	target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['charge_status']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 33:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['arrest_type']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 34:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['obts']
            	except:
            	    target_ws.cell(row = i, column = col_counter ).value = "-"

        ##### CHARGE 2 ######
            elif i == 35:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['charge_number2']  ### BEGIN IF CHARGE DATA
                except KeyError:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 36:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['agency_report_number2']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 37:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['offense2']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 38:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['statute2']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 39:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['case_number2']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 40:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['bond_assessed2']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 41:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['bond_amount_due2']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 42:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['charge_status2']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 43:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['arrest_type2']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 44:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['obts2']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"

        ### CHARGE 3 #####
            elif i == 45:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['charge_number3']  ### BEGIN IF CHARGE DATA
                except KeyError:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 46:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['agency_report_number3']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 47:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['offense3']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 48:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['statute3']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 49:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['case_number3']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 50:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['bond_assessed3']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 51:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['bond_amount_due3']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 52:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['charge_status3']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 53:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['arrest_type3']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 54:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['obts3']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"

            ##### CHARGE 4 ####
            elif i == 55:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['charge_number4']  ### BEGIN IF CHARGE DATA
                except KeyError:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 56:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['agency_report_number4']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 57:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['offense4']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 58:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['statute4']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 59:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['case_number4']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 60:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['bond_assessed4']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 61:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['bond_amount_due4']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 62:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['charge_status4']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 63:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['arrest_type4']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 64:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['obts4']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"

        ##### CHARGE 5 #####
            elif i == 65:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['charge_number5']  ### BEGIN IF CHARGE DATA
                except KeyError:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 66:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['agency_report_number5']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 67:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['offense5']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 68:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['statute5']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 69:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['case_number5']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 70:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['bond_assessed5']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 71:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['bond_amount_due5']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 72:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['charge_status5']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 73:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['arrest_type5']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"
            elif i == 74:
                try:
                    target_ws.cell(row = i, column = col_counter ).value = detail_data[key]['obts5']
                except:
                    target_ws.cell(row = i, column = col_counter ).value = "-"

    day_day = datetime.date.today()
    date_day = day_day - datetime.timedelta(hours=6)
    date_day = str(date_day)
    workbook_name = "Booking Statement Report" + date_day + ".xlsx"

    del_sheet = target_wb.get_sheet_by_name('Sheet')
    target_wb.remove_sheet(del_sheet)

    target_wb.save("/home/lawscraper/reports/"+workbook_name)

    #mail = EmailMessage("New Booking Report Statement", "", 'bprecosheet@gmail.com', ['jeberry308@gmail.com', 'js@dedicateddefense.com', 'ls@dedicateddefense.com'])

    mail = EmailMessage("New Booking Report Statement", "", 'bprecosheet@gmail.com', ['jeberry308@gmail.com'])
    mail.attach_file("/home/lawscraper/reports/"+workbook_name)
    mail.send()
    print("sent mail!")
