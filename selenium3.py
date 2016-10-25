import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcos_site.settings')


from django.core.mail import send_mail, EmailMessage
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from pyvirtualdisplay import Display

display = Display(visible=0, size=(800,600))

display.start()



driver = webdriver.Firefox()
driver.get('http://www.pcsoweb.com/InmateBooking/')

date_input = driver.find_element_by_id("txtBookingDate")
search_button = driver.find_element_by_id("btnSearch")
page_size = Select(driver.find_element_by_id("drpPageSize"))


date_input.send_keys("10/24/2016")
page_size.select_by_value('100')

search_button.click()

print(driver.title)

print("Successfully ran!")

mail = EmailMessage("Hello", "testemail", 'bprecosheet@gmail.com', ['jeberry308@gmail.com'])
mail.send()