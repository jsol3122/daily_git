# 문제 1
names = ['Kim', 'Lee', 'Park']
times = ['10시', '11시', '12시']
letter = '''
안녕하세요 님,
오늘 면접에 참석해 주실 수 있나요?
시간은 입니다.
그럼 이만~
둘리 드림'''

for x in range(3):
    print(letter[0:6], names[x], letter[7:35], times[x], letter[35:])

# -------------------------------------------------------------------------
# 문제 2
list1 = ['홍길동', 75, 82, 95]
list2 = ['라이언', 88, 64, 70]
list3 = ['프로도', 100, 95, 90]

list1.append(list1[1]+list1[2]+list1[3])
list1.append(list1[4]/3)
list2.append(list2[1]+list2[2]+list2[3])
list2.append(list2[4]/3)
list3.append(list3[1]+list3[2]+list3[3])
list3.append(list3[4]/3)

sum = []
for i in range(3):
    sum.append(list1[i+1]+list2[i+1]+list3[i+1])

print('-'*50)
print('이름','\t','국어','\t','영어','\t','수학','\t','총점','\t','평균')
print('-'*50)
for i in range(6):print(list1[i], end='     ')
print()
for i in range(6):print(list2[i], end='     ')
print()
for i in range(6):print(list3[i], end='     ')
print('-'*50)
print('\t\t  ',sum[0],'\t',sum[1],'\t',sum[2])











