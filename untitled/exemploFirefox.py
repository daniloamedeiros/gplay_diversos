import requests
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver


def instanciar_driver():
    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    caps["binary"] = "C:\Program Files\Mozilla Firefox\firefox.exe"
    driver = webdriver.firefox(capabilities=caps, executable_path="")

    def carregando_url(webdriver, url):
        webdriver.set_page_load_timeout(30)
        webdriver.set_page.get(url)
        url = requests.get(url)
        print(url.status_code)

        def instanciar_driver():
            teste = carregando_url(webdriver, "https://www.google.com.br")
            assert teste == 200, "Erro ao carregar a página"
