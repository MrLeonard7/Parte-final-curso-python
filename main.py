from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By


def create_url():
    url = "https://speedlogic.com.co/producto/tarjeta-de-video-asus-geforce-gt-1030-ddr5-oc-phoenix-1fan-2-gigas/"
    return url

def connection_to_page(url):
    session = HTMLSession()
    page = session.get(url)
    return page


def review_stock(page):
    while True:
        buy_zone = page.html.find("#product-23980")
        if len(buy_zone) > 0:
            print("HAY STOCK")
            return True
        else:
            print("Sigue sin aver stock")
        sleep(30)


def main():
    # Pedimos al usuario que prducto va ha comprar
    url_product = create_url()
    # Conectamos con la pagina
    page_product = connection_to_page(url_product)
    # Miramos si hay stock
    theres_stock = review_stock(page_product)

    if theres_stock:
        driver = webdriver.Firefox()
        driver.get(url_product)
        driver.find_element(by=By.NAME, value="add-to-cart").click()
        sleep(2)
        final_buy = driver.find_element(by=By.CLASS_NAME, value="wc-proceed-to-checkout")
        final_buy.find_element(by=By.TAG_NAME, value="a").click()
        sleep(2)
        facturation_and_send_formulary = driver.find_element(by=By.CLASS_NAME, value="woocommerce-billing-fields")
        facturation_and_send_formulary.find_element(by=By.NAME, value="billing_first_name").send_keys("David")
        facturation_and_send_formulary.find_element(by=By.NAME, value="billing_last_name").send_keys("Becerra Panqueva")
        facturation_and_send_formulary.find_element(by=By.NAME, value="billing_id_cliente").send_keys("1193476186")
        facturation_and_send_formulary.find_element(by=By.NAME, value="billing_address_1").send_keys("Tv.49C#73Sur-12")
        facturation_and_send_formulary.find_element(by=By.NAME, value="billing_address_2").send_keys("Sierra morena")
        facturation_and_send_formulary.find_element(by=By.NAME, value="billing_phone").send_keys("3016814746")
        facturation_and_send_formulary.find_element(by=By.NAME, value="billing_email").send_keys("dbecerra655@gmail.com")
        accept_order_and_terms = driver.find_element(by=By.ID, value="order_review")
        accept_order_and_terms.find_element(by=By.ID, value="terms").click()
        accept_order_and_terms.find_element(by=By.NAME, value="woocommerce_checkout_place_order")


if __name__ == '__main__':
    main()

