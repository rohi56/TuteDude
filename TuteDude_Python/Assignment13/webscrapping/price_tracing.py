import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
             'Accept-Language' : 'en-GB,en-US;q=0.9,en;q=0.8',
            'Accept-Encoding' : 'gzip, deflate, br'
        }
        self.response = requests.get(self.url, headers=self.headers).text
        self.soup = BeautifulSoup(self.response, 'lxml')
    
    def product_title(self):
        title_tag = self.soup.find("title")
        if title_tag:
            clean_title = title_tag.get_text(strip=True)
            return clean_title.replace(": Amazon.in: Electronics", "")
        return "Title Not Found"


    
    def product_price(self):
        price = self.soup.find('span', {'class': 'a-price-whole'})
        if price is not None:
            return price.text.strip()
        
        else:
            return "Price Not Found"
        
        
device  = PriceTracer('https://www.amazon.in/Samsung-Smartphone-Silverblue-Snapdragon-ProVisual/dp/B0DSKNKCYX/ref=sr_1_2?dib=eyJ2IjoiMSJ9.TnXF_RGJpd3TbN40AampmLjiEJtIW0WBw19pB2Pb9aLNtYIPcaDT0Vzjrc-ydXDiQcHW_bai0Ww1Heyk8ZBk-zBQA60GkqlVxKp_4b9b5tZEIiVu1gTLmtpIpQ0JYwfR3IFiGczZiopw_gQScpOTy9ctMOBdx1JF3uELJF8MZjl6tiKUAzSfx1gfrVP2JMmckHe-pHfxU4ftVUmwm9jXMulf8GwCAVnj0Ruejk1W6koLYYlKISylGKg539vEnYp1u3yfR43LDuCB6MZL8HsZ5f2qw0qwf4QwuAy3aENDKDU.6IlC2T1pQAOk8Ntojqd8PA0MeQwQglLZ6qMK_Kb2Weo&dib_tag=se&keywords=samsung%2Bgalaxy%2Bs25%2Bultra%2B5g&nsdOptOutParam=true&qid=1757411452&s=electronics&sr=1-2&th=1')
print(device.product_title())
print(device.product_price())


device2 = PriceTracer('https://www.amazon.in/dp/B0FDL5T1PF/ref=sspa_dk_detail_1?pd_rd_i=B0FDL5T1PF&pd_rd_w=u55YK&content-id=amzn1.sym.67d3dec9-3503-44a1-a945-e969d04cca69&pf_rd_p=67d3dec9-3503-44a1-a945-e969d04cca69&pf_rd_r=GM5AYHFXDBBJEWBF128H&pd_rd_wg=QePou&pd_rd_r=10704fec-767b-4f22-b5b6-c2374c980022&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1')
print(device2.product_title())
print(device2.product_price())