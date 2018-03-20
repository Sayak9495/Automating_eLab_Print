import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select 


def automate_java():
	browser = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div").click()
	for level in range(1,2):
		for session in range(0,2):
			java_url = 'http://care2.srmuniv.ac.in/rmpcsejavaada/login/student/code/java/java.code.php?id='+str(level)+'&value='+str(session)
			driver.get(java_url)
			time.sleep(0.5)
			java(session)

def java(session):
	driver.find_element_by_xpath("//*[@id='evaluateButton']").click()
	time.sleep(3)
	result = (driver.find_element_by_xpath("//*[@id='resultMsg']/p")).text

	if (result == "100%"):
		driver.find_element_by_xpath("//*[@id='printMsg']").click()
		print "DONE",session
	else:
		print "Code Written but not executed properly question number - ",session

	

def automate_ada():
	driver.get('http://care2.srmuniv.ac.in/rmpcsejavaada/login/student/home.php')
	browser = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div').click()

	for level in range(1,2):
		for session in range(0,2):
			ada_url = 'http://care2.srmuniv.ac.in/rmpcsejavaada/login/student/code/daa/daa.code.php?id='+str(level)+'&value='+str(session)
			driver.get(ada_url)
			time.sleep(0.5)
			ada(session)


def ada(session):
	driver.find_element_by_xpath("//*[@id='evaluateButton']").click()
	time.sleep(3)

	try:
		result = (driver.find_element_by_xpath("//*[@id='resultMsg']/p")).text
	except:
		try:
			script = ''' document.getElementById("selectInput").value ="cpp" '''
			driver.execute_script(script)
			driver.find_element_by_xpath("//*[@id='evaluateButton']").click()
			time.sleep(3)
			result_ada = (driver.find_element_by_xpath("//*[@id='resultMsg']/p")).text
		except:
			result_ada="0%"
		

	if (result_ada == "100%"):
		print "DONE",que_txt
		driver.find_element_by_xpath("//*[@id='printMsg']").click()
	else:
		print "Code Written but not executed properly question number - ",session



#uname=''
#pwd=''
print "Enter Username"
uname=raw_input()
print "Enter Password"
pwd=raw_input()


print "For ",uname,"and",pwd
path = '/home/sayak/Desktop/Automation/chromedriver'
driver = webdriver.Chrome(path)


driver.get("http://care2.srmuniv.ac.in/rmpcsejavaada/")
uname_field = driver.find_element_by_id("username")
uname_field.send_keys(uname)

pwd_field = driver.find_element_by_id("password")
pwd_field.send_keys(pwd)


driver.find_element_by_id("button").click()
time.sleep(1)

automate_java()
automate_ada()



driver.close()
print "*******DONE********\n"