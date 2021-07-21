#  왼쪽 정렬
print("{0:<10}".format("hi"))
#  오른쪽 정렬
print("{0:>10}".format("hi"))
#  가운데 정렬
print("{0:^10}".format("hi"))
#  공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

#문자 개수 세기(count)

a = "hobby"
print (a.count('b'))

#위치 알려주기1(find)

a = "Python is the best choice"
print (a.find('b'))
print (a.find('k')) # 문자열 존재하지 않는다면 -1을 반환한다.

#위치 알려주기2(index)

a = "Life is too short"
print (a.index('t'))


#문자열 삽입(join)

print (",".join(['a','b','c','d']))

#소문자를 대문자로 바꾸기(upper)

a = "hi"
print (a.upper())

#대문자를 소문자로 바꾸기(lower)

a = "HI"
print (a.lower())

