# 05. 파일 쓰기
# with open('new_file.txt','w') as f:
#     f.write("Hello world!\n")
#     f.write("My name is SH.\n")
    # 마지막에 작성한 글이 기존 파일을 덮어 쓰게 된다.
    # 그렇다면? 덮어 쓰지말고 추가를 하고 싶다면????

    # 위의 코드 대신 아래의 코드 사용
with open('new_file.txt','a') as f:
    f.write("Hello world!\n")
    f.write("My name is SH.\n")
        # 이때 'w' 대신에 'a'를 사용한다.
        # a는 append의 줄임말로 추가하는 기능을 한다고 보면 된다!
        # 첫 파라미터의 파일의 이름이 있으면 그 위에 추가하고, 없으면 파일을 만들어서 생성한다.