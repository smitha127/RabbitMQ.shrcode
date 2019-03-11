import  requests
from bs4 import BeautifulSoup
import  json
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

login_data={
'userName': 'Amey.Patil@quest-global.com',
'password': 'Quest=1234',
'Login': 'Log in'
}
with requests.session() as s:
    url="https://rolls-royce.leankit.com/Account/Membership/Authenticate?support=False"

    r=s.get(url,headers=headers)

    r=s.post(url,data=login_data,headers=headers)

    r=s.get("https://rolls-royce.leankit.com/io/user/me/board/recent?_=1551685125246")
    boards = ['107600350', '111137067', '123457855', '106606106', '129198897']
    #r=s.get("https://rolls-royce.leankit.com/io/board/106606106?_=1551685125261")

    for i in boards:
        r = s.get("https://rolls-royce.leankit.com/io/board/" + i + "/card?limit=200&id=" + i + "")
        soup1 = BeautifulSoup(r.content, 'lxml')
        cards = soup1.find("p")
        cards = cards.text
        listofcards = []
        card_Nos = {}
        card_Nos = json.loads(cards)
        # print(card_Nos)
        asd = card_Nos['cards']
        # print(asd)
        for i in range(len(asd)):
            # listofcards=['139017768','126333043','144770704']
            listofcards.append(card_Nos['cards'][i]['id'])

        print(listofcards)

        for i in listofcards:
            try:
                r = s.get("https://rolls-royce.leankit.com/io/card/" + i + "?id=" + i + "")
                soup = BeautifulSoup(r.content, 'lxml')
                # print(soup.prettify())
                card = soup.findAll(text=True)
                # print(len(card))
                # print(card)
                # link=card[1]
                # card_data = card.text
                if len(card) > 1:
                    card = card[0] + card[len(card) - 1]
                    # print(card)
                    # card_data = card1.text
                elif len(card) == 1:
                    card = card[0]

                # print(card_data)
                card_Details_data = {}
                card_Details = {}
                # externalLinks = []

                card_Details = json.loads(card)
                # print(card_Details)
                card_body = soup.find('body')

                # actualFinish = card_Details["actualFinish"]
                # actualStart = card_Details['actualStart']
                # blockedStatus = card_Details['blockedStatus']['isBlocked']
                # blockedStatus_reason = card_Details['blockedStatus']['reason']
                # blockedStatus_reason = card_Details['blockedStatus']['date']
                # board_ID = card_Details['board']['id']
                # board_Title = card_Details['board']['title']
                # createdOn = card_Details['createdOn']
                plannedFinish = card_Details['plannedFinish']
                externalLinks = card_Details['externalLinks']
                customId_ConsessionNo = card_Details['customId']['value']
                if (externalLinks != []):
                    externalLinks = card_Details['externalLinks'][0]['url']
                elif (externalLinks == None):
                    externalLinks = card_Details['externalLinks'][0]['label']
                elif (externalLinks == []):
                    externalLinks = soup.findAll(text=True)[1]
                card_ID = card_Details['id']
                lane_ID = card_Details['lane']['id']
                lane_ClassType = card_Details['lane']['laneClassType']
                lane_title = card_Details['lane']['title']
                # updatedOn = card_Details['updatedOn']
                # movedOn = card_Details['movedOn']
                priority = card_Details['priority']
                card_size = card_Details['size']
                card_title = card_Details['title']
                card_title1 = card_title.split(" ")
                engieneNo = card_title1[0]
                engpartNo = str(card_title1[1:])
                card_type = card_Details['type']['title']
                if (lane_ClassType == "backlog"):
                    card_Details_data = {"card_title": card_title, "engieneNo": engieneNo, "partNo": engpartNo,
                                         "customId_ConsessionNo": customId_ConsessionNo, "plannedFinish": plannedFinish,
                                         "externalLinks": externalLinks, "card_ID": card_ID,
                                         "lane_ID": lane_ID, "lane_ClassType": lane_ClassType, "priority": priority,
                                         "card_size": card_size, "card_type": card_type}
                    print(card_Details_data)
            except:
                pass






