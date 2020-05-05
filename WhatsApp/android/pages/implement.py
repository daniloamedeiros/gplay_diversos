from locator import locator
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver import webdriver
from appium import webdriver


def inicializar_appium(self):
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

    url = "http://127.0.0.1:4723/wd/hub" # Url Appium local
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
    return self.driver


def login(driver):
    driver.implicitly_wait(10)
    user_icon = driver.find_element_by_id("com.globo.globotv:id/menu_profile_custom_view_profile")
    user_icon.click()
    try:
        driver.implicitly_wait(10)
        entrar = driver.find_element_by_id('com.globo.globotv:id/activity_profile_text_view_get_int')
        entrar.click()
        driver.implicitly_wait(60)

        # login no GloboID
        email = driver.find_element_by_class_name('android.widget.EditText')
        email.set_value('laurent_headspin')
        driver.implicitly_wait(1)
        # password
        password = driver.find_elements_by_class_name('android.widget.EditText')[1]
        password.set_value('Globo@321')
        driver.implicitly_wait(1)
        # #botao globoid
        buttons = driver.find_elements_by_class_name("android.widget.Button")
        for button in buttons:
            entrar = button.text
            if entrar == "ENTRAR":
                button.click()
                driver.implicitly_wait(50)
                btn_voltar_home = driver.find_element_by_class_name("android.widget.ImageButton")
                btn_voltar_home.click()
                break

        # logout = driver.find_element_by_android_uiautomator('new UiSelector().text("Sair")')
        # logout.click()
        # btn = driver.find_element_by_id('android:id/button1')
        # btn.click()


    except NoSuchElementException:
        pass

        # import pdb; pdb.set_trace()


def logout(driver):
    driver.implicitly_wait(10)

    user_icon = driver.find_element_by_id("com.globo.globotv:id/menu_profile_custom_view_profile")
    user_icon.click()
    try:
        logout = driver.find_element_by_android_uiautomator('new UiSelector().text("Sair")')
        logout.click()
        btn = driver.find_element_by_id('android:id/button1')
        btn.click()
    except NoSuchElementException:
        pass

    btn_back = driver.find_element_by_class_name('android.widget.ImageButton')
    btn_back.click()

def swipe_up(driver):
    screen = driver.get_window_size()
    w = screen['width']
    h = screen['height']
    move_x = w / 2
    move_y = h * 0.7
    move_end_x = w / 2
    move_end_y = h * 0.3
    driver.swipe(move_x, move_y, move_end_x, move_end_y)


    def pesquisar_trilho(self):

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

