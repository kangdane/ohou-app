import os

# Appium 서버 설정
APPIUM_SERVER_URL = "http://127.0.0.1:5002"

# 디바이스 및 앱 정보
APP_PACKAGE = "net.bucketplace"
APP_ACTIVITY = "se.ohou.screen.splash.SplashActivity"
APK_PATH = "/root" # 설치할 apk 파일의 경로를 설정해 주세요.

CAPABILITIES = {
    "platformName": "Android",
    "automationName": "uiautomator2",
    "deviceName": "Android",
    "appPackage": APP_PACKAGE,
    "appActivity": APP_ACTIVITY,
}

# 테스트 계정 정보
O_HOU_ID = "id" # 본인의 계정 아이디를 입력해 주세요.
O_HOU_PASSWORD = "pw" #본인의 계정 비밀번호를 입력해주세요.
