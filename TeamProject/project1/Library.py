
#   - 전체 도서 목록보기(도서명, 출판사, 출판년도, 대출여부(대출자, 대출날짜, 반납날짜))
#   - 내 도서 목록보기(도서명, 출판사, 출판년도, 대출날짜, 반납날짜)
#   - 도서 대출하기(대출할 도서 검색(있음/없음), 있음-대출가능여부 확인(대출가능/불가능))
#   - 도서 반납하기(반납할 도서가 없음/있음)

import sys
from LibraryABC import LibraryABC
from BookListDAO_ import BookListDAO_ as Bdao

# 전체 도서 목록 보기
def showAllList():
    bookAllList = Bdao.getAllBookList()     # BookListDAO : BookListDTO리스트 getAllBookList() = BookListDTO의 BookList클래스 리스트 리턴해줌.    
    print("=============================================================")        
    print("----------전체도서 목록보기-----------\n")
    print("{0:15s}{1:10s}{2:10s}{3:5s}".format("도서명","출판사","출판년도","대출여부"))
    print("-------------------------------------------------------------")
    for book in bookAllList:                # book = Book객체 가지는 객체가 됨. bookAllList = 저거 여러개
        print("{0:10s}{1:10s}{2:14s}".format(book.book_Name, book.book_Publisher, book.book_Year),end="")
        if(book.isBorrow == "0"):
            print("{0:5s}".format("대출가능"))
        elif(book.isBorrow == "1"):
            print("{0:5s}".format("대출중"))
    print("=============================================================")

# 내 도서 목록 보기 
def showMyList(member_Id):
    myBookList = Bdao.getMyBookList(member_Id)
    print("=============================================================")        
    print("----------내 도서 목록보기-----------\n")
    print("{0:15s}{1:10s}{2:10s}{3:10s}{4:10s}{5:10s}".format("도서명","출판사","출판년도","대출자","대출날짜","반납날짜"))
    print("-------------------------------------------------------------")
    for book in myBookList:                # book = Book객체 가지는 객체가 됨. bookAllList = 저거 여러개
        print("{0:10s}{1:10s}{2:14s}{3:10s}{4:15s}{5:10s}".format(book.book_Name, book.book_Publisher, book.book_Year, book.whoBorrow, book.whenBorrow, book.whenReturn))
    print("=============================================================")

# 도서 대출하기
def borrow(member_Id): 
    print("=============================================================")        
    print("------------도서 대출하기------------\n")
    bookName = input("대출할 도서명을 입력해주세요: ")
    print("-------------------------------------------------------------")
    n = Bdao.setBorrow(member_Id, bookName) # BookListDAO에 id랑 책이름 넘어가고, 그것에 대해 대출하는것(실패시 0 리턴, 성공시 1 리턴)
    if(n==1):
        print("\t\t<<< 대출 성공 >>>")
    else:
        print("\t\t<<< 대출 실패 >>>")
    print("=============================================================")

# 도서 반납하기
def returnBook(member_Id):
    print("=============================================================")        
    print("------------도서 반납하기------------\n")
    bookName = input("반납할 도서명을 입력해주세요: ")
    print("-------------------------------------------------------------")
    n = Bdao.setReturn(member_Id, bookName) # BookListDAO에 id랑 책이름 넘어가고, 그것에 대해 반납하는것(실패시 0 리턴, 성공시 1 리턴)
    if(n==1):
        print("\t\t<<< 반납 성공 >>>")
    else:
        print("\t\t<<< 반납 실패 >>>")
    print("=============================================================")

    
class Library(LibraryABC):
    def librarySystem(self, member_Id="testID"):
        while True:
            print("--------------도서관리---------------\n")
            print("  1. 전체 도서 목록 보기")
            print("  2. 내 도서 목록 보기")
            print("  3. 도서 대출하기")
            print("  4. 도서 반납하기")
            print("  5. 메인 화면으로 돌아가기")
            print("  6. 종료\n")
            print("--------------------------------------")
            n = int(input("수행할 작업의 번호를 입력해주세요: "))
        
            if(n == 1):
                showAllList()                            # BookListDTO : book_Name, book_Publisher, book_Year, isBorrow(1=대출중, 0=대출가능)
                                                         # BookListDAO 접근해 getAllBookList : 전체 리스트 접근해 목록 출력
            elif(n == 2):
                showMyList(member_Id)                    # showMyList(member_Id) : 대출자가 id인 사람의 리스트 뽑아옴.
                                                 
            elif(n == 3):
                borrow(member_Id)                        # borrow(member_Id) : 도서 대출하기
        
            elif(n == 4):
                returnBook(member_Id)        # returnBook(member_Id) : 대출자가 id인 사람의 리스트중에 반납할 도서 선택, 반납하기.
        
            elif(n == 5):
                break
    
            elif(n == 6):
                print("\t\t<<< 프로그램을 종료합니다. >>>")
                sys.exit()
        
            else:
                print("\t\t<<< 번호를 잘못 입력하셨습니다. >>>")
    

