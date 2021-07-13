try:
    f = open('IOT-embeded2-RasberryPi/data/readme.txt',mode='r',encoding='utf-8')# 텍스트 파일 오픈
    f2= open('IOT-embeded2-RasberryPi/data/writeme.txt',mode='w',encoding='utf-8')#작성파일 오픈
    line=f.read()#readline()
    while line:
        print(line)
        f2.wrtie(line)
        line=f.read()
    f2.write("추가내용")
    f.close() # 파일 닫기
    f2.close()

    print('파일 작성 완료')
except Exception as e:
    print('파일 경로가 틀렸는데여 : {0}'.format(e))

#예외는 실행중에 발생한 오류를 의미한다.