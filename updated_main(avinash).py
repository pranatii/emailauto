
import os
import shutil

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from six.moves import urllib
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime

def ex(searchString,path,page):
    browser = webdriver.Chrome(executable_path=path)
    searchUrl = "https://www.google.com/search?q="+searchString+"&source=lnms&tbm=isch"

    browser.get(searchUrl)
    time.sleep(1)

    elem = browser.find_element_by_tag_name('body')

    no_of_pagedowns = page

    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1

    post_elems = browser.find_elements_by_class_name("rg_i")
    lt=[]
    for post in post_elems:
        lt.append(post.get_attribute('src'))

    f= open("urls.txt","w+")
    for y in lt[20:]:
        f.write(str(y)+'\n')
    f.close()

    with open("urls.txt", "r") as input:
        with open("temp.txt", "w") as output:
            # iterate all lines from file
            for line in input:
                # if substring contain in a line then don't write it
                if "None" not in line.strip("\n"):
                    output.write(line)

    # replace file with original name
    os.replace('temp.txt', 'urls.txt')
    with open('urls.txt') as f:
        lines = [line.rstrip() for line in f]

    os.mkdir('kaks')
    for i,j in enumerate(lines):
        jojo= urllib.request.urlretrieve(j,'img'+str(i)+'.jpg')
        os.rename(jojo[0], "kaks/"+jojo[0])

    shutil.make_archive('kaks', 'zip', 'kaks')
    browser.quit()

def email(usermail,password,clientemail):

    msg = MIMEMultipart()
    filename='kaks.zip'
    attachment  =open(filename,'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)
    msg.attach(part)
    text = msg.as_string()
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)

    server.login(usermail,password)
    server.sendmail(usermail,clientemail,text)
    server.quit()
def de():
    os.remove("urls.txt")
    os.remove("kaks.zip")
    shutil. rmtree("kaks")


def main_job(year,month,date,hour,minute,second,name,path,page,username,password,clientmail):
    sendtime = datetime.datetime(year,month,date,hour,minute,second)
    st = sendtime.timestamp()
    t = time.time()
    print(f"scheduled time:{year}-{month}-{date}-{hour}-{minute}-{second}")

    x = time.sleep(st - t)
    ex(name,path,page)
    time.sleep(15)
    email(username,password,clientmail)
    time.sleep(3)
    de()

#
# """
#
# main_job(year,month,date,hour,minute,second,name of the thing,path of your chromedrive.exe(you have to give the path in raw format,
# eg. r"C:\Users\ADMIN\Downloads\chromedriver_win32\chromedriver.exe" ),how many times you want to scroll the webpage,your email id,your password,client's email id)
#
# main_job(2021,8,13,00,00,00,"cats",r"C:\Users\ADMIN\Downloads\chromedriver_win32\chromedriver.exe",10,"youremailid","password","clientemailid")
#
#
#
# if there is a gmail authentication erron..........
#
#
# https: // myaccount.google.com / lesssecureapps?pli = 1 & rapt = AEjHL4NoPGAIuu_It757bkDeFtPrGVtbKB9FnMFUVkkp4Nhhldhmqm4jR0jTujaRMutCqVPZwNRbpbgsddZCDTVmGjxp4Pe2jg
#
# ........go here and allow less secure apps
#
# """


main_job(2021,8,15,8,9,0,'dogs',r'C:\Users\ADMIN\Downloads\chromedriver_win32\chromedriver.exe',1,'sarkarsar123@gmail.com','a123b123','sarkarsar123@gmail.com')




















