import os
import subprocess
import time
from appium import webdriver
from config import APPIUM_SERVER_URL, CAPABILITIES, APK_PATH, APP_PACKAGE

def get_driver():
    # Appium 서버 실행
    appium_process = subprocess.Popen("appium -p 5002", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)  # 서버가 시작될 때까지 대기
    print("Appium 서버가 시작되었습니다.")

    # WebDriver 연결
    wd = webdriver.Remote(APPIUM_SERVER_URL, CAPABILITIES)

    # APK 파일이 존재하면 설치 확인 후 진행
    if os.path.exists(APK_PATH):
        if not wd.is_app_installed(APP_PACKAGE):  # 앱이 설치되어 있는지 확인
            print("APK를 설치합니다...")
            wd.install_app(APK_PATH)
        else:
            print("앱이 이미 설치되어 있습니다.")
    else:
        print("APK 파일이 존재하지 않으므로 기존 앱을 실행합니다.")

    wd.implicitly_wait(10)
    return wd, appium_process

def stop_driver(wd, process):
    wd.quit()
    process.terminate()
    print("Appium 서버가 종료되었습니다.")
