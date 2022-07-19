# ifelse.py

# 다중라인으로 주석 처리 : ctrl + / (cmd + /)
# score = int(input("점수를 입력:"))70

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 :", grade)

#반복문
# value = 5
# while value > 0:
#     print(value)
#     value -= 1

#조건이 되는 함수 정의
def getBiggerThan20(i):
    return 1 > 20

print("--- 람다함수사용---")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)
