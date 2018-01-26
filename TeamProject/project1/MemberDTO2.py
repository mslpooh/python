class MemberDTO:

    def __init__(self, member_Id, member_Pw, member_Name, member_Age, member_Job):
        self.member_Id = member_Id      #String 
        self.member_Pw = member_Pw      #String
        self.member_Name = member_Name  #String
        self.member_Age = member_Age    #String
        self.member_Job = member_Job    #String


    ###################GETTER###################

    def getId(self):
        return self.member_Id
    def getPw(self):
        return self.member_Pw
    def getName(self):
        return self.member_Name
    def getAge(self):
        return self.member_Age
    def getJob(self):
        return self.member_Job

    ###################SETTER###################

    def setId(self, member_Id):
        self.member_Id = member_Id
    def setPw(self, member_Pw):
        self.member_Pw = member_Pw
    def setName(self, member_Name):
        self.member_Name = member_Name
    def setAge(self, member_Age):
        self.member_Age = member_Age
    def setJob(self, member_Job):
        self.member_Job = member_Job

    ###################GetMemberInformation form list ######################

    def getMemberInfo(self):
        return [self.member_Id, self.member_Pw, self.member_Name, self.member_Age, self.member_Job]
