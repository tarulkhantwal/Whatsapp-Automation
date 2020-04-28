from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'F:/chromedriver_win32/chromedriver.exe')
driver.maximize_window() 
driver.implicitly_wait(5) 
driver.get('http://web.whatsapp.com')

a=[]
name=[]
num=int(input("Enter the number of people or groups you want to send messages to"))
#name = input('Enter the names of user or group : ')
for i in range(0,num):
	name.append(input())
wait = WebDriverWait(driver, 1000)
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

#Scan the code before proceeding further 
input('Enter anything after scanning QR code')

 
for i in range(num):
	user=driver.find_element_by_class_name('_2S1VP').send_keys(name[i])
		
	driver.find_element_by_css_selector("[title^='"+name[i]+"']").click()
	
	msg_box = driver.find_element_by_class_name('_1Plpp')

	
	for i in range(count):
		msg_box.send_keys(msg)
		driver.find_element_by_class_name('_35EW6').click()
