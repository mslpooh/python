# BookListDTO : 도서명,    출판사,         출판년도,  대출여부(대출자, 대출날짜, 반납날짜)
#               book_Name, book_Publisher, book_Year, isBorrow(1:대출중, 0:대출x(대출가능))

# BookListDAO : getAllBookListDTO getBook() : 전체 리스트 받아옴
class Book:
    def __init__(self, book_Name, book_Publisher, book_Year, isBorrow, whoBorrow, whenBorrow, whenReturn):
        self.book_Name = book_Name
        self.book_Publisher = book_Publisher
        self.book_Year = book_Year
        self.isBorrow = isBorrow
        self.whoBorrow = whoBorrow
        self.whenBorrow = whenBorrow
        self.whenReturn = whenReturn

    def getBookName(self):
        return self.book_Name
    def setBookName(self, book_Name):
        self.book_Name = book_Name

    def getBookPublisher(self):
        return self.book_Publisher
    def setBookPublisher(self, book_Publisher):
        self.book_Publisher = book_Publisher

    def getBookYear(self):
        return self.book_Year 
    def setBookYear(self, book_Year):
        self.book_Year = book_Year

    def getIsBorrow(self):
        return self.isBorrow
    def setIsBorrow(self, isBorrow):
        self.isBorrow = isBorrow

    def getWhoBorrow(self):
        return self.whoBorrow
    def setWhoBorrow(self, whoBorrow):
        self.whoBorrow = whoBorrow

    def getWhenBorrow(self):
        return self.whenBorrow
    def setWhenBorrow(self, whenBorrow):
        self.whenBorrow = whenBorrow

    def getWhenReturn(self):
        return self.whenReturn
    def setWhenReturn(self, whenReturn):
        self.whenReturn = whenReturn
