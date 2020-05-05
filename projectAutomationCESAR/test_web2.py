from time import sleep
from selenium import webdriver


driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()
driver.get("http://www.trivago.com.br")

# ------------------------------------------


pesquisar_acomodacao = driver.find_element_by_xpath("//input[@id='querytext']").send_keys("Natal")
sleep(2)
opcao_acomodacao = driver.find_element_by_xpath("//button[@class='dealform-button dealform-button--guests js-dealform-button-guests']").click()
sleep(2)
individual_acomodacao = driver.find_element_by_xpath("//li[1]//button[1]//div[1]").click()
sleep(2)
buscar_acomodacao = driver.find_element_by_xpath("//button[@class='btn btn--primary btn--regular search-button js-search-button']").click()
driver.implicitly_wait(20)
buscar_acomodacao = driver.find_element_by_xpath("//option[contains(text(),'Somente distância')]").click()

# ---------------------------------------------------

print("Informações do hotel desejado")
detalhe_segundo_item = driver.find_element_by_xpath("(//span[contains(@class,'item-link name__copytext')])[2]").click()
exibir_info= driver.find_element_by_xpath("(//button[@class='tabs__label'][contains(.,'Info')])[1]").click()
sleep(2)
exibir_comodidades = driver.find_element_by_xpath("(//button[contains(@class,'link')])[2]").click()
nome_segundo_item = driver.find_element_by_xpath("(//span[@class='item-link name__copytext'])[2]").text
oferta_empresa= driver.find_element_by_xpath("(//span[@data-qa='recommended-price-partner'])[2]").text
valor_oferta= driver.find_element_by_xpath("(//strong[@data-qa='recommended-price'])[2]").text
try:
    estrelas= driver.find_element_by_xpath("/html[1]/body[1]/div[4]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/ol[1]/li[4]/article[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/meta[1]").get_attribute("content")
    print(">>>",estrelas)
    qtd_estrelas= estrelas
except:
    qtd_estrelas = "não informado"

print("Nome: ", nome_segundo_item, "Estelas: ",qtd_estrelas)
print("Oferta da empresa: ", oferta_empresa, "-  Preço: ", valor_oferta)
print("Comodidades do quarto: ")
sleep(2)
comod_parent = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/ol[1]/li[2]/article[1]/div[2]/div[1]/div[2]/div[1]/section[1]/div[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[2]/ul[1]")
for x in comod_parent.find_elements_by_tag_name("li"):
	try:
 		print(">", x.text)
	except:
		pass