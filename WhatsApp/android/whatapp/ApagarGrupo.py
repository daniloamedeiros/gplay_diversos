import unittest
from appium.webdriver import webdriver
from appium import webdriver
from time import sleep


class MyTestCase(unittest.TestCase):


    def test_something(self):
        udid = "ZY3235B66B"  # motoG
        # udid = "330073bd2b2bb325" #j7 prime
        # udid = "4200d58fd878548f" #j5 prime
        # udid = "ZY225FNTX8"  # motoG7 novo
        # udid = "ZY224VFBJR"  # MOTO Z2
        # udid = "HAAXB7611423Y4Y"  # ZENFONE 4 MAX
        # udid = "39587924f93f7ece"  # S9
        # udid = "ad061703bcaf56bc2b"  # S7 Edge
        # udid = "NVCQ5HNJ7DS8DMFM"  # LG K4
        # udid = "N2F4C15605001333"  # HUAWEI P8
        # udid = "0057160804"  # Headspin galax tab

        url = "http://127.0.0.1:4723/wd/hub"  # Url Appium local
        # url = "https://br-sao.headspin.io:7012/v0/e0dfc76ad34c4b9882a4734ef479a891/wd/hub"
        # url = "https://br-sao.headspin.io:7012/v0/e0dfc76ad34c4b9882a4734ef479a891/wd/hub"

        desired_caps = {}
        desired_caps['platformName'] = "Android"
        desired_caps['udid'] = udid
        desired_caps['deviceName'] = udid
        desired_caps['appPackage'] = "com.whatsapp"
        desired_caps['appActivity'] = "com.whatsapp.HomeActivity"
        desired_caps['noReset'] = True
        desired_caps['automationName'] = "uiautomator2"
        desired_caps['newCommandTimeout'] = 900
        desired_caps['no-reset'] = True
        url = url
        self.driver = webdriver.Remote(url, desired_caps)

        sleep(5)


        categorias = self.driver.find_element_by_id("com.whatsapp:id/eula_accept").click()
        sleep(2)

        els5 = self.driver.find_element_by_id("Qual é meu número?").click()
        sleep(2)
        els6 = self.driver.find_element_by_id("com.whatsapp:id/submit").click()
        sleep(2)
        permitir = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        sleep(2)
        usar = self.driver.find_element_by_id("android:id/button1").click()
        sleep(2)
        avancar= self.driver.find_element_by_id("com.whatsapp:id/registration_submit").click()
        sleep(5)
        ok = self.driver.find_element_by_id("android:id/button1").click()



if __name__ == '__main__':
    unittest.main()
