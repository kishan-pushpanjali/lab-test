import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By



from src.Resources.PageObject.locator import Locator


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Locator.test_url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_all_elements_located((By.XPATH,Locator.tab )))

    def testcarouselArticle(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        print("page scrolled till bottom")
        time.sleep(5)
        navi_Button = self.driver.find_elements(By.XPATH,Locator.Button)
        navi_Button[0].click()
        Body = self.driver.find_elements(By.XPATH,Locator.carousel_Body)
        article = self.driver.find_elements(By.XPATH,Locator.article)
        print("no of carousel on display", str(len(Body)))
        index_caro = 0

        print("starting index is of carousel is", index_caro)
        co = 0
        obj_id_list = []

        for elements in Body:
                carousel_count = 1
                print("for carousel no", carousel_count)
                carousel_count = carousel_count + 1
                for obj in article:
                    obj_id = article[co].get_attribute("data-scroll-id")
                    print(co, "indexed article id is :", obj_id)
                    obj_id_list.append(obj_id)
                    self.assertIn(obj_id, obj_id_list, "duplicate objects in carousel")
                    print("checked duplicate, goin to next list of id till now",obj_id_list)
                    print("********************")
                    co = co + 1



        self.assertEqual(co,15,"article count displayed is not equal to 15 as expected")



    def tearDown(self):
        self.driver.quit()

    if  __name__ == "__main__":
        unittest.main()