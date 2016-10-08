import dryscrape
import re
from bs4 import BeautifulSoup
import sys


def getIDs():
    search_ids = []

    if 'linux' in sys.platform:
        # start xvfb in case no X is running. Make sure xvfb 
        # is installed, otherwise this won't work!
        dryscrape.start_xvfb()


    sess = dryscrape.Session()
    sess.visit('http://www.pcsoweb.com/inmatebooking/')


    button = sess.at_css('#btnSearch')
    check = sess.at_css('#chkIncludeCharge')
    return_size = sess.at_css('#drpPageSize')

    dateInput = sess.at_xpath('//*[@id="txtBookingDate"]')
    dateInput.set('10/6/2016')

    return_size.set('100')

    check.click()

    button.click()

    response = sess.body()

    soup = BeautifulSoup(response)

    dates = soup.findAll("span", {"id" : re.compile('lblJMSNumber.*')})

    for d in dates:
        search_ids.append(d.text)

    get_id_detail(search_ids)

def get_id_detail(search_ids):

    sess = dryscrape.Session()

    test_id = search_ids[0]
    base_url = 'http://www.pcsoweb.com/inmatebooking/SubjectResults.aspx?id='
    target_url = base_url + test_id
    
    sess.visit(target_url)
    response = sess.body()

    print(response)
"""

IDS to Pull

lblName1
lblDocket1
lblArrestDate1
lblAgency
lblAddress
lblCity
lblState
lblZipCode
lblRace1
lblSex1
lblDOB1
lblPOB
lblArrestAge
lblEyes
lblHair
lblComplexion
lblHeight
lblWeight
lblCellLocation
lblAccountBalance
lblSPIN
lblBookingType
lblAKA

CHARGE INFO
table id=tblCharges

info is held in tds

class = tdBold
style=width:450px;
    
    """


    
