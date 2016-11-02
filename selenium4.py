import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcos_site.settings')
from django.core.mail import send_mail, EmailMessage

import getIDs
import parseTargetID
import excelWriter

from parseTargetID import parseTarget
from getIDs import runParser
from excelWriter import write_to_excel

def email_attachment():
    mail = EmailMessage("New Booking Report Statement", "testemail", 'bprecosheet@gmail.com', ['jeberry308@gmail.com'])
    mail.attach_file("/home/lawscraper/reports/Booking Statement Report.xlsx")
    mail.send()
    print("sent mail!")

def error_handler():
	mail = EmailMessage("PCSO SCRAPE ERROR", "There was an error check the program! Try again", 'bprecosheet@gmail.com', ['jeberry308@gmail.com'])
	mail.send()
	print("Sent error Mail!")


def main():
    html_pages = getIDs.runParser()
    arrest_data = parseTargetID.parseTarget(html_pages)
    excelWriter.write_to_excel(arrest_data)
    email_attachment()

main()


