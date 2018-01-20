from MemberClass import Member
from operator import eq


def memberManagement():

    while True:
        print("--------------------------------------------------")
        print("-----안녕하세요 회원관리 프로그램입니다      -----")
        print("-----실행하실 번호를 누르고 앤터를 눌러주세요-----")
        print("-----1.회원등록                              -----")
        print("-----2.회원정보출력                          -----")
        print("-----3.프로그램 종료                         -----")
        print("--------------------------------------------------")
        
        selection = int(input("번호를 입력해주세요 : "))

        if selection == 1:
            addMember()
            continue
        elif selection == 2:
            showMember()
            continue
        else:
            print("--------------------------------------------------")
            print("-----프로그램을 이용해주셔서 감사합니다.     -----")
            print("--------------------------------------------------")
            break

        
def addMember():

    print("--------------------------------------------------")
    print("-----등록하실 회원님의 정보를 입력해주세요  ------")

    member = Member(input("아이디 : "), input("비밀번호 : "), input("이름 : "), int(input("나이 : ")),
                    int(input("주민번호 앞6자리 : ")), input("성별(남/여) : "))

    with open("c:/PythonTest/Memberinfo.txt", "r+") as f:


        user_id = member.getId()
        user_pw = member.getPw()
        name = member.getName()
        age = str(member.getAge())
        birth = str(member.getBirth())
        gender = member.getGender()
            
        inputData = user_id + "/" + user_pw + "/" +name + "/" + age + "/" + birth + "/"  + gender + "\n"

        
        lines = f.readlines()

        print(lines)

        if not lines:
            for line in lines:
                if eq(line, inputData):
                    print("이미 있는 회원입니다.")
                    f.close
                    return

        f.write(inputData)

        print("--------------------------------------------------")
        print("-----회원 등록이 완료되었습니다.             -----")
        print("--------------------------------------------------")

def showMember():
    print("--------------------------------------------------")
    print("-----아이디와 비밀번호를 입력해주세요       ------")

    user_id = input("아이디 : ")
    user_pw = input("비밀번호 : ")

    with open("c:/PythonTest/Memberinfo.txt", "r+") as f:

        while True:
            line = f.readline()
            if not line: break
            str_list = line.split("/")

            if eq(user_id, str_list[0]):
                  if eq(user_pw, str_list[1]):
                        member = Member(str_list[0], str_list[1], str_list[2], int(str_list[3]), int(str_list[4]), str_list[5])
                        member.printMemberInfo()
                        return
            else:
                  continue

        print("존재하지 않는 회원입니다.")
