class Member:
    def __init__(self, user_id, user_pw, name, age, birth, gender):
        self.user_id = user_id
        self.user_pw = user_pw
        self.name = name
        self.age = age
        self.birth = birth
        self.gender = gender

    def getId(self):
        return self.user_id

    def getPw(self):
        return self.user_pw

    def getName(self):
        return self.name

    def getBirth(self):
        return self.birth

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def printMemberInfo(self):
        print("--------회원정보--------")
        print("아이디 : {}".format(self.user_id))
        print("비밀번호 : {}".format(self.user_pw))
        print("이름 : {}".format(self.name))
        print("나이 : {}".format(self.age))
        print("주민번호 앞6자리 : {}".format(self.birth))
        print("성별 : {}".format(self.gender))
        print("------------------------")
