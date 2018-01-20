class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def name_(self):
        return self.name

    def age_(self):
        return self.age

    def gender_(self):
        return self.gender


def main():
    while True:
        print()
        print("회원 관리 프로그램입니다.(1. 회원 등록 2. 회원 정보 3. 종료)")
        ans = int(input("번호를 입력해주세요: "))
        
        if ans == 1:
            f = open("person.txt",'a')
            p = Person(input("이름: "), input("나이: "), input("성별: "))
            f.write("이름: " + p.name_() + ", 나이: " + p.age_() + ", 성별: " +p.gender_() +"\n")
            f.close()
            continue

        elif ans == 2:
            f = open("person.txt",'r')
            while True:
                line = f.readline()
                if not line: break
                print(line)
            f.close()
            continue

        elif ans == 3:
            print("종료")
            break

