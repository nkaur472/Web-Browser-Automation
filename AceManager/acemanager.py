from selenium import webdriver
from authentication import Authentication
from statuspage import StatusPage
import xlrd
import xlwt
from xlutils.copy import copy

def main():
	rb = xlrd.open_workbook(r'C:\....\Modem_Master_List_Ver_13-NKV03.xls')
	rs = rb.sheet_by_index(0)
	wb = copy(rb)
	ws = wb.get_sheet(0)
	
	for row in range(161,rs.nrows):
		phoneNumber =""
		esnEid = ""
		valueList =""
		mitigated = rs.cell_value(row,34).strip()

		if mitigated == "Yes - IMB" or mitigated == "Yes-FIELD":

			url = rs.cell_value(row,28).strip()
			print url
			password = rs.cell_value(row,35).strip()
			
			
			if not password == "" and not url == "":
				try:
					
					browser = webdriver.Ie(r"C:\....\IEDriverServer_Win32_2.39.0\IEDriverServer.exe")
					
					auth = Authentication(url.strip(),password.strip())
					auth.login(browser)
					stspg = StatusPage()
					stspg.status_Locater_action(browser)
					phoneNumber = stspg.home_Locater_action(browser)
					esnEid = stspg.wan_Locater_action(browser)
					valueList = stspg.about_Locater_action(browser)
					ws.write(row,13,phoneNumber)
					ws.write(row,17,esnEid)
					ws.write(row,20,valueList[0])
					ws.write(row,33,valueList[1])

		
				except:
					pass
				finally:
					browser.close()

			else:
				print "Password/url fields are empty "+url	
				

		if mitigated == "No":
			url = rs.cell_value(row,28).strip()
			print url
			password = str(rs.cell_value(row,31))

			'''
			Some of the passwords are in number format and excel convert numbers into float format at backend.
			'''
			
			if password == "****.0":
				password = password.strip('.0')
			elif password == "*****.0":
				password = password.strip('.0')
			else:
				password = password.strip()

			if not password == "" and not url == "":

				try:
					browser = webdriver.Ie(r"C:\...\IEDriverServer_Win32_2.39.0\IEDriverServer.exe")

					auth = Authentication(url.strip(),password.strip())
					auth.login(browser)
					#if status:
					stspg = StatusPage()
					stspg.status_Locater_action(browser)
					phoneNumber = stspg.home_Locater_action(browser)
					esnEid = stspg.wan_Locater_action(browser)
					valueList = stspg.about_Locater_action(browser)
					ws.write(row,13,phoneNumber)
					ws.write(row,17,esnEid)
					ws.write(row,20,valueList[0])
					ws.write(row,33,valueList[1])

				except:
					pass
				finally:
					browser.close()
			else:
				print "Password/url fields are empty "+url	
					

		wb.save(r'C:\....\Modem_Master_List_Ver_13-NKV03.xls')				
	
if __name__ == "__main__":
	main()