for i in range(10):
    print(i, end=" ")
print()

for i in range(1, 10, 1):
    print(i, end=" ")
print()

# 역순으로 9 8 7 6 5 4 3 2 1 0 출력 - 방법 1
for i in range(9, -1, -1):
       print(i, end=" ")
print()

# 역순으로 9 8 7 6 5 4 3 2 1 0 출력 - 방법 2 ( 많이 쓰임 )
for i in list(range(10)[::-1]):
       print(i, end=" ")
print()

# 문제 1 - 구구단 찍기
dan = int(input('원하는 단 입력 : '))
for i in range(1, 10):
    print(dan, ' * ', i, ' = ', dan*i)
print()
print('-'*30)
    
# 문제 2 - 구구단 전체 찍기
for i in range(1, 10):
    for dan in range(2, 10):
        print(dan, '*', i, '=', dan*i, end='\t')
    print()
print()
print('-'*30)

# 문제 3 - 배수의 합과 차 구하기
sum1, sum2 = 0, 0
for i in range(0, 101, 5):
    sum1 += i
for i in range(0, 101, 7):
    sum2 += i
print('5의 배수의 합 = ', sum1)
print('7의 배수의 합 = ', sum2)
print(sum1, '-', sum2, '=', sum1-sum2)
print("%d - %d = %d" %(sum1, sum2, sum1-sum2))           # 서식문자 사용한 경우
print("{0} - {1} = {2}".format(sum1, sum2, sum1-sum2))   # format() 사용한 경우



















