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


def created_driver_of_page(url_product):
    driver = webdriver.Firefox()
    driver.get(url_product)
    return driver


def accept_cookies(driver_page):
    driver_page.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div/div[2]/button[2]').click()
    sleep(2)


def process_of_buy(driver_page):
    driver_page.find_element(by=By.NAME, value="add-to-cart").click()
    sleep(2)
    final_buy = driver_page.find_element(by=By.CLASS_NAME, value="wc-proceed-to-checkout")
    final_buy.find_element(by=By.TAG_NAME, value="a").click()
    sleep(2)


def complete_formulary(driver_page):
    facturation_formulary = driver_page.find_element(by=By.CLASS_NAME, value="woocommerce-billing-fields")
    facturation_formulary.find_element(by=By.NAME, value="billing_first_name").send_keys("David")
    facturation_formulary.find_element(by=By.NAME, value="billing_last_name").send_keys("Becerra ")
    facturation_formulary.find_element(by=By.NAME, value="billing_id_cliente").send_keys("1122554499")
    facturation_formulary.find_element(by=By.NAME, value="billing_address_1").send_keys("Tv.50C#90Sur-24")
    facturation_formulary.find_element(by=By.NAME, value="billing_address_2").send_keys("Alamos")
    sleep(3)
    driver_page.find_element(by=By.XPATH, value='//*[@id="billing_city_field"]/span/span[1]/span').click()
    driver_page.find_element(by=By.XPATH, value='/html/body/span[2]/span/span[2]/ul/li[2]').click()
    sleep(3)
    facturation_formulary.find_element(by=By.NAME, value="billing_phone").send_keys("3016814746")
    facturation_formulary.find_element(by=By.NAME, value="billing_email").send_keys("dbecerra655@gmail.com")
    sleep(2)


def accept_terms_and_buy(driver_page):
    driver_page.find_element(by=By.XPATH, value='//*[@id="terms"]').click()
    driver_page.find_element(by=By.XPATH, value='//*[@id="place_order"]').click()


def main():
    # Definimos la url del producto que vamos ha comprar
    url_product = create_url()
    # Conectamos con la pagina
    page_product = connection_to_page(url_product)
    # Miramos si hay stock
    theres_stock = review_stock(page_product)

    if theres_stock:
        # creamos el conductor
        driver_page = created_driver_of_page(url_product)
        sleep(2)
        # acceptamos las cookies
        accept_cookies(driver_page)
        # empezamos el proceso de compra
        process_of_buy(driver_page)
        # Llenamos el formulario de compra
        complete_formulary(driver_page)
        # Aceptamos la compra y realizamos la compra
        accept_terms_and_buy(driver_page)


if __name__ == '__main__':
    main()

