# 제어문 if
'''
[형식]
1. if 조건:
    참

2. if 조건:
    참
   else:
    거짓
    
3. if 조건:
    참
   elif 조건:
    참
   else:
    거짓
    
파이썬에는 switch가 없
'''

x = 11
if x>10:
    print('참')
print('-'*30)

x = 30
if x>10 and x<20:
    print('참')
else:
    print('거짓')
print('-'*30)

x = 65
if x>=65 and x<=90:
    print(x, '는 대문자 ')
elif x>=90 and x<=120:
    print(x, '는 소문자')
else:
    print('숫자이거나 특수문자')
    

# ------------------------------------------------------------------------------------------
# 문제 1
str = input('문자열 입력 : ')
if str==str[::-1]:
    print(str,' 회문이다')
else:
    print(str, ' 회문이 아니다')
    
# 문제 2 - 풀이 1
'''
a = int(input('a의 값을 입력 : '))
b = int(input('b의 값을 입력 : '))
if a>=b:
    print(b, ' ', a)
else:
    print(a, ' ', b)
'''

# 문제 2 - 풀이 2
a = int(input('a의 값을 입력 : '))
b = int(input('b의 값을 입력 : '))
if a>=b:
    a, b = b, a        # 값 교환
    print(a, ' ', b)





















