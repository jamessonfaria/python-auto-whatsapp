from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

def abrir_navegador():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://web.whatsapp.com/')
    time.sleep(10)

    return driver

def buscar_contato(contato, driver):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    #time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem, driver):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')[1]
    campo_mensagem.click()
    #time.sleep(3)
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)

def enviar_anexo(filepath, driver):
    botao_anexo = driver.find_element_by_xpath('//div[@title="Anexar"]')
    botao_anexo.click()
    
    botao_imagem = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    botao_imagem.send_keys(filepath)

    time.sleep(3)

    div = driver.find_element_by_xpath('//div[@class="_3tSYy"]')
    legenda = div.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')  
    legenda.send_keys("Teste meu amor...... ")

    time.sleep(5)

    botao_enviar = driver.find_element_by_xpath('//span[@data-icon="send"]')
    botao_enviar.click()