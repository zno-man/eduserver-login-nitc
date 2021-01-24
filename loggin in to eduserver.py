import selenium
import requests 
from bs4 import BeautifulSoup 
import msvcrt

from selenium import webdriver
import pandas as pd
import time
import os
import subprocess

try:
    f = open('login data.txt','r')
    temp = f.read().split()
    rno = temp[0]
    pswd = temp[1]
except:
    f = open('login data.txt','w')
    print('enter your roll no  :',end = '')
    rno = input()
    print('enter your password :',end = '')
    pswd = input()    
    f.write(rno)
    f.write(' ')
    f.write(pswd)



f.close()



def kill():

    taskname ='"'
    taskname+='chromedriver.exe'  #this is its name , the cisco pop up name
    #taskname+='NOTEPAD.exe'
    taskname+='"'
    while(True):
        try:
            #(os.popen('taskkill /IM '+taskname+' /F')) 
            st = str(subprocess.check_output('taskkill /IM '+taskname+' /F',shell = True).decode('utf-8'))
        except:
            print("\nall instances terminated ; extiting program....")
            time.sleep(2)
            break
        
        else :

            print(taskname +' terminated ')
    


def edu_login():
    driver.get ("https://eduserver.nitc.ac.in/login/index.php")

def menu():
    print("""
            1 -- DSP 

            2 -- DSD 

            3 -- MACHINES LAB 

            4 -- CS II 

            5 -- ESDB 

            6 -- PS II 

            7 -- ELECTRICAL DRAWING 

            8 -- POM 

                                       enter subject code ->|:""",end = '')
    
    links   = {'1':'https://eduserver.nitc.ac.in/course/view.php?id=835',
               '2':'https://eduserver.nitc.ac.in/course/view.php?id=849',
               '3':'https://eduserver.nitc.ac.in/course/view.php?id=837',
               '4':'https://eduserver.nitc.ac.in/course/view.php?id=836',
               '5':'https://eduserver.nitc.ac.in/course/view.php?id=850',
               '6':'https://eduserver.nitc.ac.in/course/view.php?id=854',
               '7':'https://eduserver.nitc.ac.in/course/view.php?id=838',
               '8':'https://eduserver.nitc.ac.in/course/view.php?id=1145'
               }
    ch = input()

    while(True):
        
        try:
            links[ch]
        except:
            print('the value you entered is out of range please try again...')
            print('\n                                       enter subject code ->|:',end = '')
            ch = input()
        else:
            break
        
    return(links[ch])

    
URL = menu()


#do the login


driver = webdriver.Chrome(os.getcwd()+'\chromedriver.exe')
driver.get(URL)

driver.find_element_by_id("username").send_keys(rno)
driver.find_element_by_id ("password").send_keys(pswd)
driver.find_element_by_tag_name("button").click()



a = driver.page_source
soup = BeautifulSoup(a,features="html.parser")

#time.sleep(1)
#driver.close()
kill()

st = []
for i in soup.findAll('a'):
    temp = (i.get_text().strip())
    if 'attendance'.upper() in temp.upper():
        print(i)


print(st)




msvcrt.getch()
