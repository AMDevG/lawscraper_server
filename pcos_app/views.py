from django.shortcuts import render
from django.http import HttpResponse

import dryscrape
import re
from bs4 import BeautifulSoup
import sys

def home(request):

	ids = getIDs()

	return HttpResponse("success")


def getIDs():

	print("getids called")
	search_ids = []




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

	print("Search ids are:")

	for i in search_ids:
		print(i)


	get_id_detail(search_ids)

def get_id_detail(search_ids):

    sess = dryscrape.Session()

    print("stardted second sesh in detail")

    test_id = search_ids[0]
    base_url = 'http://www.pcsoweb.com/inmatebooking/SubjectResults.aspx?id='
    target_url = base_url + test_id
    
    sess.visit(target_url)
    response = sess.body()


    return search_ids