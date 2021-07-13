try:
    f = open('IOT-embeded2-RasberryPi/data/readme.txt',mode='r',encoding='utf-8')# 텍스트 파일 오픈

    line=f.read()#readline()
    while line:
        print(line)
        line=f.read()
    f.close() # 파일 닫기

except FileNotFoundError as e:
    print('파일 경로가 틀렸는데여 : {0}'.format(e))

#예외는 실행중에 발생한 오류를 의미한다.