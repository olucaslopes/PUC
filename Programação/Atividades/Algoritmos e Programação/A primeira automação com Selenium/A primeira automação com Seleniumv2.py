#Trabalho feito por Emanuel e Lucas

#importando o selenium, o webdriver e o time
from selenium import webdriver
import time
caminho = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(caminho)
driver.get('https://curso-python-selenium.netlify.app/exercicio_01.html')

time.sleep(5)

#encontrando elementos e adicionando-os ao dicionário
chaved1 = driver.find_element_by_tag_name('h1')
p = driver.find_elements_by_tag_name('p')
k1, k2, k3 = p

dic2 = {chaved1.text: {'texto1': k1.text, 'texto2': k2.text, 'texto3':k3.text}}

#fechando o navegador
driver.quit()

print(dic2)