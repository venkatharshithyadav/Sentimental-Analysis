from selenium import webdriver
from selenium .webdriver.common.by import By
import time
def start_scraping(url,page_count=10):
    url = url.replace("dp","product-reviews")
    driver =webdriver.firefox()
    loc =url.find("ref")
    initial_page_ref= 'ref=sr_1_1_sspa'
    url_final= url[:loc]+f"/{initial_page_ref}?ie=UTF8&reviewsType=all_reviews"
    driver.get(url)
    time.sleep(10)
    driver.get(url_finial)
    time.sleep(10)
    reviews=get_reviews(drivers)
    print(reviews)
    driver.close()


if __name__=="__main__":
    url= "https://www.amazon.de/Apple-iPhone-14-128-Mitternachtsblau/dp/B0BDJH7J5C/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1S0I5026XWHL3&keywords=iphone&qid=1703004473&sprefix=iphone%2Caps%2C133&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
    start_scraping(url,5)
