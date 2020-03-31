import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()