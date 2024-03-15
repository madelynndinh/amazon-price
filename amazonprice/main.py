import requests
from bs4 import BeautifulSoup
import lxml
import smtplib


URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"

}

app_pw = "wlig juzw ifth jbjj"
mail = "madelynndinh@gmail.com"
BUY_PRICE = 100
recipient = "minhtam71.work@gmail.com"


response = requests.get(URL,headers=header)
yc_web_page = response.content
soup = BeautifulSoup(yc_web_page,"lxml")
title = soup.find(id="productTitle").getText()
print(title)



price = soup.find(class_="a-offscreen").getText().split("$")[1]
priceFloat = float(price)
print(priceFloat)


if priceFloat<BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
        connection.starttls()
        result = connection.login(mail, app_pw)
        connection.sendmail(
            from_addr=mail,
            to_addrs= recipient,
            msg=f"Subject: Amazon Price Alert!\n\n {message}\n{URL}".encode("utf-8")
        )


