import re
import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get("https://www.discourse.org/")

menu_demo = driver.find_element_by_xpath("//body/nav[@id='main']/ul/li[4]/a[1]")
menu_demo.click()
driver.implicitly_wait(5)
driver.switch_to.window(driver.window_handles[1])

# ------------------------------------------

print("---------------- Quantos items por categoria --------------------")
al_categ = driver.find_element_by_xpath("//div[@id='ember21']").click()

category_parent = driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[2]/div[3]/div[1]/section[1]/ol[1]/li[1]/div[2]/ul[2]")
for li in category_parent.find_elements_by_tag_name("li"):
    try:
        name_categ = li.find_element_by_class_name("category-name")
        qtd_itens = li.find_element_by_class_name("topic-count")

        print("A categoria", name_categ.text, "possui", qtd_itens.text, "itens.")
    except:
        pass

al_categ = driver.find_element_by_xpath("//div[@id='ember21']").click()

# ---------------------------------------------------------

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# ------------------------------------

print("\n----------------Relação de tópicos fechados--------------------")
el = driver.find_elements_by_class_name("closed")
for x in el:
    try:
        a = x.find_element_by_class_name("title")
        print(a.text)
    except:
        pass


# ------------------------------------

maior = 0

tbody = driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[2]/div[5]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]")
for tr in tbody.find_elements_by_tag_name("tr"):
    try:

        nome_view = tr.find_element_by_class_name("title")
        view = tr.find_element_by_class_name("views").find_element_by_class_name("number").get_attribute("title")
        view = re.sub('[^0-9]', '', view)
        if int(view) > maior:
            maior = int(view)
            nome_maior_view= nome_view.text


    except:
        pass

print("\n--------------------Tópico com maior número de views------------")
print("O tópico,", nome_maior_view, "possui" ,maior, "de visualizações")