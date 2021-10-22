# slicing & Indexing
# 0:5는 0번인덱스의 글자부터 5번인덱스 "이전까지"의 글자까지 꺼내오기
a = "Hello Python"
print(a[6:] + ' ' + a[0:5])

# ::-1 은 시작인덱스번호 / 마지막인덱스번호를 생략하였으며 -1로 맨 뒤에서부터 실행하도록 설정한 것
b="Hello"
print(b[::-1])
print('-'*30)

# 리스트(list), 튜플(tuple), 사전(dict)  -- 아주 많이 쓰임
print(type([]))  # 리스트 - 자바의 배열을 확장한 것과 유사한 개념
print(type(()))  # 튜플
print(type({}))  # 사전 - 자바의 map과 유사
print('-'*30)

# 1. list ----------------------------------------------------------------------------------
# 배열과 유사함 (동일x)
L = [1,2,3]
print(type(L))   # type명령어는 자료형 확인하는 것
print('크기 = ',len(L))    # length (=크기,갯수) 구하기
print(L[1])      # index번호는 0번부터 시작임에 주의
print(L[-1])     # -index번호는 -1부터 시작임에 주의
print(L[1:3])    # list안의 여러개의 값을 가져올때는 리스트형태로 [2,3] 과 같이 가져옴에 주의
print()
print(L+L)       # L값과 L값을 결합하여 하나의 리스트값으로 가져옴 (개별리스트 2개 x)
print(L*3)       # L값을 3번 반복
print(L)         # 리스트의 값을 출력할때는 반드시 리스트타입으로 출력됨에 주의 (값만 가져오지X)
print('-'*30)

d={'one':[1,2,3], 'two':(1,2,3), 'three':'set'}  # d라는 dict에 리스트 / 튜플 / 문자열 들어있는것
print(d['two'])  # 자바의 map처럼 이름으로 꺼내오면 그 안의 값을 꺼내옴
print(d['one'])
print(d['three'])
print('-'*30)

k=[1,2,3]
k[1]=10          # list의 값 변경 -- list값은 추가/변경 가능
print(k)
print('-'*30)

# range(n) : 0부터 (n-1)까지 -- 짱짱 많이 쓰임
p = range(10)
print(p)         # p 안에는 range(0, 10) 값이 들어있음
print(list(p))   # list타입으로 찍어야 range안의 모든 값들을 나열해줌
print(list(p)[::-1])  # range안의 모든 값을 역순으로 출력
print(list(p)[::2])   # range안의 모든 값을 2칸씩 띄고 출력 (역순x)
print('-'*30)

# 2. tuple ---------------------------------------------------------------------------------
t=(1,2,3)
print(t)
print('크기 = ', len(t))
print(t[-1])      # -index번호는 -1부터 시작
print(t+t+t)      # 내부의 값이 결합되어 하나의 튜플 안에 담긴 형태로 출력
print(t*3)        # 반복 (개별튜플x / 하나의 튜플로 묶여서 출력)
print(4 in t)     # t 내부(in)에 4가 존재하는지 여부를 True/False 로 출력 -- 많이 쓰임
print()

# 값(요소)이 1개인 튜플의 경우 
s = (4)
print(s)          # 4 로 출력 (튜플형식x)
print(type(s))    # int형임

s2 = (5,)         # (5,) 와 같이 튜플형식으로 출력 - 값이 한개임에도 튜플형 유지함
print(s2)         # tuple형임
print(type(s2))
print('-'*30)

# 3. dict ----------------------------------------------------------------------------------
d = {'one': 'apple', 'two':'orange', 'three':'banana'}
print(d)
print(d['one'])       # 이름을 주고 해당하는 값을 꺼내오기

d['four']='melon'     # dict의 값 추가
print('추가 = ',d)

d['one']='strawberry' # dict의 값 변경
print('변경 = ',d)

print('two' in d)     # d 내부에 'two'가 있는지 여부를 True/False로 출력

print('키 = ', d.keys())    # dict의 key값만 출력 
print('값 = ', d.values())  # dict의 value값만 출력
print(d.items())            # dict를 각각 tuple형태인 하나의 list로 묶어서 출력 - 변환 (이제dict아님)
print('-'*30)

a, b = b, a          # 교환법칙(파이썬은 자바와달리 간결하게 가능) = b값을 a로, a값을 b로

list1 = []           # 초기화 개념 - 빈 리스트
list2 = [1,2,3,4,5]

tup1 = ()            # 초기화 개념- 빈 튜플
tup2 = (1,2,3,4,5)
tup3 = 1,2,3,4,5     # 하나의 변수에 여러값을 넣으면 튜플형태로 자동 Packing (자바에 없는 문법) 

set = {1,2,3,4,5}    # oracle의 union과 같은 형식

dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

print(list1, type(list1))
print(list2, type(list2))
print(tup1, type(tup1))
print(tup2, type(tup2))
print(tup3, type(tup3))
print(set, type(set))
print(dic, type(dic))
print('-'*30)

# format() --------------------------------------------------------------------------------
s = "{} {} {}".format(100, "Hello", 1.1)    # format()안의 순서는 0번부터 시작
print(s)

print(5/3)
print('{:10.2f}'.format(5/3))   # 전체 10자리이며 소숫점 이하 2자리까지 출력되도록 설정
print('Hello, {0}'.format('world'))         # 0번 자리에 world 들어가도록 설정
print('Hello, {1} {0}'.format(100, 200))    # 0번 자리에 200, 1번 자리에 100 들어가도록 설정
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.8))
print('{0} {0} {1} {1}'.format('Python', 'Script')) 
print('Hello, {language} {version}'.format(language='Python', version=3.6)) # 변수로 위치 지정도 가능
print('-'*30)

# 자릿수 지정 설정 추가 - 05d 와 같이 빈값 부분은 0으로 채우기
print('%03d' %1)   # 001처럼 빈자리는 0으로 채우기
print('{0:03d}'.format(2))  # 002 - format중 0번 값(=2)을 꺼내오되, 03자리수로 잡고 빈숫자는 0으로 채우기
print('{2:05d}'.format(1,2,3))  # format중 2번 값(3)을 꺼내오되, 05자리수로 잡고 빈숫자는 0으로 채우기
print('-'*30)

s="123"
print(s.zfill(5))        # 5자리 잡고 빈값부분은 0(=zero)으로 채우기
print(s.rjust(5, '#'))   # 5자리 잡고 빈값부분은 #으로 채우기
print('goofy'.zfill(6))  # 6자리 잡고 빈값부분은 0으로 채우기















