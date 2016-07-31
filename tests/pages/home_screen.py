from screen import Screen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomeScreen(Screen):
    def __init__(self, driver):
        super(HomeScreen, self).__init__(driver)

    def wait_page_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ion-log-out"))
        )
