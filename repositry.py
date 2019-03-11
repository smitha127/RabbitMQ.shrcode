from bs4 import BeautifulSoup
import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import html5lib
import lxml
import time
import json


from src.AutomationPart1.ServiceVo import ServiceVo


chrome_options=Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
driver_path="../../Drivers/chromedriver.exe"
chrome_options=chrome_options

driver=webdriver.Chrome(executable_path=driver_path,chrome_options=chrome_options)
driver.get("https://rolls-royce.leankit.com/Account/Membership/Login")
driver.maximize_window()
element1=driver.find_element_by_id("userName")
element1.send_keys("Amey.Patil@quest-global.com")
element2=driver.find_element_by_id("password")
element2.send_keys("Quest=1234")
driver.find_element_by_class_name("login-rememberLabel").click()
driver.find_element_by_id("Login").click()
driver.find_element_by_class_name("boardList-thumbnail").click()
element_url=driver.current_url
print(element_url)
time.sleep(3)
#r=requests.get(element_url)
soup = BeautifulSoup(driver.page_source, 'lxml')

#print(soup.prettify())
#file=open("baord.html","w+")
#file.write(soup.prettify())
#card_data=[]
#f = open('baord.html')
#soup = BeautifulSoup(f,'lxml')

table=soup.find("div",class_="board-laneContainer u-posAbsolute")
objectlist=[]
data = {}
for i in table:
    print(i)
cardTitle=table.find_all('div',class_="card-background")
cardtype=table.findAll('div',class_="card-background")
cardId=table.findAll('div',class_="laneCardContainer-card")
cardSize=table.findAll('div',class_="cardIcons-icon--cardSize")
cardPF=table.findAll('div',class_="cardIcons-icon--calendar")
for i in range(len(cardTitle)):
    #print(i)
    for row in cardTitle[i] :
        data["Con/DpNo"]=cardTitle[i].div.text
        #print(data["Con/DpNo"])
        title=cardTitle[i].get('title')
        title=title.split(':')
        data["Type"]=title[0]
        data["title"]=title[1]
        #for row in table.findAll('div',class_="laneCardContainer-card"):
    #for row in cardId[i] :
        #print(cardId[0])
        #print(row.div[0])
        #print(row)
        data['cardID'] = cardId[i].get("data-card-id")
       #for row in table.findAll('div',class_="cardIcons-icon--cardSize")  :
        size=cardSize[i].get('title')
        size=size.split(':')
        data['Cardsize']=size[1]
        #for row in table.findAll('div',class_="cardIcons-icon--calendar"):
        date=cardPF[i].get('title')
        date = date.split(':')
        data['PlanedFinishDate']=date[1]
        service = ServiceVo(Con=data["Con/DpNo"], Type=data["Type"], title=data["title"], cardID=data['cardID'],Cardsize=data['Cardsize'], PlanedFinishDate=data['PlanedFinishDate'])
        objectlist.append(service)
        break
for i in objectlist:
    asd=json.dumps(i.__dict__)
    print(asd)



    #print(data)
       ##hdata=data[i]
#service = ServiceVo(Con=data["Con/DpNo"], Type=data["Type"], title=data["title"], cardID=data['cardID'],Cardsize=data['Cardsize'], PlanedFinishDate=data['PlanedFinishDate'])
#objectlist.append(service)
#for i in objectlist:
   # asd=json.dumps(i.__dict__)
   # print(asd)




    #service = ServiceVo()
    #service = [ServiceVo(Con=data["Con/DpNo"], Type=data["Type"], title=data["title"], cardID=data['cardID'], Cardsize=data['Cardsize'],PlanedFinishDate=data['PlanedFinishDate'])];



"""print("*************************Data-5******************************")
card=driver.find_element_by_partial_link_text("eCon 211133571")
time.sleep(3)
card.click()
#/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div[5]/div/div[1]/div/div[2]/div[1]/header
for row in table.findAll('div',class_="cardDetails-group"):
    data5={}
    print("inside the loop")
    data5["Forumpass_Link"]=row.get('value')

    print(data5)"""

#driver.quit()


"""print("*************************Data-2******************************")
for row in table.findAll('header',class_="laneHeader--level3"):
    data2={}
    data2["CurrentLeanID"]=row.get("data-clipboard-text") and row.get("title")==title[0]
    print(row.get('title'))

    print(data2)"""