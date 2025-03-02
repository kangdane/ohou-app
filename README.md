# Bucketplace App Automation
오늘의 집 앱의 자동화 테스트를 수행하는 프로젝트입니다.

## 필수 패키지 설치
프로젝트를 실행하기 전에 필요한 Python 패키지를 설치해 주세요.

### 1. Python 환경 설정
Python이 설치되어 있어야 합니다. Python 3.x 버전을 사용해 주세요.

설치가 되어 있지 않다면, [Python 공식 웹사이트](https://www.python.org/downloads/)에서 설치해 주세요.

### 2. 패키지 설치
이 프로젝트에 필요한 모든 패키지는 `requirements.txt`에 명시되어 있습니다. 프로젝트 디렉터리로 이동하여 아래 명령어를 실행하여 필요한 패키지를 설치해 주세요.

```bash
pip install -r requirements.txt
```

### 3. Appium 설치
Appium은 Node.js 기반의 도구이므로, 먼저 Node.js와 npm이 설치되어 있어야 합니다. Node.js를 설치하지 않았다면, [Node.js 공식 웹사이트](https://nodejs.org/)에서 설치해 주세요.

Appium을 글로벌로 설치하려면 아래 명령어를 실행해 주세요.

```bash
npm install -g appium
```

### 4. Android SDK 설치
Appium을 사용하여 Android 디바이스에서 자동화를 실행하려면 Android SDK가 필요합니다. [Android 공식 웹사이트](https://developer.android.com/studio)에서 SDK를 다운로드하고 설치해 주세요.

설치 후, Android 디바이스와의 연결을 위해 adb 명령어가 정상적으로 작동하는지 확인해 주세요.

### 5. config.py 설정  
테스트를 실행하기 전에, `config.py` 파일에서 테스트 계정 정보와 APK 파일 경로를 설정해 주세요.

#### 테스트 계정 정보 설정  
`config.py` 파일을 열어 아래 항목을 자신의 계정 정보로 수정해 주세요.  

```python
O_HOU_ID = "본인의 아이디"
O_HOU_PASSWORD = "본인의 비밀번호"
```

#### APK 파일 경로 설정
테스트할 APK 파일의 경로를 설정해 주세요. APK 파일이 없으면 앱이 설치되지 않습니다.

```python
APK_PATH = "/path/to/your/app.apk"  # 본인의 APK 파일 경로 입력
```
APK 파일이 지정된 경로에 존재하면, 자동으로 앱이 설치됩니다.
파일이 없으면 기존에 설치된 앱을 실행합니다.

## 자동화 실행
모든 패키지와 환경 설정이 완료되면, 이제 자동화 테스트를 실행할 준비가 되었습니다. main.py 파일을 실행하여 테스트를 시작해 주세요.

### 1. Android 디바이스 연결
실제 Android 디바이스를 연결하거나, 에뮬레이터를 실행해야 합니다. 연결된 디바이스가 정상적으로 인식되는지 확인하려면 아래 명령어를 사용해주세요.

```bash
adb devices
```
디바이스가 정상적으로 표시되면 준비 완료 상태입니다.

### 2. 테스트 실행
다음 명령어를 실행하여 테스트를 시작해 주세요.

```bash
python main.py
```
이 명령어는 main.py에서 정의된 자동화 테스트를 실행합니다. 이 코드에서는 로그인과 광고 팝업 처리 등의 동작을 자동으로 수행합니다.

## 프로젝트 구조

```plaintext
ohou_project/
│── config.py            # 설정 정보 (Appium 서버, 앱 정보 등)
│── driver.py            # WebDriver 설정 및 초기화
│── main.py              # 테스트 실행 파일
│── pages/               # 페이지 객체 모델(POM) 관련 파일들
│   ├── ad_popup.py      # 광고 팝업 처리 관련 클래스
│   ├── base_page.py     # 기본 페이지 클래스 (공통 동작 정의)
│   └── login_page.py    # 로그인 페이지 관련 동작 정의
│── tests/               # 실제 테스트 파일들
│   └── test_login.py    # 로그인 테스트 (예시)
│── utils/               # 공통 함수들 및 유틸리티들
│   └── appium_server.py # Appium 서버 실행/종료 유틸리티 (예: server start/stop 자동화)
│── .gitignore           # Git 무시 파일
│── requirements.txt     # 필수 라이브러리 목록
```

## 문제 해결
Appium 서버가 시작되지 않음: Appium이 정상적으로 설치되었는지 확인하고, npm install -g appium으로 최신 버전을 설치해 주세요.
디바이스 연결 문제: adb devices 명령어로 연결된 디바이스가 확인되지 않는다면, Android SDK 설치가 제대로 되었는지, adb 경로가 제대로 설정되었는지 다시 확인해 주세요.
