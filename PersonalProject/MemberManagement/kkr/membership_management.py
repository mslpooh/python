# 회원관리 프로그램

class Member:                                                       # Member 클래스 : 이름, 번호, 학과 정보있는 한명 회원 정보 담는 클래스
    def __init__(self, name, number, department):
        self.name = name
        self.number = number
        self.department = department

def Menu():                                                         # Menu() : 메뉴화면 보여주는 함수
    while True:
        print("===============================================")
        print("  1.추가\n  2.보기\n  3.삭제\n  4.종료")
        print("===============================================")
        n = int(input("수행할 번호를 입력하세요: "))
        if(n == 1):
            add()
        elif(n == 2):
            show()
        elif(n == 3):
            remove()
        elif(n == 4):
            print("종료합니다.")
            break
        else:
            print("잘못 입력하셨습니다.")
            continue

def add():                                                          # add() : 회원 추가하는 함수
    print("===================<추가>====================")
    name = input("이름을 입력하세요: ")
    number = input("학번을 입력하세요: ")
    department = input("학과를 입력하세요: ")

    memberDic = {}                                    # memberDic = {'이름': '이름     학번'}형태인 사전
    try:
        f = open("memberlist.txt", 'r')                                 # memberlist.txt를 '읽기기능'으로 열어줌.
        for line in f:                                                  # line : f파일의 한 줄 받아옴
            if(line[0:3] == name) :
                print("이미 있는 회원입니다.")                          # 파일에서 읽어와 이미 있는 회원이면 추가 안함.
                f.close()
                return
        f.close()
    except:
        print("")
        
    
    
    f = open("memberlist.txt", 'a')                                 # memberlist.txt를 '추가기능'으로 열어줌.
    
    a = Member(name, number, department)                            # a = 추가할 한명 회원
    f.write("{0:10s}{1:15s}{2:10s}\n".format(a.name, a.number, a.department))
    f.close()
    print("<추가완료>")
    
def show():                                                         # show() : 회원 보여주는 함수
    print("===================<보기>====================")
    print("{0:10s}{1:15s}{2:10s}\n".format("이름","학번","학과"))
    f = open("memberlist.txt", 'r')                                 # memberlist.txt를 '읽기기능'으로 열어줌.
    for line in f:                                                  # line : f파일의 한 줄 받아옴
        print(line, end='')
    f.close()

def remove():
    print("===================<삭제>=====================")
    name = input("삭제할 회원의 이름을 입력하세요: ")                 # name : 삭제할 회원 이름

    memberDic = {}                                    # memberDic = {'이름': '이름     학번'}형태인 사전
    f = open("memberlist.txt",'r')
    for line in f:
        memberDic[line[0:3]] = line                   # line = "고강련    2016301002", line[0:3] = "고강련"

    f.close()                                         # 파일을 'w'모드로 열기위해 닫아줌.

    f = open("memberlist.txt",'w')
    for k,v in memberDic.items():
        print("키값 k=",k)
        if(k == name) :                              #삭제할 회원만 입력 안함
            print("<삭제완료>")
            continue
        f.write(v)

    f.close()
    
            
    
