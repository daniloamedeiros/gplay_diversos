import unittest
from Working.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from android.pages.homePage import Locator
from android.pages.implement import inicializar_appium, swipe_up


class MyTestCase(unittest.TestCase):

    def setUp(self):
        inicializar_appium(self)
        bp = BasePage(self.driver)

    def tearDown(self):
        self.driver.quit()


    def test_something(self):
        bp = BasePage(self.driver)
        locator = Locator(self.driver)
        self.driver.implicitly_wait(10)


        previous_title = None
        repeat_count = 0
        while True:
            try:
                locator.assistir_titulo()
                locator.poster()

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
