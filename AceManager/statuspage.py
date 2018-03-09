from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time

class StatusPage:

	status_Locater_path = ".//*[@id='StatusM1']/a/span"
	home_Locater_path = ".//*[@id='SM1_Status_HomeM1']/a/span"
	home_table_path = ".//*[@id='TD_256_Status_Home_']/table/tbody/tr" 
	wan_Locater_path = ".//*[@id='SM1_Status_WAN/CellularM1']/a/span"
	wan_table_path = ".//*[@id='TD_256_Status_WAN/Cellular_']/table/tbody/tr"
	about_Locater_path = ".//*[@id='SM1_Status_AboutM1']/a/span"
	about_table_path = ".//*[@id='TD_256_Status_About_']/table/tbody/tr"


	def status_Locater_action(self,browser):
		try:
			statusCssLocater =browser.find_element_by_xpath(self.status_Locater_path).click()
		except NoSuchElementException:
			print "Status tab not available on AirlinkPage "
			




	def home_Locater_action(self,browser):

			phoneNumber = ""
			homeCssLocater = browser.find_element_by_xpath(self.home_Locater_path).click()
			time.sleep(10)
			table_rows = browser.find_elements_by_xpath(self.home_table_path)
			for row in table_rows:
				try:					
					if row.find_element_by_xpath(".//td[2]").text == "Phone Number":
						phoneNumber =  row.find_element_by_xpath(".//td[3]").text
				except NoSuchElementException:
					pass
			return phoneNumber
		
	
	def wan_Locater_action(self,browser):
		
		esnEid = ""
		wanCssLocater = browser.find_element_by_xpath(self.wan_Locater_path).click()
		time.sleep(10)
		table_rows = browser.find_elements_by_xpath(self.wan_table_path)
		
		for row in table_rows:
			try:
				if row.find_element_by_xpath(".//td[2]").text == "ESN/EID/IMEI":
					esnEid =  row.find_element_by_xpath(".//td[3]").text
			except NoSuchElementException:	
				pass
		return esnEid

	def about_Locater_action(self,browser):

		valueList = []
		aboutCssLocater = browser.find_element_by_xpath(self.about_Locater_path).click()
		time.sleep(10)
		table_rows = browser.find_elements_by_xpath(self.about_table_path)
		
		for row in table_rows:
			try:
				if row.find_element_by_xpath(".//td[2]").text == "Device Model":
					valueList.append(row.find_element_by_xpath(".//td[3]").text)
				if row.find_element_by_xpath(".//td[2]").text == "Global ID":
					valueList.append(row.find_element_by_xpath(".//td[3]").text)
			except NoSuchElementException:	
				pass

		return valueList

