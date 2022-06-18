usedCar = ['K5', 'white', 5000]
# print(usedCar)
if 'K6' in usedCar :
    print('지금 주문가능해요')
else :
    print('주문이 불가능합니다')

# if 조건문
# !!! 조건이 맞을 때만 코드를 실행시켜준다. !!!
# 조건식에는 부등호, 등호를 자주 쓴다.
# 조건식에는 in 문법도 자주 쓴다.
# else를 뒤에 붙여 사용이 가능하다.
# elif -> 차례대로 여러 조건을 검사할 때 사용한다.

# leftAmount = 10
# if leftAmount > 0 :
#     print('지금 주문 가능합니다')

# 반복문
# for i in range(0, 10) :
#     print('BMW 있어요!')

for i in usedCar :
    print(i)
    
# 함수 사용하기
# 1. 긴 코드를 짧은 단어로 축약할 때
def introducing(hello) :
    print(hello)
    
# 2. 마법의 모자 만들기 가능 => parameter 인자값을 넣기
# 무엇인가 집어넣으면 다른게 나오는 자료변환기 같은 느낌
introducing(12345)

def retIntro() :
    return 10

#  return은 남길자료 (그저 옵션일 뿐)
retIntro()
print(retIntro())