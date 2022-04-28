'''
python에서 정수는 int로 나타냄
변수와 객체 참조간에 차이가 없는 불변(immutable)형
'''

a = (613).bit_length() # 정수를 나타내는 데 필요한 바이트 수 확인

'''
어떤 문자열을 정수로 변환하거나, 
다른 진법의 문자열을 정수(10진법)로 변환하려면 int(문자열, 밑) 메서드를 사용
'''

s = '11'
d = int(s)
print(d)

b = int(s, 2)
print(b)

''' int 메서드의 밑은 2에서 36 사이의 선택적 인수(optional argument) 
문자열 s에서 밑 범위의 숫자를 벗어나는 값을 입력할 경우 int 메서드에서 ValueError 발생 '''

'''
- python에서 부동소수점은 float로 표현하며 불변형
- 단정도(single precision) 방식에서 32비트 부동소수점을 표현할 경우
  1비트는 부호(sign, 0 양수 1 음수)
  23비트는 유효 숫자 자릿수(significant digits, 혹은 가수(mantissa))
  8비트는 지수(exponent)
- 배정도(double precision) 방식에서 64비트 부동소수점을 나타낼 때
  1비트는 부호
  52비트는 가수
  11비트는 지수로 표현
'''

# 부동소수점끼리 비교하기

# 부동소수점은 이진수 분수(binary fraction)로 표현되기 때문에 함부로 비교하거나 빼면 안 된다.
print(0.2 * 3 == 0.6)
print(1.2 - 0.2 == 1.0)
print(1.2 - 0.1 == 1.1)
print(0.1 * 0.1 == 0.01)

# 그 대신 동등성 테스트(equality test)는 사전에 정의된 정밀도 범위 내에서 수행되어야 한다.
def a(x, y, places = 7):
    return round(abs(x-y), places) == 0

# 정수와 부동소수점 메서드

'''
- 나누기 연산자 /는 항상 부동소수점을 반환
- // 연산자(floor 또는 truncation)를 사용하면 정수를 반환할 수 있다.
- % 연산자(module 또는 remainder)는 나머지를 구함
- divmod(x, y) 메서드는 x를 y로 나눌 때 몫과 나머지를 반
'''

print()