from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import xlrd

''' Multiple logins information can be stored in an excel sheet and logined one by one as required '''
#rb = xlrd.open_workbook(r'C:\Data\Navpreet\ReportingA\DriveBCHwyCams20171024-ALMS - Navpreet.xlsx')
#rs = rb.sheet_by_index(1)'''


traversed =[]

''' use of for loop if reading multiple login '''
ß
#for row in range(0,rs.nrows):
	#PASSWORD = rs.cell_value(row,2).strip()
	#url = s.cell_value(row,3).strip()

''' login information for single user '''

PASSWORD = "******" 
url = "*******" 


''' browser of your choice '''

#chromedriver = r'/Users/navpreetkaur/IBMReserach/python_crawler/chromedriver.exe'
#os.environ["webdriver.chrome.driver"] = chromedriver'''

browser = webdriver.Firefox() #replace with .Firefox(), or with the browser of your choice

if url not in traversed:

	url = "http://"+url.strip()+":9191"
	print url
	traversed.append(url)
	try:

		browser.get(url) #navigate to the page
		username = browser.find_element_by_xpath(".//*[@id='username']") #username form field
		password = browser.find_element_by_xpath(".//*[@id='password']") #password form field

		#username.send_keys("")
		password.send_keys(PASSWORD.strip())

		submitButton = browser.find_element_by_xpath(".//*[@id='login']/div[1]/div/div/form/fieldset/table/tbody/tr[2]/td[2]/input[2]") 
		submitButton.click()

	# store it to string variable
	except:
		print url 
		print "no response"
		print 
		pass
