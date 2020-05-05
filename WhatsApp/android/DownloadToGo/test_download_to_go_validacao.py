import unittest
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from android.pages.homePage import Locator
from android.pages.implement import inicializar_appium


class MyTestCase(unittest.TestCase):

    def setUp(self):
        inicializar_appium(self)

    # def tearDown(self):
    #     self.driver.quit()


    def test_something(self):
        locator = Locator(self.driver)


        locator.click_menu_download()

        while True:
            try:
                locator.assert_lista_download_vazio()
                break
            except NoSuchElementException:

                locator.click_selecionar_itens_downlaod()
                locator.click_primeiro_item_lista_download()
                locator.click_apagar_download()


        locator.click_menu_categorias()
        locator.click_categoria_novela()
        locator.click_primeiro_item_categoria_novela()
        locator.click_icone_download_lista_capitulo()
        sleep(10)
        locator.click_navegar_voltar()
        locator.click_menu_download()
        locator.click_primeiro_item_lista_download()

        while True:
            try:

                locator.assert_download_concluido()
                print(">>>>>>>>>>>>> Download realizado com sucesso!!!!")
                break

            except NoSuchElementException:
                print("\n> Download em andamento ...")




if __name__ == '__main__':
    unittest.main()
