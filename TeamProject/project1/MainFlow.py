import MemberABC_ as Mdao
from MemberDTO2 import MemberDTO as M
from Bank import Bank as B
from Library import Library as L
from operator import eq

global global_member

def joinMember():

    print("--------------------------------")
    print("----- 회    원    가    입 -----")
    print("--------------------------------")
    user_Id = input("아이디를 입력해주세요 : ")
    user_Pw = input("비밀번호를 입력해주세요 : ")
    user_Name = input("이름을 입력해주세요 : ")
    user_Age = input("나이를 입력해주세요 : ")
    user_Job = input("직업을 입력해주세요 : ")

    Mdao.insertMember(M(user_Id, user_Pw, user_Name, user_Age, user_Job))

    member = M(user_Id, user_Pw, user_Name, user_Age, user_Job)

    print("-----    회원가입 완료!    -----")
    print("--------------------------------")

    global_member = member
    return member

def login(member):
    print("--------------------------------")
    print("-----       로 그 인       -----")
    print("--------------------------------")
    user_Id = input("아이디를 입력해주세요 : ")
    user_Pw = input("비밀번호를 입력해주세요 : ")

    if eq(user_Id, member.getId()):
        if eq(user_Pw, member.getPw()):
            return "1"
        else: return 0
    else: return 0

    #member = Mdao.getMember(user_Id, user_Pw)

    #try:
    #    member.getUserInfo()
    #    print("로그인성공!")
    #    myUser_Id = member.getId()
    #    return "1"
    #except AttributeError as e:
    #   print("로그인실패!")
    #    return "0"

def innerFlow(member):

    while True:
        print("------------------------------------")
        print("-----실행할 번호를 입력해주세요-----")
        print("-----1. 은행업무               -----")
        print("-----2. 도서관업무             -----")
        print("-----3. 종료                   -----")
        print("------------------------------------")

        selection2 = input("번호입력 : ")

        if eq(selection2, "1"):
            B.bankSystem(member.getId())
            continue
        elif eq(selection2, "2"):
            L.librarySystem(member.getId())
            continue
        else :
            print("프로그램을 종료합니다. 사용해주셔 감사합니다.")
            break
        
    

def MainFlow():
    while True:
        print("--------------------------------")
        print("-----1. 회원가입           -----")
        print("-----2. 로그인             -----")
        print("-----3. 종료               -----")
        print("--------------------------------")

        selection = input("번호를 입력해주세요 : ")

        

        if selection == "1":
            global_member = joinMember()
            print(global_member.getMemberInfo())
            #joinMember()
            continue
        elif selection == "2":
            output = login(global_member)
            if output == "1":
                print("login success")
                innerFlow(global_member)
            #    inBoard()
            break
        elif output == "0":
            continue
        elif selection == "3":
            print("--------------------------------")
            print("----- 프로그램을 종료합니다-----")
            print("--------------------------------")
            break
MainFlow()
