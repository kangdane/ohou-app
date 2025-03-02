import time
from driver import get_driver, stop_driver
from pages.login_page import LoginPage
from pages.ad_popup import AdPopup
from config import O_HOU_ID, O_HOU_PASSWORD

# 드라이버 실행 및 Appium 서버 시작
wd, appium_process = get_driver()
print("자동화 테스트를 시작합니다.")

# 로그인 실행
login_page = LoginPage(wd)
login_page.login(O_HOU_ID, O_HOU_PASSWORD)

# 광고 팝업 닫기 시도
ad_popup = AdPopup(wd)
ad_popup.close_popup()

time.sleep(5)

# 테스트 종료
print("자동화 테스트를 종료합니다.")
stop_driver(wd, appium_process)  # 드라이버 종료 및 Appium 서버 종료
