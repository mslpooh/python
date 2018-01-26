#   - 내 입출금 목록 보기
#   - 입금하기
#   - 출금하기


import sys
from BankABC import BankABC
from BankDAO_ import BankDAO_ as Bdao

# 내 입출금 목록 보기 
def showMyList(member_Id):
    myBankList = Bdao.getMyList(member_Id)  #getMyList - DAO에서 내 목록 리스트 반환하는 함수
    print("=============================================================")        
    print("----------입출금 목록-----------\n")
    print("-------------------------------------------------------------")
    for record in myBankList:
        if record.put != 0:
            print("{0:15s}{1:10s}".format("입금","입금날짜"))
            print("{0:10s}{1:10s}".format(record.put, record.put_date))
        elif record.out != 0:
            print("{0:15s}{1:10s}".format("출금","출금날짜"))
            print("{0:10s}{1:10s}".format(record.out, record.out_date))
    print("잔고: " + myBankList.balance)
    print("=============================================================")


# 입금하기
def money_put(member_Id):
    myBankList = Bdao.getMyList(member_Id)
    print("=============================================================")        
    print("------------입금하기------------\n")
    print("잔고: " + myBankList.balance)
    put = input("입금할 돈의 액수: ")
    if put <= 0:
        print("입금할 돈의 액수가 잘못 입력되었습니다.")
    else:
        myBankList.balance += put
        print("입금 성공! 잔고: " + myBankList.balance)
    print("=============================================================")



# 출금하기
def money_out(member_Id):
    myBankList = Bdao.getMyList(member_Id)
    print("=============================================================")        
    print("------------출금하기------------\n")
    print("잔고: " + myBankList.balance)
    out = input("출금할 돈의 액수: ")
    if myBankList.balance == 0:
        print("잔고에 있는 돈이 0원입니다.")
    elif myBankList.balance < myBankList.out:
        print("잔고에 있는 돈이 부족합니다.")
    elif out <= 0:
        print("출금할 돈의 액수가 잘못 입력되었습니다.")
    else:
        myBankList.balance -= out
        print("출금 성공! 잔고: " + myBankList.balance)
    print("=============================================================")


class Bank(BankABC):
    def bankSystem(self, member_Id="testID"):
        while True:
            print("--------------통장관리---------------\n")
            print("  1. 내 입출금 목록 보기")
            print("  2. 입금하기")
            print("  3. 출금하기")
            print("  4. 메인 화면으로 돌아가기")
            print("  5. 종료\n")
            print("--------------------------------------")
            n = int(input("무엇을 수행하시겠습니까?: "))
        
            if(n == 1):
                showMyList(member_Id)
                    
            elif(n == 2):
                money_put(member_Id)
                                                 
            elif(n == 3):
                money_out(member_Id)
                
            elif(n == 4):
                break
    
            elif(n == 5):
                print("\t\t<<< 프로그램을 종료합니다. >>>")
                sys.exit()
        
            else:
                print("\t\t<<< 번호를 잘못 입력하셨습니다. >>>")
