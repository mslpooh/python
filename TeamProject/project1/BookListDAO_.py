#BookListDAO 상속
import MySQL_DB as DB
import datetime
import BookListDAO

#dao =  BookListDAO_() 
#book = []
#book = dao.getMyBookList
#print(book)
class BookListDAO_(BookListDAO):
	# 전체 목록 리스트 반환
	#def __init__(self):
	#	print('생성')
	def getAllBookList():           # book 데이터베이스에 접근해 각각의 도서명, 출판사, 출판년도, 대출여부, 대출자, 대출일, 반납일 받아와
		con, cur = DB.connectDB()
		query = "select * from book"
		cur.execute(query)
		book = []
		for result in cur: # @@받아온 정보들을 book이란 리스트에 저장 후 리턴
			book.append(result[0])
			book.append(result[1])
			book.append(result[2])
			book.append(result[3])
			book.append(result[4])
			book.append(result[5])
			book.append(result[6])
		DB.disconnectDB()
		return book
        # Book b에 저장 후 리스트(각 원소=BookListDTO의 Book클래스 객체)로 넘기기
                                    # ex) result = [b1, b2, b3,...] 

    # 내 목록 리스트 반환
	def getMyBookList(id):          # 대출자가 id인 리스트 받아와 넘겨주기(getAllBookList와 같은 절차)
		con, cur = DB.connectDB()
		query = "select * from book where id ='{}'".format(id)
		cur.execute(query)
		book = []
		for result in cur:
			book.append(result[0])
			book.append(result[1])
			book.append(result[2])
			book.append(result[3])
			book.append(result[4])
			book.append(result[5])
			book.append(result[6])
		DB.disconnectDB()
		return book
        # return값 = Book객체의 리스트(getAllBookList와 같은 리턴값)

    # 대출하기(성공시 1, 실패시 0리턴)
	def setBorrow(id, bookName):    # 대출 성공시 1리턴, 실패시 0리턴
		con, cur = DB.connectDB()
		now = datetime.now()
		try:
			query = "update book set isBorrow ='{}',whoBorrow ='{}', whenBorrow = '{}', whenReturn = '{}' where book_name = '{}'".format("1", id, now,'' , bookName )
			cur.update(query)
		except Error:
			return 0;
		return 1;
        # 데이터중에 book_Name이 넘어온 bookName을 값으로 가진 리스트 뽑아
                                    # isBorrow="1", whoBorrow=id, whenBorrow=그날 날짜, whenReturn=다음주 날짜로 세팅해주기

    # 반납하기(성공시 1, 실패시 0리턴)                                
	def setReturn(id, bookName):    # 반납 성공시 1리턴, 실패시 0리턴
		con, cur = DB.connectDB()
		now = datetime.now()
		try:
			query = "update book set isBorrow ='{}',whoBorrow ='{}', whenBorrow = '{}', whenReturn = '{}' where book_name = '{}'".format("0", null, "", "", bookName )
			cur.update(query)
		except Error:
			return 0;
		return 1;
        # 데이터중에 book_Name이 넘어온 bookName을 값으로 가진 리스트 뽑아
                                    # isBorrow="0", whoBorrow=""(null), whenBorrow="", whenReturn=""로 세팅해주기

