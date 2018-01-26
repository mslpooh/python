# BankDTO : 입금, 출금, 저장 값, 입출금날짜(입금날짜, 출금날짜)
#           put,  out,  balance, put_date, out_date

import datetime as Date
class Book:
    def __init__(self, put, out, balance, put_date, out_date):
        self.put = put
        self.out = out
        self.balance = balance
        self.put_date = Date.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.out_date = Date.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def getPut(self):
        return self.put
    def setPut(self, put):
        self.put = put

    def getOut(self):
        return self.out
    def setOut(self, out):
        self.out = out

    def getBalance(self):
        return self.balance 
    def setBalance(self, balance):
        self.balance = balance

    def getPut_date(self):
        return self.put_date
    def setPut_date(self, put_date):
        self.put_date = Date.datetime.now()

    def getOut_date(self):
        return self.out_date
    def setOut_date(self, out_date):
        self.out_date = Date.datetime.now()

