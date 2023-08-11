# 3.문자열 처리_ 3.1 문자열
sentence = '나는 소년입니다.'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

#3. 문자열 처리_ 3.2 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : "+ jumin[0:2]) # 0부터 2 직전까지 (0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " +jumin[:6]) #처음부터 6 직전까지
print("뒤 7자리 : " +jumin[7:])
print("뒤 7자리 (뒤에서부터):" +jumin[-7:]) 
# 맨 뒤에서 7번째부터 끝까지 (-를 붙일때는 -1부터 시작한다.주의:0아님)



#3. 문자열 처리_ 3.3 문자열처리함수
python = "Python is Amazing"
print(python.lower()) #모두 소문자

print(python.upper()) #모두 대문자

print(python[0].isupper()) #파이썬의 []안 문자가 대문자 인지?T/F

print(len(python)) #공백도 포함

print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n" , index +1) #처음 인덱스값 말고 다른 위치에서 찾고 싶을 때
print(index) #출력: 15

print(python.find("Java"))   #find로 찾을 경우에는 없으면 -1 반환
#print(python.index("Java")) #index로 찾을 경우에는 오류로 반환
##-> 그러면서 뒤에 문장을 오류로 인해 출력하지 못한다. 
print("hi")

print(python.count("n")) #출력: 2

#3. 문자열 처리_ 3.4 문자열포맷

#방법1
print("나는 %d살입니다." %20)           #d는 정수를 의미한다.
print("나는 %s를 좋아해요." %"파이썬")   #문자열이라 "" 필요하다.
print("Apple은 %c로 시작해요" %"A")     #c는 캐릭터락 한 글자만 받겠다는 의미이다.
# %s
print("나는 %s살입니다." %20)
print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간"))

#방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간")) #인덱스 값에 해당하는 값을 출력해주는 format

#방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

#방법4
age=20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#3. 문자열 처리_ 3.5 탈출문자
# \n: 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
print("저는 '나도코딩' 입니다.")
print("저는 \"나도코딩\"입니다.")

# \\ : 문장내에서\
print("c:\\Users\\nekoi\\Ondrive")

# \r :커서를 맨 앞으로 이동
print("Red Apple\rPi") #출력: Pid Apple

# \b : 백스페이스 ( 한 글자 삭제 )
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

#3. 문자열 처리_ 3.6 퀴즈3
#사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.
url = "http://naver.com"
my_str = url.replace("http://", "") #규칙1번(http제외)
print(my_str)

my_str = my_str[:my_str.index(".")] #규칙2번(.이후제외)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) +"!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))
