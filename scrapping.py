from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_reviews(driver):
    review_list = []
    reviews = driver.find_elements(By.CLASS_NAME,"review")
    try:
        for items in reviews:
            review_list.append(items.find_element(By.CLASS_NAME,"review-text").text.strip())
    except Exception as e:
        print(e)
    return review_list


def start_scraping(url,page_count=10):
    final_review_set=[]
    url = url.replace("dp","product-reviews")
    driver = webdriver.Firefox() #webdriver.Chrome()
    loc = url.find("ref")
    initial_page_ref = "ref=cm_cr_dp_d_show_all_btm"
    url_final = url[:loc]+f"/{initial_page_ref}?ie=UTF8&reviewerType=all_reviews&pageNumber="
    new_page = url_final + f'1'
    for x in range(2,page_count):
        driver.get(new_page)
        time.sleep(5)
        reviews = get_reviews(driver)
        #check if there is a next page
        try:
            next_page = driver.find_element(By.CLASS_NAME,'a-disabled a-last')
            break
        except:
            pass
        paging_ref = f'cm_cr_arp_d_paging_btm_next_{x}'
        new_page = url[:loc]+f"/{paging_ref}?ie=UTF8&reviewerType=all_reviews&pageNumber={x}"
        final_review_set.extend(reviews)

    driver.close()
    return final_review_set

#https://www.amazon.de/-/en/Wireless-Keyboard-Function-Windows-Included/dp/B0C3GLZNH3/ref=sr_1_36?crid=B2X08NTM6O0&dib=eyJ2IjoiMSJ9._MUpgKIT1fQakOpmGwusALIJbggeFpToztYrhhE9NEdfvdd5qx9QOSeWiO9J_xS33w5DHuBFESiyrf2K-xU59nEKO0pXqR78o1cazGWPE0YRjMTRh7yNJGKRl7WBrQrKQSKs5K84vKNYGUtqc3js8ggxfMNAGbWm_k33GM2K9mCTwyLI3WY3ThnpZamYEDZh.PzxUzatMKzYij20qlhR-eOoYlTH_4VGdC_ucIXN-FEg&dib_tag=se&keywords=keyboard+pc+wireless&qid=1723023659&sprefix=keyboard+pc+%2Caps%2C106&sr=8-36

if __name__=="__main__":
    url = "https://www.amazon.de/-/en/Wireless-Keyboard-Function-Windows-Included/dp/B0C3GLZNH3/ref=sr_1_36?crid=B2X08NTM6O0&dib=eyJ2IjoiMSJ9._MUpgKIT1fQakOpmGwusALIJbggeFpToztYrhhE9NEdfvdd5qx9QOSeWiO9J_xS33w5DHuBFESiyrf2K-xU59nEKO0pXqR78o1cazGWPE0YRjMTRh7yNJGKRl7WBrQrKQSKs5K84vKNYGUtqc3js8ggxfMNAGbWm_k33GM2K9mCTwyLI3WY3ThnpZamYEDZh.PzxUzatMKzYij20qlhR-eOoYlTH_4VGdC_ucIXN-FEg&dib_tag=se&keywords=keyboard+pc+wireless&qid=1723023659&sprefix=keyboard+pc+%2Caps%2C106&sr=8-36"
    final_review_set = start_scraping(url,5)
    print(final_review_set)
