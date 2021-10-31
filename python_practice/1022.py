# tuple 안의 list값을 2차원배열 형태로 이용 가능 --------------------------------------------
f=(1,[1,2,3],2)
print(f)
print(f[0])
print(f[1])
print(f[2])
print(f[1][2])    # 2차원배열같은 형태 - 3 출력 ( 1번인덱스값 안의 2번인덱스값 )

# f[2]=5          # tuple은 값을 바꿀 수 없음
print(f)
f[1][1]=5         # tuple안의 리스트는 값 변경 가능   
print(f)
print()
print('-'*30)
print()

# 파이썬의 객체형 변수의 주소값 ------------------------------------------------------------
x = 9000
y = 9000
z = 1
print(x, ', ', y)
print(type(x), ', ', type(y))
print(id(x), ', ', id(y))          # 둘의 주소값이 동일함 = 메모리에 한번 설정되고 같이쓰는중
print(x is y)                      # x가 가진 값과 y가 가진 값이 동일 = True 
print(id(x) == id(y))              # id()는 객체의 주소값 제공
print(x == y)
print()
print('-'*30)
print()

# 다중 for문 예제 -------------------------------------------------------------------------
# 문제 - 다중for문 
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()
print('-'*30)
print()

# 문제 - 다중for문 ( 역순 출력 ) - 방법 1 (range만 이)
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
print()
print('-'*30)
print()

# 문제 - 다중for문 ( 역순 출력 ) - 방법 2 (list 이용)
for i in list(range(1, 6)[::-1]):
    for j in list(range(1, i+1)[::-1]):
        print(j, end=' ')
    print()
print()
print('-'*30)
print()

# 문제 - 다중for문 ( 역순 출력 ) - 방법 3 (방법2에서 list담기 생략하고 index만 이)
for i in range(1, 6)[::-1]:
    for j in list(range(1, i+1)[::-1]):
        print(j, end=' ')
    print()
print()
print('-'*30)
print()


# -----------------------------------------------------------------------------------------
a = []
a = [1, 2, "Great"]
print(a[0], a[-1])           # 각각 int형 / str형
print(type(a[0]), type(a[-1]))
print(a[1:3], a[:])          # list형태로 출력
print('-'*30)


# 확장 for문 ------------------------------------------------------------------------------
lt = [('one', 1), ('two', 2), ('three', 3)]
for t in lt:                 # 확장 for문 형태
    print(t)                 # tuple 형태로 출력
    print(t[0], ', ', t[1])  # 문자열 형태로 출력
print('-'*30)
print()

# 단어 / 문장 대문자화 ---------------------------------------------------------------------

str = 'i love you'
print(str.title())           # 단어의 첫글자마다 대문자화
print(str.capitalize())      # 문장의 첫글자만 대문자화
print('-'*30)
print()

# 특정 값 제거 ----------------------------------------------------------------------------
s = [10, 20, 30, 40, 50]
s.remove(10)                 # 현재 갖고 있는 요소 중 10 인 값을 제거
print(s)
del s[0]                     # index번호로 특정 요소 값 제거
print(s)

s = [10, 20, 30, 20, 40, 50]
s.remove(20)                 # 특정 값을 가진 요소가 여러개일 때는, 첫번째 중복값만 제거
print(s)

s = [10, 20, 30, 40, 50]
s.append(60)                 # 특정 값을 추가하면 맨 뒤에 추가되며 (stack구조)
print(s)

# pop()을 통한 추출 및 삭제는 원본(s의 값)을 변경시킴
print(s.pop())               # pop()은 가장 마지막 값 하나 꺼내온 후 삭제 
print(s)
print(s.pop(0))              # pop(index번호) 를 통해 특정 값 하나 꺼내온 후 삭제
print(s)

print('-'*30)
print()

# 특정 값 추가 ----------------------------------------------------------------------------
s.extend([60, 70])           # 값으로 추가 - 기존의 리스트와 병합됨
print(s)
s.append([60, 70])           # list자체로 추가 - 기존의 리스트 안에 별개의 리스트값으로 포함
print(s)

print('-'*30)
print()

# 정렬 (sort) -----------------------------------------------------------------------------
# sort() - 원본이 변경 ( 원본은 반드시 백업해둬야 함 )
L = [('lee', 5, 38), ('kim', 3, 28), ('jung', 10, 36)]
L.sort()                    # 첫번째 값인 lee, kim, jung 기준으로 정렬됨 - 기본 오름차순(False)
print(L)
L.sort(reverse=True)        # 내림차순으로 sort
print(L)

L.sort(key=lambda x: x[1])  # index번호 1번 기준으로 오름차순 정렬 ( 5, 3, 10 기준 )
print(L)

# sorted() - 원본 변경 x
num = [25, 30, 90, 78, 45]
print(sorted(num))
print(num)





















