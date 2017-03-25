# import time
# import webbrowser
# url = "https://www.google.com.tr/search?q={}".format("Raspberry Pi") 
# b = webbrowser.get('firefox')
# b.open(url)

# time.sleep(10)
#b.close(url)

# from selenium import webdriver
# from time import sleep

# driver = webdriver.Firefox()
# driver.get("http://google.co.uk")
# sleep(10)
# driver.close()


# import time
# import subprocess

# p = subprocess.Popen(["firefox", "http://www.google.com"])
# time.sleep(10) #delay of 10 seconds
# p.kill()
# import subprocess as sp
# import time
# def browse(url, how_long):
#     child = sp.Popen("firefox %s" % url, shell=True)
#     #child = sp.Popen(['firefox', '-p',  'foo', '-no-remote', url])
#     time.sleep(how_long)
#     child.terminate()
# browse("http://www.python.org", 3)

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# from selenium import webdriver

# driver = webdriver.Firefox()
# search="Raspberry Pi"
# driver.get('https://www.google.com.tr/search?q='+search)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.save_screenshot('screenshot.png')
# driver.quit()

#run this before 
#export DISPLAY=:0
#-*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
import sys
import BeautifulSoup
import wikipedia
# import csv


# with open('test.csv', 'rb') as f:
#     reader = csv.reader(f)
#     your_list = map(tuple, reader)

# print (your_list)
# # [('This is the first line', ' Line1'),
# #  ('This is the second line', ' Line2'),
# #  ('This is the third line', ' Line3')]
# time.sleep(10)

# fp = webdriver.FirefoxProfile()

# fp.set_preference("browser.download.folderList",2)
# fp.set_preference("browser.download.manager.showWhenStarting",False)
# fp.set_preference("browser.download.dir", os.getcwd())
# fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

#browser = webdriver.Firefox(firefox_profile=fp)
import io
i=0
lines = []
with open('test.txt', 'r') as f:
	for line in f.readlines():
		lines.append(line)

for text in lines:
	search=text
	fp = webdriver.FirefoxProfile()
	fp.set_preference("browser.download.folderList",2)
	fp.set_preference("browser.download.manager.showWhenStarting",False)
	fp.set_preference("browser.download.dir", os.getcwd())
	fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
	browser = webdriver.Firefox(firefox_profile=fp)
	try:
		browser.get('https://www.google.com.tr/search?q='+search+' wiki')
	except OSError as err:
	    print("OS error: {0}".format(err))
	except ValueError:
	    print("Could not convert data to an integer.")
	except:
	    print("Unexpected error:", sys.exc_info()[0])
	    raise
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(1)
	browser.execute_script("window.scrollTo(0, -100);")
	time.sleep(1)
	search2 = 'Wikipedia'
	browser.find_element_by_partial_link_text(search2).click()
	time.sleep(1)
	browser.save_screenshot('screenshot_'+ search+'_'+str(i)+'.png')
	#time.sleep(1)
	#print (wikipedia.summary(search, sentences=2))
	browser.quit()
	
	#print (wikipedia.summary(search, sentences=2))
	#print ('\n')

	


	with io.open("wiki.txt", "a", encoding='utf8') as myfile:

		myfile.write(wikipedia.summary(search, sentences=2))
		myfile.write(u'\n')
		myfile.write(u'\n')	
	time.sleep(1)
	i+=1
f.close()
myfile.close()

	