#BankDAO 상속
import MySQL_DB as DB

class BankDAO_(BankDAO):
	def getMyList():
		con, cur = DB.connectDB()
		query = "select * from bank".format()
		cur.execute(query)
		bank = []
		for result in cur:
			bank.append(result[0])
			bank.append(result[1])
			bank.append(result[2])
			bank.append(result[3])
			bank.append(result[4])
		DB.disconnectDB()
		return bank
        raise NotImplementedError() 
	
