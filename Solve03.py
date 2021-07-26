# 리스트 자료형

a = [1,2,3]
print (a)
print (a[0])
print (a[0]+a[2])

a= [1,2,3,['a','b','c'],4,5]
print (a[2:5])

# 리스트 반복하기

a = [1,2,3]
print (a*3)

# 리스트 길이 구하기

a = [1,2,3]
print (len(a))

# 리스트에서 값 수정하기

a = [1,2,3]
a[2] = 4
print (a)

# del 함수 사용해 리스트 요소 삭제하기

a = [1,2,3]
del a[1]
print (a)

# 리스트에 요소 추가 (append)

a = [1,2,3]
a.append(4)
print (a)
a.append([5,6])
print (a)

# 리스트 정렬(sort)

a = [1,4,3,2]
a.sort()
print (a)

# 리스트 뒤집기(reverse)

a =['a','b','c']
a.reverse()
print (a)

# 위치 반환(index)

a = [1,2,3]
print (a.index(3))

# 리스트에 요소 삽입(insert)

a = [1,2,3]
a.insert(0,4)
print (a)
a.insert(4,4)
print (a)

# 리스트 요소 제거(remove)

a = [1,2,3,1,2,3]
a.remove(3)
print (a)

# 리스트 요소 끄집어내기(pop)  == 맨 마지막 요소를 돌려주고 그 요소는 삭제한다

a= [1,2,3]
print (a.pop())
print(a)

# 리스트 확장(extend)

a = [1,2,3]
a.extend([4,5])
print (a)
b= [6,7]
a.extend(b)
print (a)

# 튜플은 어떻게 만들까?
# 튜플(tuple)은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다.
# 1. 리스트는 [] 으로 둘러싸지만 튜플은()으로 둘러싼다.
# 2. 리스트는 그 값의 생성, 삭제 , 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.

t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('ab','cd'))

# 리스트와 모습은 거의 비슷하지만 튜플에서는 리스트와 다른 2가지 차이점을 찾아볼 수 있다.
# t2 = (1,)처럼 단지 1개의 요소만을 가질때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다는 것과
# t4 = 1,2,3 처럼 괄호()를 생략해도 무방하다는 점이다

# 튜플 다루기

# 인덱싱하기

t1 = (1,2,'a','b')
print (t1[0])

# 슬라이싱하기

t1 = (1,2,'a','b')
print (t1[1:])

# 튜플 더하기

t1 = (1,2,'a','b')
t2 = (3,4)
print (t1 + t2)