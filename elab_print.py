import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select 


def automate_java():
	browser = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div").click()
	for level in range(1,2):
		for session in range(0,100):
			java_url = 'http://care2.srmuniv.ac.in/rmpcsejavaada/login/student/code/java/java.code.php?id='+str(level)+'&value='+str(session)
			driver.get(java_url)
			time.sleep(2)
			java(session)

def java(session):
	driver.find_element_by_xpath("//*[@id='evaluateButton']").click()
	time.sleep(3)
	try:
		result = (driver.find_element_by_xpath("//*[@id='resultMsg']/p")).text
	except:
		result="0%"
	if (result == "100%"):
		driver.find_element_by_xpath("//*[@id='printMsg']").click()
		print "DONE",session
	else:
		print "Code Written but not executed properly question number - ",session

	

def automate_ada():
	driver.get('http://care2.srmuniv.ac.in/rmpcsejavaada/login/student/home.php')
	browser = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div').click()

	for level in range(1,2):
		for session in range(0,100):
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

def automate_c():
	browser = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div").click()
	for level in range(1,2):
		for session in range(0,100):
			c_url = 'http://care2.srmuniv.ac.in/rmpcsepddmathslab/login/student/code/c/c.code.php?id='+str(level)+'&value='+str(session)
			driver.get(c_url)
			time.sleep(2)
			c(session)

def c(session):
	driver.find_element_by_xpath("//*[@id='evaluateButton']").click()
	time.sleep(3)
	try:
		result = (driver.find_element_by_xpath("//*[@id='resultMsg']/p")).text
	except:
		result="0%"
	if (result == "100%"):
		driver.find_element_by_xpath("//*[@id='printMsg']").click()
		print "DONE",session
	else:
		print "Code Written but not executed properly question number - ",session


def automate_mathslab():
	browser = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div").click()
	for level in range(1,2):
		for session in range(0,100):
			mathslab_url = 'http://care2.srmuniv.ac.in/rmpcsepddmathslab/login/student/code/mathslab/mathslab.code.php?id='+str(level)+'&value='+str(session)
			driver.get(mathslab_url)
			time.sleep(2)
			mathslab(session)

def mathslab(session):
	driver.find_element_by_xpath("//*[@id='evaluateButton']").click()
	time.sleep(3)
	try:
		result = (driver.find_element_by_xpath("//*[@id='resultMsg']/p")).text
	except:
		result="0%"
	if (result == "100%"):
		driver.find_element_by_xpath("//*[@id='printMsg']").click()
		print "DONE",session
	else:
		print "Code Written but not executed properly question number - ",session



year=raw_input("enter year, 1 or 2\n")
uname=raw_input("Enter Username\n")
pwd=raw_input("Enter Password\n")
if year=="1":
	choice=raw_input("hit 1 for C or 2 for MathsLab\n")
elif year=="2":
	choice=raw_input("hit 1 for JAVA or 2 for ADA\n")

print "For ",uname,"and",pwd,"and",choice

############################################################
path = 'C:\Users\sayak\Desktop\Automation\chromedriver'
############################################################

driver = webdriver.Chrome(path)

if year=="1":
	driver.get("http://care2.srmuniv.ac.in/rmpcsepddmathslab/")
elif year=="2":
	driver.get("http://care2.srmuniv.ac.in/rmpcsejavaada/")

uname_field = driver.find_element_by_id("username")
uname_field.send_keys(uname)

pwd_field = driver.find_element_by_id("password")
pwd_field.send_keys(pwd)

time.sleep(4)
driver.find_element_by_xpath('//*[@id="button"]/b').click()
time.sleep(1)

if year=="1":
	if choice=='1':
		automate_c()
	elif choice=='2':
		automate_mathslab()
elif year=="2":
	if choice=='1':
		automate_java()
	elif choice=='2':
		automate_ada()



#driver.close()
print "*******DONE********\n"
