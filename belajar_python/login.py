import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) # buka browser google chrome
        
    def test_verify_success_login_with_email_and_pass_registered(self): # test case
        # steps
        web = self.browser
        web.get("http://barru.pythonanywhere.com") # buka situs
        time.sleep(3)
        web.find_element(By.ID,"email").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        web.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago") # isi password
        time.sleep(1)
        web.find_element(By.CSS_SELECTOR,"input#signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = web.find_element(By.ID, "swal2-title").text  # get teks/tulisan pop up atas
        popup_bawah = web.find_element(By.ID, "swal2-content").text  # get teks/tulisan pop up bawah
        time.sleep(2)

        # validasi
        assert 'Welcome' in popup_atas
        assert popup_bawah == 'Anda Berhasil Login'
        
    def tearDown(self): 
        self.browser.close() 


if __name__ == "__main__": 
    unittest.main()