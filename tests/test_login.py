import time
from driver import get_driver
from pages.login_page import LoginPage
from pages.ad_popup import AdPopup
from utils.appium_server import start_appium, stop_appium
from config import OHO_ID, OHO_PASSWORD

# Appium 서버 실행
appium_process = start_appium()

# WebDriver 설정
wd = get_driver()

print("로그인 테스트 시작")

try:
    login_page = LoginPage(wd)
    ad_popup = AdPopup(wd)

    login_page.login(OHO_ID, OHO_PASSWORD)
    ad_popup.close_popup()  # 광고 팝업이 있으면 닫기

    print("로그인 성공")
except Exception as e:
    print("로그인 실패")

time.sleep(5)
wd.quit()
print("로그인 테스트 종료")

# Appium 서버 종료
stop_appium(appium_process)
