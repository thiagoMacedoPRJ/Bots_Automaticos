from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "___*BOM DIA*___                                                                                        AUTOMATIZADO!!                                                                                     [By: Thiago Macedo!]                                                                                      _       ---------       _                                                                             Próximo Horário as 12:00"
        self.mensage = "___*BOA TARDE*___                                                                                        AUTOMATIZADO!!                                                                                     [By: Thiago Macedo.S!!]                                                                                      _       ---------       _                                                                             Próximo Horário as 18:00"
        self.mensag = "___*BOA NOITE*___                                                                                        AUTOMATIZADO!!                                                                                     [By: BOA NOITE!! Thiago Macedo.S!!]                                                                                      _       ---------       _                                                                             Próximo Horário as 6:00"
       
       
       # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["TesteLegal"]

        options = webdriver.ChromeOptions()

        options.add_argument('lang=pt-br')

        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def EnviarMensagens(self):

        self.driver.get('https://web.whatsapp.com')

        time.sleep(30)




        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            t = True
            while t:
                x = time.localtime()
                horas =  str(x[3])
                minutos = str(x[4])
                segundos = str(x[5])
                campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo_ou_pessoa}']")

                time.sleep(3)

                campo_grupo.click()



                if horas >= '0':
                     #<div tabindex="-1" class="_2A8P4"><div tabindex="-1" class="_1JAUF _2x4bz"><div class="OTBsx" style="visibility: visible;">Digite uma mensagem</div><div class="_2_1wd copyable-text selectable-text" contenteditable="true" data-tab="6" dir="ltr" spellcheck="true"></div></div></div>

                    chat_box = self.driver.find_element_by_class_name('_2A8P4')

                    chat_box.click()

                    chat_box.send_keys(self.mensagem)

                    botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                    time.sleep(3)
                    botao_enviar.click()
                    time.sleep(5)
                    t = False
                else:
                    pass
                    



                
                if horas <= '12':
                    #<div tabindex="-1" class="_2A8P4"><div tabindex="-1" class="_1JAUF _2x4bz"><div class="OTBsx" style="visibility: visible;">Digite uma mensagem</div><div class="_2_1wd copyable-text selectable-text" contenteditable="true" data-tab="6" dir="ltr" spellcheck="true"></div></div></div>
                    chat_box = self.driver.find_element_by_class_name('_2A8P4')
                    chat_box.click()
                    chat_box.send_keys(self.mensage)
                    botao_enviar = self.driver.find_element_by_xpath(
                    "//span[@data-icon='send']")
                    time.sleep(3)
                    botao_enviar.click()
                    time.sleep(5)
                    t = False
                else:
                    pass
    
    
    
                if horas <= '18':
                    #<div tabindex="-1" class="_2A8P4"><div tabindex="-1" class="_1JAUF _2x4bz"><div class="OTBsx" style="visibility: visible;">Digite uma mensagem</div><div class="_2_1wd copyable-text selectable-text" contenteditable="true" data-tab="6" dir="ltr" spellcheck="true"></div></div></div>
                    chat_box = self.driver.find_element_by_class_name('_2A8P4')
                    chat_box.click()
                    chat_box.send_keys(self.mensag)
                    botao_enviar = self.driver.find_element_by_xpath(
                    "//span[@data-icon='send']")
                    time.sleep(3)
                    botao_enviar.click()
                    time.sleep(5)
                    t = False
                else:
                    pass


bot = WhatsappBot()
bot.EnviarMensagens()
