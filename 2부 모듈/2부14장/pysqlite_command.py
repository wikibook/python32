# -*- coding: cp949 -*-
import sqlite3
import sys
import re

# 데이터베이스 경로 설정 
if len(sys.argv) == 2:
	path = sys.argv[1]
else:
	path = ":memory:"

con = sqlite3.connect(path)
con.isolation_level = None	# 트랜잭션없이 자동 커밋이 되도록 설정
cur = con.cursor()

buffer = ""			# 쿼리 버퍼 

def PrintIntro():
	"프로그램 인트로 메세지"
	print("pysqlite의 command 프로그램입니다.")
	print("특수 명령어를 알고 싶으시면 '.help;'를 입력하세요.")
	print("SQL 구문은 ';'으로 끝나야 합니다.")

def PrintHelp():
	"도움말"
	print(".dump\t\t데이터베이스의 내용을 덤프합니다.")

def SQLDump(con, file=None):
	"데이터베이스 내용 덤프"
	if file != None:
		f = open(file, "w")
	else:
		f = sys.stdout

	for l in con.iterdump():
		f.write("{0}\n".format(l))

	if f != sys.stdout:
		f.close()

PrintIntro()		# 인트로 메세지 출력

while True:
	line = input("pysqlite>> ")		# 명령어 입력
	if buffer == "" and line == "":
		break;
	buffer += line
	
	if sqlite3.complete_statement(buffer):		# ';'으로 구문이 끝나는지 검사
		buffer = buffer.strip()

		if buffer[0]==".":		# 특수 명령어인 경우
			cmd = re.sub('[ ;]', ' ', buffer).split()
			if cmd[0] == '.help':
				PrintHelp()
			elif cmd[0] == '.dump':
				if len(cmd) == 2:
					SQLDump(con, cmd[1])
				else:
					SQLDump(con)
		else:					# 일반 SQL 구문인 경우
			try:
				buffer = buffer.strip()
				cur.execute(buffer)

				if buffer.lstrip().upper().startswith("SELECT"):	# SELECT 질의인 경우
					print(cur.fetchall())
			except sqlite3.Error as e:
				print("Error: ", e.args[0])
			else:
				print("구문이 성공적으로 수행되었습니다.") 
		buffer=""		# 입력 버퍼 초기화
con.close()
print("프로그램을 종료합니다. 야옹~")
