
#run this before 
#export DISPLAY=:0
#-*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
import sys
import BeautifulSoup
import wikipedia

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

	
