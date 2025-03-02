from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdPopup(BasePage):
    CLOSE_BUTTON = (By.XPATH, '//android.view.View[@content-desc="닫기"]/android.widget.TextView')

    def close_popup(self):
        try:
            self.click(*self.CLOSE_BUTTON)
            print("광고 팝업 닫기 클릭")
        except:
            print("광고 팝업 없음")



