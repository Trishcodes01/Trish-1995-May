num = 10
word = "new"
try:
     output = num + word
     print(output)
except:
    print(word[0])

import requests
from bs4 import BeautifulSoup as BS

url = "https://jumia.com.ng/smartphones/"
headers = requests.utils.default_headers() #access default headers that comes with python header
headers.update({
    "user-agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
})

my_response = requests.get(url, headers)
# print(my_response.status_code)

first_soup = BS(my_response.content, features = "lxml")
# print(first_soup)
second_soup = first_soup.find("div", attrs = {"class" : "-paxs row _no-g _4cl-3cm-shs"})
# print(second_soup)

list_of_soups = second_soup.find_all("article", attrs = {"class" : "prd _fb col c-prd"})
for soup in list_of_soups:
    # print(soup.prettify())
    phone_details = soup.find("a")
    ### FOR PHONE BRAND
    # try:
    #     phone_brand = phone_details.get("data-brand")
    #     print(phone_brand)
    # except:
    #     phone_brand = None
    # break

    #FOR PHONE DESCRIPTION
    # try:
    #     phone_description = phone_details.get("data-name")
    #     print(phone_description)
    # except:
    #     phone_description = None
    # break

    ##FOR PHONE OLD PRICE, to remove the naira symbol and the comma
    # try:
    #     old_div = soup.find("div", attrs = {"class" : "old"})
    #     phone_old_price = old_div.text
    #     a = phone_old_price.lstrip("₦")
    #     # print(a)
    #     d = a.split(",")
    #     # print(d)
    #     string = [str(latest) for latest in d]
    #     a_string = "".join(string)
    #     an_latest = int(a_string)
    #     print(an_latest)
    # except:
    #     phone_old_price = None
    # break

    # try:
    #     old_div = soup.find("div", attrs = {"class" : "old"})
    #     phone_old_price = int((old_div.text).lstrip("₦").replace(",", ""))
    #     print(phone_old_price)
    # except:
    #     phone_old_price = None
    # break

    # try:
    #     new_div = soup.find("div", attrs = {"class" : "prc"})
    #     phone_new_price = int((new_div.text).lstrip("₦").replace(",", ""))
    #     print(phone_new_price)
    # except:
    #     phone_new_price = None
    # break

    # try:
    #     disct_div = soup.find("div", attrs = {"class" : "tag _dsct _sm"})
    #     phone_disct_price = disct_div.text
    #     print(phone_disct_price)
    # except:
    #     phone_disct_price = None
    # break          

    try:
        rating_div = soup.find("div", attrs = {"class" : "stars _s"})
        phone_rating_price = rating_div.text
        # print(phone_rating_price)
        # rating_value = (rating_div.text[0])
        # print(rating_value)
        rating_value = float((rating_div.text).replace("")
    except:
        phone_rating_price = None
    break          ;