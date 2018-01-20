#학생정보저장 프로그램 만들기

students = []
info = {'이름':'', '학번':'', '학과':''}

while True:
	print("----학생정보저장프로그램----") 
	print("1. 저장")
	print("2. 보기")
	print("4. 종료")
	
	num = input()
	if num == '1':
		print("저장실행")
		info['이름'] = input("이름: ")
		info['학번'] = input("학번: ")
		info['학과'] = input("학과: ")
		with open('stuInfo.txt', 'a') as file_object:
			file_object.write(info['이름'].title())
			file_object.write("\t\t")
			file_object.write(info['학번'].title())
			file_object.write("\t\t")
			file_object.write(info['학과'].title())
			file_object.write("\t\t")
			file_object.write("\n")
			file_object.close()
	elif num == '2':
		print("보기실행")
		with open('stuInfo.txt') as file_object:
			contents = file_object.read()
			print(contents)
			file_object.close()
	elif num == '4':
		print("프로그램 종료")
		break
		
