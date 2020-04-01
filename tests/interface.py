import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
abs_path = os.path.abspath(".")

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_success_login(self):
        driver = self.driver
        driver.get('http://admin:admin@localhost:8080/')
        assert driver.title == "SoftDes 2018.2"

    def test_fail_login(self):
        driver = self.driver
        driver.get('http://admin:batata@localhost:8080/')
        driver.switch_to.alert.dismiss()
        assert driver.title != "SoftDes 2018.2"

    def test_success_pw_change(self):
        driver = self.driver
        driver.get('http://admin:admin@localhost:8080/pass')
        old_pw_input = driver.find_element_by_id('velha').send_keys("admin")
        new_pw_input = driver.find_element_by_id('nova').send_keys("admin")
        confirm_pw_input = driver.find_element_by_id('repeteco').send_keys("admin")
        driver.find_element_by_id("change").click()
        mensagem = driver.find_element_by_id("aviso-senha").text
        assert mensagem == "Senha alterada com sucesso"

    def test_fail_pw_change(self):
        driver = self.driver
        driver.get('http://admin:admin@localhost:8080/pass')
        old_pw_input = driver.find_element_by_id('velha').send_keys("admin")
        new_pw_input = driver.find_element_by_id('nova').send_keys("batata")
        confirm_pw_input = driver.find_element_by_id('repeteco').send_keys("linguiça")
        driver.find_element_by_id("change").click()
        mensagem = driver.find_element_by_id("aviso-senha").text
        assert mensagem == "As novas senhas nao batem"

    def test_submit_success_test(self):
        driver = self.driver
        driver.get('http://admin:admin@localhost:8080/?ID=1')
        file_path = f"{abs_path}/desafio_test1.py"
        driver.find_element_by_id('resposta').send_keys(file_path)
        driver.find_element_by_id('enviar-resposta').click()
        resultado = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//table/tbody/tr[1]/td[3]')))
        assert resultado.text == "OK!"

    def test_submit_failed_test(self):
        driver = self.driver
        driver.get('http://admin:admin@localhost:8080/?ID=1')
        file_path = f"{abs_path}/desafio_test2.py"
        driver.find_element_by_id('resposta').send_keys(file_path)
        driver.find_element_by_id('enviar-resposta').click()
        resultado = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//table/tbody/tr[1]/td[3]')))
        assert resultado.text == "Erro"

    def test_submit_failed_test_with_feedback(self):
        driver = self.driver
        driver.get('http://admin:admin@localhost:8080/?ID=1')
        file_path = f"{abs_path}/desafio_test2.py"
        driver.find_element_by_id('resposta').send_keys(file_path)
        driver.find_element_by_id('enviar-resposta').click()
        resultado = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//table/tbody/tr[1]/td[3]')))
        feedback = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//table/tbody/tr[1]/td[2]')))
        assert resultado.text == "Erro" and feedback.text == "a b c"


    def test_submit_failed_function_with_feedback(self):
        driver = self.driver
        driver.get('http://admin:admin@localhost:8080/?ID=1')
        file_path = f"{abs_path}/desafio_test3.py"
        driver.find_element_by_id('resposta').send_keys(file_path)
        driver.find_element_by_id('enviar-resposta').click()
        resultado = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//table/tbody/tr[1]/td[3]')))
        feedback = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//table/tbody/tr[1]/td[2]')))
        assert resultado.text == "Erro" and feedback.text == "Nome da função inválido. Usar 'def desafio1(...)'"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()