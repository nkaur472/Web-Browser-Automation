from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class Authentication:

	password_Locater_path = ".//*[@id='password']"
	login_error_Locater_path = ".//*[@id='Lst']"

	def __init__(self,url,password):
		self.url = "http://"+url+":9191" 
		self.password = password


	def login(self,browser):
		try:
			browser.get(self.url)
			password_Locater = browser.find_element_by_xpath(self.password_Locater_path) #password form field
			login_Locater = browser.find_element_by_class_name("button_submit_padleft")
			password_Locater.send_keys(self.password)
			login_Locater.click()

		except TimeoutException:
			print ("No response "+self.url)
		except NoSuchElementException:
			print ("No such Element exist "+self.url) 	
		except Exception as e:
			print (e)

		else:
			try:
				if browser.find_element_by_xpath(self.login_error_Locater_path):
					raise Exception	
			except NoSuchElementException:
				pass
			except Exception:
				print ("Password is incorrect "+self.url)
				
			

			
