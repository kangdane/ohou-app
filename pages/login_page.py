from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_LOGIN_BUTTON = (By.ID, "net.bucketplace:id/emailLogInText") 
    EMAIL_INPUT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.AutoCompleteTextView")
    PASSWORD_INPUT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.view.ViewGroup/android.widget.AutoCompleteTextView")
    LOGIN_BUTTON = (By.ID, "net.bucketplace:id/loginButton")

    def login(self, email, password):
        # 이메일로 로그인 버튼 클릭
        self.click(*self.EMAIL_LOGIN_BUTTON)
        
        # 이메일과 비밀번호 입력
        self.send_keys(*self.EMAIL_INPUT, email)
        self.send_keys(*self.PASSWORD_INPUT, password)
        
        # 로그인 버튼 클릭
        self.click(*self.LOGIN_BUTTON)