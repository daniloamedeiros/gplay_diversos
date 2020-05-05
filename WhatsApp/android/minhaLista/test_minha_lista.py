import unittest
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from android.pages.homePage import Locator
from android.pages.implement import inicializar_appium, swipe_up


class MyTestCase(unittest.TestCase):

    def setUp(self):
        inicializar_appium(self)

    # def tearDown(self):
    #     self.driver.quit()

    def test_something(self):
        locator = Locator(self.driver)

        locator.click_menu_perfil()
        locator.click_minha_lista()


        while True:
            try:
                locator.click_minha_lista()
                locator.assert_minha_lista_vazia()

                break
            except NoSuchElementException:

                locator.click_primeiro_item_minha_lista()
                locator.click_adicionar_remover_item_minha_lista()
                sleep(5)
                locator.click_navegar_voltar()
                sleep(5)
                locator.click_navegar_voltar()

        locator.click_navegar_voltar()
        sleep(5)
        locator.click_navegar_voltar()
        locator.click_banner_destaque()
        locator.click_adicionar_remover_item_minha_lista()
        sleep(5)
        locator.click_navegar_voltar()
        locator.click_menu_perfil()
        locator.click_minha_lista()
        locator.click_primeiro_item_minha_lista()

        self.driver.close_app()
        sleep(10)
        self.driver.launch_app()

        locator.click_menu_perfil()
        locator.click_minha_lista()

        locator.click_primeiro_item_minha_lista()
        locator.assert_item_adicionado_minha_lista()

        self.driver.launch_app()
        sleep(10)


        self.driver.implicitly_wait(10)
        previous_title = None
        repeat_count = 0
        while True:
            try:
                locator.trilho_minha_lista()


                break
            except NoSuchElementException:
                swipe_up(self.driver)
                item = self.driver.find_element_by_android_uiautomator(
                    'new UiSelector().className("android.widget.TextView")')
                print(">>>>>>>>>> ", item.text)
                if item.text == previous_title:
                    repeat_count += 1

                if repeat_count == 3:
                    raise Exception("Trilho do Continue assistindo não disponivel")
                previous_title = item.text




if __name__ == '__main__':
    unittest.main()
