a = 3
b = 4
print (a+b)

"Hello World"
"Python is Fun"

# 이스케이프 코드란?
# 문자열 예제에서 여러 줄으 ㅣ문장을 처리할 때 백슬래시 문자와 소문자 n을 조합한 \n 이스케이프 코드를 사용했다.
# 이스케이프 코드란 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 "문자 조합"이다. 주로 출력물을 보기 좋게 정렬하는 용도로 사용한다.
# 몇 가지 이스케이프 코드를 정리하면 다음과 같다.
# \n : 문자열 안에서 줄을 바꿀 때 사용
# \t : 문자열 사이에 탭 간격을 줄 때 사용
# \\ : 문자 \를 그대로 표현할 때 사용
# \' : 작은따음표(')를 그대로 표현할 때 사용
# \" : 큰따음표(")를 그대로 표현할 때 사용
# \r : 캐리지 리턴(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
# \f : 폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
# \a : 벨 소리(출력할 때 pc스피커에서 '삑'소리가 난다)
# \b : 백 스ㅠ페이스
# \000 : 널 문자

# 문자열 연산하기

# 문자열 더해서 연결하기(Concatenation)

head = "Phyton"
tail = "is fun!"
print (head + tail)

# 문자열 곱하기
a = "PYTHON"
print (a*2)

# 문자열 곱하기 응용

print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이 구하기

a= "Life is too short"
print (len(a))

# 문자열 인덱싱이란?

a = "Life is too short, You need Python"
print (a[3])

# 문자열 슬라이싱이란?

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print (b)

# 슬라이싱으로 문자열 나누기

a = "20210721Rainy"
date = a[:8]
weather = a[8:]
date
'20210721'
weather
'Rainy'

# "Pithon"이라는 문자열을 "Python"으로 바꾸려면?

a = "Pithon"
a[:1]
'P'
a[2:]
print (a[:1] + 'y' + a[2:])

# 문자열 포매팅 따라 하기

# 1. 숫자 바로 대입

print ("I eat %d apples." % 3)

# 2. 문자열 바로 대입

print ("I eat %s apples." % "five")

# 3. 숫자 값을 나타내는 변수로 대입

number = 3
print ("I eat %d apples." % number)

# 4. 2개 이상의 값 넣기

number = 10
day = "three"
print ("I eat %d apples. so I was sick for %s days." % (number, day))

# 문자열 포맷 코드
# 문자열 포매팅 예제에서는 대입해 넣는 자료형으로 정수와 문자열을 사용했으나 이 외에도 다양한 것을 대입할 수 있다.
# 문자열 포맷코드로는 다음과 같은 것이 있다.

# %s 문자열(String)
# %c 문자 1개(Character)
# %d 정수(integer)
# %f 부동소수(floating-point)
# %o 8진수
# %x 16진수
# %% Literal % (문자 % 자체)

print ("I have %s apples" %3)
print ("rate is %s" % 3.234)  # %s는 어떤 형태의 값이든 변환해 넣을 수 있다

# 포맷 코드와 숫자 함께 사용하기

# 1. 정렬과 공백

print("%10s" % "hi")

print("%-10sjane." % 'hi')

# 2. 소수점 표현하기

print("%0.4f" % 3.42134234)

print("%10.4f" % 3.42134234)
