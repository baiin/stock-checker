import requests
import tkinter
import bs4

symbolfile = open("symbols.txt")
symbolslist = symbolfile.read()
symbolslist = symbolslist.split("\n")

print(len(symbolslist))

for i in range(len(symbolslist)):

    url = "http://finance.yahoo.com/q?s=" + symbolslist[i]
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    data_a = soup.find("div", {"class": "title"}).h2.contents
    data_b = soup.find("span", {"class": "time_rtq_ticker"}).span.contents

    print("NAME: ", data_a[0])
    print("PRICE: ", data_b[0])
    print("----------------------")

    

