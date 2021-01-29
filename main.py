import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.bdshop.com/redmi-note-9-pro-6gb-128gb'

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

page = requests.get(URL,headers = headers)
soup = BeautifulSoup(page.content,'html.parser')

#print(soup.prettify())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    title= get_title()

    server.login('romanraihan17@gmail.com','ctemsnvaidrnycjs')
    subject = "Hey, The price of "+title+" has fell down"
    body = "Check the BdShop link !" + URL + "\n You have requested for this price fell down notification"

    message = f"Subject:{subject}\n\n{body}"

    server.sendmail('romanraihan17@gmail.com','romanraihan60@gmail.com',message)
    print("Hey, mail has been sent to your link")
    server.quit()


def get_title():
    title = soup.find(class_ = "base").get_text()
    return title


def check_price():
    price = soup.find(class_="price")
    price = price.get_text()
    price = price[1:]
    price_list = price.split(",")
    length = len(price_list)
    modified_price = ''

    for i in range(length):
        modified_price = modified_price+price_list[i]

    modified_price = float(modified_price)

    if modified_price < 28000:
        send_mail()

while(True):
    check_price()
    time.sleep(60*60*24)



