import unittest
from time import sleep

from android.pages.implement import inicializar_appium


class MyTestCase(unittest.TestCase):


    def tearDown(self):
        self.driver.quit()


    def test_something(self):
        self.assertEqual(True, True)

        inicializar_appium(self)

        self.driver.implicitly_wait(10)
        categorias = self.driver.find_element_by_id("com.globo.globotv:id/menu_bottom_navigation_view_item_categories")

        categorias.click()
        self.driver.implicitly_wait(10)
        categorias_series = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Séries")')
        categorias_series.click()
        self.driver.implicitly_wait(10)
        primeira_serie = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
            ".widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
            "1]/android.view.ViewGroup/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat"
            "/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.view.ViewGroup/androidx"
            ".recyclerview.widget.RecyclerView/android.widget.RelativeLayout["
            "1]/android.view.ViewGroup/android.widget.ImageView")

        primeira_serie.click()

        self.driver.implicitly_wait(10)
        assistir_ou_continuar = self.driver.find_element_by_id("com.globo.globotv:id/activity_title_button_one")

        if assistir_ou_continuar == 'Assista':
            assistir_ou_continuar.click()
            sleep(120)
            self.driver.close_app()
            sleep(10)
            self.driver.launch_app()
            self.driver.implicitly_wait(10)
            categorias = self.driver.find_element_by_id(
                "com.globo.globotv:id/menu_bottom_navigation_view_item_categories")
            categorias.click()
            self.driver.implicitly_wait(10)
            categorias_series = self.driver.find_element_by_android_uiautomator(
                'new UiSelector().textContains("Séries")')
            categorias_series.click()
            self.driver.implicitly_wait(10)
            primeira_serie = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget"
                                                               ".LinearLayout/android.widget.FrameLayout/android"
                                                               ".widget.FrameLayout/android.widget.FrameLayout"
                                                               "/android.view.ViewGroup/android.widget.FrameLayout["
                                                               "1]/android.view.ViewGroup/android.widget.ScrollView"
                                                               "/androidx.appcompat.widget.LinearLayoutCompat"
                                                               "/androidx.recyclerview.widget.RecyclerView/android"
                                                               ".widget.RelativeLayout/android.view.ViewGroup"
                                                               "/androidx.recyclerview.widget.RecyclerView/android"
                                                               ".widget.RelativeLayout["
                                                               "1]/android.view.ViewGroup/android.widget.ImageView")

            self.driver.implicitly_wait(10)
            assistir_ou_continuar = self.driver.find_element_by_id("com.globo.globotv:id/activity_title_button_one")
            temp_final_video = float(
                self.driver.find_element_by_id("com.globo.globotv:id/activity_title_progress").text)

            print(f'Tempo final >>>>>>', {temp_final_video}, type(temp_final_video))

            if temp_final_video > 0:
                print("Continue assistindo funcionou")
            else:
                raise Exception("Continue assistindo quebrou")
        else:
            temp_inicio_video = float(
                self.driver.find_element_by_id("com.globo.globotv:id/activity_title_progress").text)
            print(temp_inicio_video)
            assistir_ou_continuar.click()
            sleep(120)
            self.driver.close_app()
            sleep(10)
            self.driver.launch_app()
            self.driver.implicitly_wait(60)
            categorias = self.driver.find_element_by_id(
                "com.globo.globotv:id/menu_bottom_navigation_view_item_categories")
            categorias.click()
            self.driver.implicitly_wait(10)
            categorias_series = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Séries")')
            categorias_series.click()
            self.driver.implicitly_wait(10)
            primeira_serie = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                ".widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
                "1]/android.view.ViewGroup/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat"
                "/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.view.ViewGroup"
                "/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout["
                "1]/android.view.ViewGroup/android.widget.ImageView")
            primeira_serie.click()

            self.driver.implicitly_wait(20)

            temp_final_video = float(
                self.driver.find_element_by_id("com.globo.globotv:id/activity_title_progress").text)

            print(f'Tempo inicial >>>>>>', {temp_inicio_video}, type(temp_inicio_video))
            print(f'Tempo final >>>>>>', {temp_final_video}, type(temp_final_video))

            if temp_final_video > temp_inicio_video:
                print("Continue assistindo funcionou")
            else:
                raise Exception("O tempo está diferente")


if __name__ == '__main__':
    unittest.main()
