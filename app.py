# Online store comparison engine.
import requests
from bs4 import BeautifulSoup


class ComparisonEngine:

    def getFlipkartPrice(self, url):
        response = self.handleHTTP(url)
        data = BeautifulSoup(response.content, "lxml")
        target_div = data.find("div", {"class": "_1vC4OE _3qQ9m1"})
        unformatted_price = target_div.text
        list_of_price_elements = unformatted_price.split('₹')
        if list_of_price_elements[1] is not None:
            return int(list_of_price_elements[1])
        else:
            print("Price not found!")
            return -1

    def getAmazonPrice(self, url):
        response = self.handleHTTP(url)
        data = BeautifulSoup(response.content , 'lxml')
        target_div = data.find("span", {"class" : "a-size-base a-color-price a-color-price"})
        unformatted_price = str(target_div).split(' ')[-5]
        list_of_price_elements = unformatted_price.split(("\n"))
        return int(float(list_of_price_elements[0]))
        
    def getSnapdealPrice(self, url):
        response = self.handleHTTP(url)
        data = BeautifulSoup(response.content, 'lxml')
        target_div = data.find ("span" , {"class" : "payBlkBig"})
        return int(target_div.text)
        

    def handleHTTP(self, url):
        if url is not None:
            response = requests.get(url)
            if response is not None:
                return response
            else:
                print("Response invlaid!")


flipkart_price = ComparisonEngine().getFlipkartPrice("https://www.flipkart.com/harry-potter-deathly-hallows/p/itmfc4a2fx8qjkbw?pid=9781408855713&lid=LSTBOK9781408855713V6GNDA&marketplace=FLIPKART&srno=s_1_2&otracker=search&fm=SEARCH&iid=fef4d86e-4be3-42f9-9644-72bc863263af.9781408855713.SEARCH&ppt=ProductPage&ppn=ProductPage&ssid=f6r0bgbe0g0000001552901463341&qH=b245005e8b3df99a")
amazon_price = ComparisonEngine().getAmazonPrice("https://www.amazon.in/Harry-Potter-Deathly-Hallows/dp/1408855712/ref=sr_1_1?s=books&ie=UTF8&qid=1552902593&sr=1-1&keywords=harry+potter+and+the+deathly+hallows")
snapdeal_price = ComparisonEngine().getSnapdealPrice("https://www.snapdeal.com/product/harry-potter-and-the-deathly/618550513335")

if flipkart_price > 0 and amazon_price > 0 and snapdeal_price>0:
    print("Amazon ", amazon_price)
    print("Flipkart ", flipkart_price)
    print("Snapdeal ", snapdeal_price)
