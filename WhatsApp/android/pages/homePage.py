
from selenium.webdriver.common.by import By
from Working.base_page import BasePage


class Locator(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.init_maps()

    def init_maps(self):
        self.MENU_CATEGORIA =                     (By.ID, "com.globo.globotv:id/menu_bottom_navigation_view_item_categories")
        self.watching_title =                     (By.ID, 'new UiSelector().textContains("Continue assistindo")')
        self.POSTER =                             (By.ID, "com.globo.globotv:id/custom_view_continue_watching_image_view_poster")
        self.MENU_PERFIL =                        (By.ID, "com.globo.globotv:id/custom_view_profile_image_view_picture")
        self.MINHA_LISTA =                        (By.ID, 'new UiSelector().textContains("Minha lista")')
        self.ASSERT_MINHA_LISTA_VAZIA =           (By.ID, "com.globo.globotv:id/custom_view_empty_state_text_view_title")
        self.ASSERT_ITEM_ADICIONADO_MINHA_LISTA = (By.ID, "com.globo.globotv:id/activity_title_button_two")
        self.ASSERT_DOWNLOAD_CONCLUIDO =          (By.ID, "com.globo.globotv:id/custom_view_download_status_image_view_icon")
        self.PRIMEIRO_ITEM_MINHA_LISTA =          (By.ID, "com.globo.globotv:id/custom_view_title_image_view_poster")
        self.ADICIONA_REMOVER_ITEM_MINHA_LISTA =  (By.ID, "com.globo.globotv:id/activity_title_button_two")
        self.NAVEGAR_VOLTAR =                     (By.XPATH, "//android.widget.ImageButton[@content-desc='Navegar para cima']")
        self.BANNER_DESTAQUE =                    (By.ID, "com.globo.globotv:id/custom_view_premium_highlights_image_view_background")
        self.TRILHO_CONTINUE_ASSISTINDO =         (By.ID, 'new UiSelector().textContains("Continue assistindo")')
        self.TRILHO_MINHA_LISTA =                 (By.ID, 'new UiSelector().textContains("Minha lista")')
        self.MENU_DOWNLOAD =                      (By.ID, "com.globo.globotv:id/menu_bottom_navigation_view_item_downloads")
        self.MENU_INICIO =                        (By.ID, "com.globo.globotv:id/menu_bottom_navigation_view_item_home")
        self.ASSERT_LISTA_DOWNLOAD_VAZIA =        (By.ID, "com.globo.globotv:id/custom_view_empty_state_image_view_icon")
        self.ASSERT_DOWNLOAD_EM_ANDAMENTO =       (By.ID, 'com.globo.globotv:id/view_holder_download_title_text_view_downloading')
        self.SELECIONAR_ITENS_DOWNLOAD =          (By.ID, "com.globo.globotv:id/menu_downloads_item_edit")
        self.PRIMEIRO_ITEM_LISTA_DOWNLOAD =       (By.ID, "com.globo.globotv:id/view_holder_download_title_content_root")
        self.APAGAR_DOWNLOAD =                    (By.ID, "com.globo.globotv:id/snackbar_action")
        self.PRIMEIRO_ITEM_CATEGORIA_NOVELA =     (By.ID, "com.globo.globotv:id/custom_view_title_image_view_poster")
        self.CATEGORIA_NOVELA =                   (By.ID, 'new UiSelector().textContains("Novelas")')
        self.ICONE_DOWNLOAD_LISTA_CAPITULO =      (By.ID, "custom_view_video_custom_view_download_status")

    def assert_item_adicionado_minha_lista(self):
        self.driver.implicitly_wait(30)
        item_adicionado_minha_lista = self.driver.find_element_by_id(self.ASSERT_ITEM_ADICIONADO_MINHA_LISTA[1])
        if item_adicionado_minha_lista.text == "Adicionado":
            print(">>>>>>>>>", item_adicionado_minha_lista.text )
        else:
            raise Exception("O minha lista não foi salvo ao reiniciar o APP")

    def click_primeiro_item_lista_download(self):
        self.driver.implicitly_wait(30)
        primeiro_item_lista_download = self.driver.find_element_by_id(self.PRIMEIRO_ITEM_LISTA_DOWNLOAD[1])
        primeiro_item_lista_download.click()

    def click_icone_download_lista_capitulo(self):
        self.driver.implicitly_wait(30)
        icone_download_lista_capitulo = self.driver.find_element_by_id(self.ICONE_DOWNLOAD_LISTA_CAPITULO[1])
        icone_download_lista_capitulo.click()

    def click_primeiro_item_categoria_novela(self):
        self.driver.implicitly_wait(30)
        primeiro_item_categoria_novela = self.driver.find_element_by_id(self.PRIMEIRO_ITEM_CATEGORIA_NOVELA[1])
        primeiro_item_categoria_novela.click()


    def click_categoria_novela(self):
        self.driver.implicitly_wait(30)
        categoria_novela = self.driver.find_element_by_android_uiautomator(self.CATEGORIA_NOVELA[1])
        categoria_novela.click()

    def click_apagar_download(self):
        self.driver.implicitly_wait(30)
        apagar_download = self.driver.find_element_by_id(self.APAGAR_DOWNLOAD[1])
        apagar_download.click()


    def click_selecionar_itens_downlaod(self):
        self.driver.implicitly_wait(30)
        selecionar_itens_download = self.driver.find_element_by_id(self.SELECIONAR_ITENS_DOWNLOAD[1])
        selecionar_itens_download.click()

    def click_banner_destaque(self):
        self.driver.implicitly_wait(30)
        banner_destaque = self.driver.find_element_by_id(self.BANNER_DESTAQUE[1])
        banner_destaque.click()


    def click_adicionar_remover_item_minha_lista(self):
        self.driver.implicitly_wait(30)
        adicionar_remover_item_minha_lista = self.driver.find_element_by_id(self.ADICIONA_REMOVER_ITEM_MINHA_LISTA[1])
        adicionar_remover_item_minha_lista.click()



    def click_primeiro_item_minha_lista(self):
        self.driver.implicitly_wait(30)
        click_primeiro_item_minha_lista = self.driver.find_element_by_id(self.PRIMEIRO_ITEM_MINHA_LISTA[1])
        click_primeiro_item_minha_lista.click()

    def click_menu_download(self):
        self.driver.implicitly_wait(30)
        click_menu_download = self.driver.find_element_by_id(self.MENU_DOWNLOAD[1])
        click_menu_download.click()

    def click_menu_inicio(self):
        self.driver.implicitly_wait(30)
        menu_inicio = self.driver.find_element_by_id(self.MENU_INICIO[1])
        menu_inicio.click()


    def click_menu_categorias(self):
        self.driver.implicitly_wait(30)
        menu_categorias = self.driver.find_element_by_id(self.MENU_CATEGORIA[1])
        menu_categorias.click()

    def assistir_titulo(self):
        assistir_titulo = self.driver.find_element_by_android_uiautomator(self.watching_title[1])

    def trilho_continue_assistindo(self):
        continue_assistindo = self.driver.find_element_by_android_uiautomator(self.TRILHO_CONTINUE_ASSISTINDO[1])

    def trilho_minha_lista(self):
        minha_lista = self.driver.find_element_by_android_uiautomator(self.TRILHO_MINHA_LISTA[1])

    def poster(self):
        poster = self.driver.find_element_by_id(self.POSTER[1]).click()

    def click_menu_perfil(self):
        self.driver.implicitly_wait(30)
        menu_perfil = self.driver.find_element_by_id(self.MENU_PERFIL[1])
        menu_perfil.click()

    def click_minha_lista(self):
        self.driver.implicitly_wait(30)
        minha_lista = self.driver.find_element_by_android_uiautomator(self.MINHA_LISTA[1]).click()

    def assert_minha_lista_vazia(self):
        self.driver.implicitly_wait(30)
        assert_minha_lista_vazia = self.driver.find_element_by_id(self.ASSERT_MINHA_LISTA_VAZIA[1])

    def assert_download_em_andamento(self):
        self.driver.implicitly_wait(30)
        download_em_andamento = self.driver.find_element_by_id(self.ASSERT_DOWNLOAD_EM_ANDAMENTO[1])


    def assert_lista_download_vazio(self):
        self.driver.implicitly_wait(30)
        assert_lista_download_vazio = self.driver.find_element_by_id(self.ASSERT_LISTA_DOWNLOAD_VAZIA[1])

    def assert_download_concluido(self):
        self.driver.implicitly_wait(30)
        assert_download_concluido = self.driver.find_element_by_id(self.ASSERT_DOWNLOAD_CONCLUIDO[1])


    def click_navegar_voltar(self):
        self.driver.implicitly_wait(30)
        navegar_voltar = self.driver.find_element_by_xpath(self.NAVEGAR_VOLTAR[1])
        navegar_voltar.click()
