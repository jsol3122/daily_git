import sys
import keyword

print (3+2)
print ("Hello World") #주석 - 따옴표는 종류상관x
print ('-------------------')
print ('-' * 30) # -를 30번 반복해라
print(4 + 5)
print(12 - 32)
print((4 + 5) * 6)
print(4 + 5 * 6)
print(9 / 5)  # 자바와 다르게 정수/정수 상관없이 실수출력 = 자바스크립트문법 따라감
print(9.0 / 5.0)
print(9 / 5.0)
print ('-' * 30) 

print(sys.version)
print()
print(sys.version_info)
print ('-' * 30) 

print(keyword.kwlist) # 파이썬에 지정된 키워드들(=예약어) 확인
print ('-' * 30) 

# 기본 문형
a="123"
print(a, type(a))

b = int(a)
print(b, type(b))
print ('-' * 30) 

# 입력
#name = input('이름 입력 : ')
#age = int(input('나이 입력 : '))
#print (name, ', ', age)
#print (name, end=',')
#print (age)

#print (name, end="\t")
#print (age)
#print ('-' * 30) 

# 이름, 국어, 영어, 수학 점수를 입력받아서 총점 / 평균 구하기
name = input('이름 입력 : ')
kor = int(input('국어 입력 : '))
eng = int(input('영어 입력 : '))
math = int(input('수학 입력 : '))
tot = kor+eng+math
# print('이름','\t','국어','\t','영어','\t','수학','\t','총점','\t','평균') - 잘나옴
# print('이름\t 국어\t 영어\t 수학\t 총점\t 평균') - 이렇게하면 탭간격 깨짐
print('%10s %7s %7s %7s %8s %7s' %('이름','국어','영어','수학','총점','평균')) # 서식문자 이용한 방법
# print(name,'\t',kor,'\t',eng,'\t',math,'\t',tot,'\t',(tot/3)) - 잘나옴
print('%10s %7d %7d %7d %8d %7.2f' %(name, kor, eng, math, tot, tot/3)) # 서식문자 이용한 방법

# 서식 출력
# 서식 문자 : %d %f %s
# 정수형 : %d 혹은 %자릿수d
# 실수형 : %f 혹은 %전체자릿수.소수이하자릿수f
# 문자열 : %s 혹은 %자릿수s

# 여러줄 주석은 ''' 내용 ''' or """ 내용 """ 이렇게 써주면 됨 
# '''와 """는 주석임에 동시에 문자열 역할도 함

str = '''
안녕하세요
반갑습니다
'''
print(str)















