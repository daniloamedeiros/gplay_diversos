from time import sleep
import os

import time
import unittest
import logging
import datetime
import sys

from appium import webdriver


class SimpleAndroidTests(unittest.TestCase):

    def setUp(self):

        self.reference = str(int(round(time.time() * 1000)))
        self.package = "com.globo.globotv"

        # device id as 1st argument
        self.udid = sys.argv[1]
        self.os = 'Android'

        # desired caps for the app
        desired_caps = {}
        desired_caps['platformName'] = self.os
        desired_caps['udid'] = self.udid
        desired_caps['deviceName'] = self.udid
        desired_caps['appPackage'] = self.package
        desired_caps['appActivity'] = "com.globo.globotv.splash.SplashActivity"
        desired_caps['noReset'] = True
        desired_caps['automationName'] = "uiautomator2"
        desired_caps['newCommandTimeout'] = 600
        desired_caps['no-reset'] = True

        appium_input = sys.argv[2]
        if appium_input.isdigit():
            self.url = ('http://127.0.0.1:' + appium_input + '/wd/hub')
        else:
            self.url = appium_input

        # launching app
        self.driver = webdriver.Remote(self.url, desired_caps)

        self.start_app = int(round(time.time() * 1000))

        # initialising variables
        self.status = "Fail_launch"
        self.app_launch_time = 0

        self.status_dic = {}
        self.kpi_dic = {}

        self.app_launch_time = 0
        self.video_laod_time = 0
        self.home_pg_load_time = 0
        self.title_check = False
        self.progress_check = False
        self.test_name = "Continue_Assistindo"
        self.kpi_count = 5
        self.pass_count = 0
        self.fail_count = 0

    def tearDown(self):

        # incrementing kpi count
        print("Pass count is %s" % self.pass_count)
        if self.pass_count != self.kpi_count:
            self.fail_count = self.kpi_count - self.pass_count
        else:
            self.fail_count = 0
        print("Fail count is %s " % self.fail_count)

        # self.driver.quit()

    def videoplay_check(self, sec):
        self.driver.implicitly_wait(5)
        t_end = time.time() + sec
        while time.time() < t_end:
            try:
                screen_size = self.driver.get_window_size()
                width = screen_size['width']
                height = screen_size['height']
                tap_x = width * 0.5
                tap_y = height * 0.23
                self.driver.tap([(tap_x, tap_y)])
                player_control = self.driver.find_element_by_id("com.globo.globotv:id/media_control")
                sleep(5)
            except:
                spinner = self.driver.find_element_by_id('com.globo.globotv:id/progress_bar')
                print("Video Interrupted")
                self.video_play()

    def video_play(self):
        self.driver.implicitly_wait(1)
        t_end = time.time() + 10
        while time.time() < t_end:
            try:
                spinner = self.driver.find_element_by_id('com.globo.globotv:id/progress_bar')
                print("Spinner!!")
            except:
                break

    def test_login(self):

        self.driver.implicitly_wait(60)
        # Launching app
        # home_page_image = self.driver.find_element_by_id('com.globo.globotv:id/custom_view_premium_highlights_image_view_background')
        launched_app = int(round(time.time() * 1000))

        # calcualting launch time
        self.app_launch_time = launched_app - self.start_app
        print("App Launch Time is %s ms" % self.app_launch_time)
        d = {'globo_launch_time': self.app_launch_time}
        self.kpi_dic.update(d)
        # incrementing pass count
        self.pass_count += 1

        # library tab view time
        self.status = "Fail_login"
        user_icon = self.driver.find_element_by_id("com.globo.globotv:id/menu_profile_custom_view_profile")
        user_icon.click()

        # Log out
        try:
            self.driver.implicitly_wait(5)
            logout = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Sair")')
            logout.click()
            # Confirm log out
            yes_btn = self.driver.find_element_by_id('android:id/button1')
            yes_btn.click()
            # Click on te account button
            self.driver.implicitly_wait(10)
            user_icon = self.driver.find_element_by_id("com.globo.globotv:id/menu_profile_custom_view_profile")
            user_icon.click()
        except:
            pass

        self.driver.implicitly_wait(60)
        entrar = self.driver.find_element_by_id('com.globo.globotv:id/activity_profile_text_view_get_int')
        entrar.click()
        self.driver.implicitly_wait(10)
        try:
            none_of_the_above = self.driver.find_element_by_id("com.google.android.gms:id/cancel")
            none_of_the_above.click()
        except:
            pass
        sleep(5)
        self.driver.implicitly_wait(60)
        email_id_tf = self.driver.find_elements_by_class_name('android.widget.EditText')
        email_id_tf.set_value('laurent_headspin')

        # password
        password_tf = self.driver.find_elements_by_class_name('android.widget.EditText')[1]
        password_tf.set_value('Globo@321')

        sleep(10)
        buttons = self.driver.find_elements_by_class_name("android.widget.Button")
        for button in buttons:
            entrar = button.text
            if entrar == "ENTRAR":
                button.click()
                break

        self.status = "Fail_page_load_post_login"
        back_btn = self.driver.find_element_by_android_uiautomator('new UiSelector().description("Navigate up")')
        back_btn.click()
        home_page_load_start = int(round(time.time() * 1000))
        self.driver.implicitly_wait(0.5)
        t_end = time.time() + 60
        while time.time() < t_end:
            try:
                self.driver.find_element_by_class_name('android.widget.ProgressBar')
            except:
                break

        home_page = self.driver.find_element_by_id(
            "com.globo.globotv:id/custom_view_premium_highlights_image_view_background")
        home_page_load_end = int(round(time.time() * 1000))
        self.home_pg_load_time = home_page_load_end - home_page_load_start
        d = {'globo_post_login_home_load_time': self.home_pg_load_time}
        self.kpi_dic.update(d)
        self.pass_count += 1
        print("Home page loading time ", self.home_pg_load_time)

        sleep(4)
        # Choose a title from home page

        screen_size = self.driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']
        swipe_start_x = width / 2
        swipe_start_y = height * 0.7
        swipe_end_x = width / 2
        swipe_end_y = height * 0.3

        self.driver.swipe(swipe_start_x, swipe_start_y, swipe_end_x, swipe_end_y)
        sleep(2)

        title_button = self.driver.find_element_by_id(
            "com.globo.globotv:id/view_holder_custom_view_rails_custom_view_title")
        title_button.click()

        sleep(2)
        title_name = self.driver.find_element_by_id("com.globo.globotv:id/activity_title_text_view_title")
        get_title_name = title_name.text
        print(get_title_name)

        sleep(2)
        play_button = self.driver.find_element_by_id("com.globo.globotv:id/activity_title_button_one")
        play_button.click()
        self.status = "Fail_video_Play"
        video_start = int(round(time.time() * 1000))
        self.driver.implicitly_wait(1)
        t_end = time.time() + 60
        while time.time() < t_end:
            try:
                spinner = self.driver.find_element_by_id('com.globo.globotv:id/progress_bar')
                print("Spinner!!")
            except:
                print("Not displayed")
                break

        self.driver.implicitly_wait(1)
        t_end = time.time() + 60
        while time.time() < t_end:
            try:
                spinner = self.driver.find_element_by_id('com.globo.globotv:id/progress_bar')
                print("Spinner!!")
            except:
                video_end = int(round(time.time() * 1000))
                print("Not displayed")
                break

        self.video_laod_time = video_end - video_start
        print("Video load time ", self.video_laod_time)
        self.pass_count += 1
        d = {'globo_video_load_time': self.video_laod_time}

        self.kpi_dic.update(d)

        # Watch the Video for 1 minute
        self.videoplay_check(80)
        self.driver.implicitly_wait(50)

        navigate_up = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().descriptionContains("Navigate up")')
        navigate_up.click()

        get_title_progress = self.driver.find_element_by_id("com.globo.globotv:id/activity_title_progress").text
        print(get_title_progress)

        sleep(2)
        navigate_up = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().descriptionContains("Navigate up")')
        navigate_up.click()

        # closing and relaunching app
        self.driver.close_app()
        sleep(10)
        self.driver.launch_app()

        # App relaunched
        home_screen = self.driver.find_element_by_id(
            "com.globo.globotv:id/custom_view_premium_highlights_image_view_background")

        # Searching for the same titile
        search_button = self.driver.find_element_by_id("com.globo.globotv:id/menu_bottom_navigation_view_item_search")
        search_button.click()

        search_bar = self.driver.find_element_by_id("com.globo.globotv:id/search_src_text")
        search_bar.click()
        search_bar.send_keys(get_title_name)
        self.driver.press_keycode(66)

        title_select = self.driver.find_element_by_id(
            "com.globo.globotv:id/view_holder_custom_view_rails_custom_view_title")
        title_select.click()

        self.status = "Fail_title_check"

        search_title = self.driver.find_element_by_id("com.globo.globotv:id/activity_title_text_view_title")
        search_title_name = search_title.text
        print(search_title_name)
        if search_title_name == get_title_name:
            print("Title found")
            self.title_check = True
            self.pass_count = self.pass_count + 1

        sleep(2)
        self.status = "Fail_progress_check"

        search_title_progress = self.driver.find_element_by_id("com.globo.globotv:id/activity_title_progress")
        search_title_progress = search_title_progress.text
        print(search_title_progress)
        if search_title_progress == get_title_progress:
            print("Progress time verified")
            self.progress_check = True
            self.pass_count = self.pass_count + 1

        continue_button = self.driver.find_element_by_id("com.globo.globotv:id/activity_title_button_one")
        continue_button.click()

        self.driver.implicitly_wait(1)
        t_end = time.time() + 60
        while time.time() < t_end:
            try:
                spinner = self.driver.find_element_by_id('com.globo.globotv:id/progress_bar')
                print("Spinner!!")
            except:
                print("Not displayed")
                break

        self.driver.implicitly_wait(1)
        t_end = time.time() + 60
        while time.time() < t_end:
            try:
                spinner = self.driver.find_element_by_id('com.globo.globotv:id/progress_bar')
                print("Spinner!!")
            except:
                print("Not displayed")
                break

        print(" Video Resumed ")
        sleep(10)
        self.status = "Pass"


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
