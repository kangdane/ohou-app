import subprocess
import time

def start_appium():  # Appium 서버 실행
    cmd = "appium -p 5002"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # 서버가 시작되었을 때의 메시지 출력
    while True:
        line = process.stdout.readline()
        if line:
            # Appium이 정상적으로 시작되었을 때의 로그 메시지 확인
            if "Appium REST http interface listener started" in line.decode('utf-8'):
                print("Appium 서버가 시작되었습니다.")
                break
        else:
            break
    
    time.sleep(5)  # 서버가 완전히 시작되도록 잠시 대기
    return process

def stop_appium(process):  # Appium 서버 종료
    process.terminate()
    print("Appium 서버가 종료되었습니다.")
