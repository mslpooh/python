#MemberABC 를 상속

import MySQL_DB as DB
import MemberABC
class MemberABC_(MemberABC):
	def getMember(self, member_Id, member_Pw): ##로그인시 멤버 정보를 담은 객채를
		con, cur = DB.connectDB()
		query = "select * from userInfo where member_Id = '{}' and member_Pw = '{}'".format(member_Id, member_Pw)
		cur.execute(query)
		member = []
		for result in cur:
			member.append(result[0])
			member.append(result[1])
			member.append(result[2])
			member.append(result[3])
			member.append(result[4])
		DB.disconnectDB()
		return member

	def idCheck(self, member_Id): ##회원가입시 아이디 중복 체크
		return 'false'
##return values는 boolean(현재 아이디가 있을시 false / 현재 아이디가 없을시 True), parameter는 String형식



	def insertMember(self, member): #아이디 중복체크에서 성공하고 모든 정보가 다 있을 시 사용되는 메서드
#return values는 x, parameter는 MemberDTO형식
		con, cur = DB.connectDB()
		query = "insert into userInfo values'{%s,%s,%s,%s,%s}'"
		cur.execute(query, (member[0], member[1], member[2], member[3], member[4]))
		DB.disconnectDB()
