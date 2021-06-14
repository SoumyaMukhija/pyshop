# Online store comparison engine.
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

@dataclass
class ComparisonEngine():
    """The base class of all ComparisonEngine.
    """
    url: str
    # price: int = self.getPrice()

    def handleHTTP(self):
        if self.url is not None:
            response = requests.get(self.url)
            if response is not None:
                return response
            else:
                print("Response invlaid!")

    def getPrice(self):
        pass


class FlipkartEngine(ComparisonEngine):

    def getPrice(self):
        response = self.handleHTTP()
        data = BeautifulSoup(response.content, "lxml")
        target_div = data.find("div", {"class": "_1vC4OE _3qQ9m1"})
        unformatted_price = target_div.text
        list_of_price_elements = unformatted_price.split('₹')
        if list_of_price_elements[1] is not None:
            return int(list_of_price_elements[1])
        else:
            print("Price not found!")
            return -1


class AmazonEngine(ComparisonEngine):
    
    def getPrice(self):
        response = self.handleHTTP()
        data = BeautifulSoup(response.content , 'lxml')
        target_div = data.find("span", {"class" : "a-size-base a-color-price a-color-price"})
        unformatted_price = str(target_div).split(' ')[-5]
        list_of_price_elements = unformatted_price.split(("\n"))
        return int(float(list_of_price_elements[0]))
        
class SnapdealEngine(ComparisonEngine):

    def getPrice(self, url):
        response = self.handleHTTP()
        data = BeautifulSoup(response.content, 'lxml')
        target_div = data.find ("span" , {"class" : "payBlkBig"})
        return int(target_div.text)

flipkart_url = "https://www.flipkart.com/harry-potter-deathly-hallows/p/itmfc4a2fx8qjkbw?pid=9781408855713&lid=LSTBOK9781408855713V6GNDA&marketplace=FLIPKART&srno=s_1_2&otracker=search&fm=SEARCH&iid=fef4d86e-4be3-42f9-9644-72bc863263af.9781408855713.SEARCH&ppt=ProductPage&ppn=ProductPage&ssid=f6r0bgbe0g0000001552901463341&qH=b245005e8b3df99a"
amazon_url   = "https://www.amazon.in/Harry-Potter-Deathly-Hallows/dp/1408855712/ref=sr_1_1?s=books&ie=UTF8&qid=1552902593&sr=1-1&keywords=harry+potter+and+the+deathly+hallows"
snapdeal_url = "https://www.snapdeal.com/product/harry-potter-and-the-deathly/618550513335"
        
flipkart_price = FlipkartEngine(flipkart_url).getPrice()
amazon_price = AmazonEngine(amazon_url).getPrice()
snapdeal_price = SnapdealEngine(snapdeal_url).getPrice()

if flipkart_price > 0 and amazon_price > 0 and snapdeal_price > 0:
    print("Amazon: ", amazon_price)
    print("Flipkart: ", flipkart_price)
    print("Snapdeal: ", snapdeal_price)
    
# exp not to hardcode in main block
# urls = ['flip', 'amaz', 'snap']
# engines = [FlipkartEngine: flipkart_url,
#            AmazonEngine: amazon_url,
#            SnapdealEngine: snapdeal_url]x[(a

# for url in urls:
#     engines.__getattribute__(name)
