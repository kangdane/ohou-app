from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 요소 클릭
    def click(self, by, value):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
        except Exception as e:
            print(f"요소를 클릭할 수 없습니다: {value}")
    
    # 텍스트 입력
    def send_keys(self, by, value, text):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((by, value))
            )
            element.send_keys(text)
        except Exception as e:
            print(f"요소에 텍스트를 입력할 수 없습니다: {value}")
