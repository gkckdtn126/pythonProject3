'''def test_8_10(): #괄호 안에 인수 parameter,여기까지는 생성을 위해서 무조건 필요하다.
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
   # return #함수를 만들고 함수를 불러온다.

test_8_10()  #콜론 안쓴다.함수를 호출한다.
test_8_10()

#매개 변수 값을 쓴다. 특정 값을 받아서 연산한다.
def print_n_times(value,n): #값을 두개 받을 수 있다.
    for i in range(n):
        print(value)
    #return #다시 올때
print_n_times("안녕하세!",5)  #매개변수 2개 쓰면 2개 써야하고, 3개쓸라면 3개만 적어야된다.
#함수 호출할 때 인자로 주는 값의 갯수는 맞춰줘야함 '''

'''def func3():
    x = 10
    z = 20
    c = x+z
    return c #변수 c가 가는 것이 아니고 값인 30만 간다. 
a=func3() #아무 변화가 없다.
print(a)
#함수 안에 abcsde가 있다. 내부로 값을 받아오긴 함 a 안에 abcsde가 들어가있다.'''

'''def func4(a,b): #함수 생성하는데 2개의 값을 받을 수 있다.
    return a*b #a와 b를 곱해서 함수를 호출 한 곳으로 그 값을 돌려보낸다. 내부에서만 쓰고 외부로 보낼라면 return을 쓰고 외부로 보낸다
c = func4(10,20)
print(c)'''

'''for i in range(1,10):
    print(f'{2} x {i} = {2*i}')
for i in range(1,10):
    print(f'{3} x {i} = {3*i}')  #함수 사용 안할때

def gugudan(num):
    for i in range(1,10):
        print(f'{num} x {i} = {num*i}')

gugudan(2)
gugudan(3)'''
'''def print_num(k):
    if k == 1:
        return False
    k_root = round(k**0.5)+1
    for i in range(2,k_root):
        if not(k%i):
            return False
    return True
num = int(input())
if print_num(num):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")'''

'''A,B = map(int, input().split())
def max_ke7(A,B):  #인수 두개
    if A>B:
        print("{}가 {}보다 큽니다.".format(A,B))
    else:
        print("{}가 {}보다 큽니다.".format(B,A))
max_ke7(A,B)'''

''''#def abc(a,b,c,d = 10) #디폴트값 그냥 정해진 값이다. 디폴트 매개변수
def print_n_time(value, n = 2):
    for i in range(n):
        print(value)
print_n_time("안녕하세요") #디폴트로 생성된 값이 있어서 두번째꺼 안쳐도 된다. n =2 뒤에 (value, n = 2, c)이렇게 안된다. c를 넣으려면
#디폴트 매개변수 앞으로 가야한다. (value, c, n=2)이렇게 해야한다. 

def print_n_time(value, b = 5, n = 10):
    return value+b+n
print_n_time(1,2,3) #1+2+3
print_n_time(1,2) #1+2+10
print_n_time(1) #1+5+10'''

'''#가변 매개변수
#def 함수 이름(*n): #9개 매개변수 n개 매개 변수 앞에 별표를 해서 n개의 매개변수가 되도록 해준다.
def print_n_time(n,*values): #가변 매개변수는 무조건 뒤에 와야된다. 규칙1.가변 매개변수 뒤에는 일반 매개변수가 올수없다.
    #2. 가변매개변수는 하나만 사용할 수 있다.
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_time(3,"안녕하세요","반갑","ㅂㅂ")'''

'''def print_n_time(*value):
    print(max(*value))

print(print_n_time(1,2,3,4,5,8,30))'''

'''def print_n_time(*values, n = 2):
    for i in range(n):
        for value in values:
            print(value)
        print()
        
print_n_time(3,"안녕하세요","반갑습니다","ㅂㅂ", n = 3) #그냥 3 적으면 안들어가고 n = 3으로 키워드 값으로 넣어준다.'''

'''def sum_all(start, end):
    output = 0
    for i in range(start, end+1):
        output += i
    return output

print("0부터 100까지", sum_all(0,100))


def sum_all(start = 0, end = 100, step = 1):
    output = 0
    for i in range(start, end+1,step):
        output += i
    return output

print("0부터 100까지", sum_all(0,100,2))'''

#재귀: 나 자신을 호출하는 무한루프, 팩토리얼
def factorial(n):
    output = 1
    for i in range(1,n+1):
        output *= i
    return output
print("1! :", factorial(1))
print("3! :" ,factorial(3))
print("5! :", factorial(5))
print("9! :" ,factorial(9))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1) #재귀 적인 함수  0이 될때까지 반복한다.

print("5!: ", factorial(5))

'''
1. 암 수
2. 두달 이상된 토끼는 번식할 수 있다. 
3. 토끼는 죽지 않는다. 
4. 번식한 토끼는 매달 새끼를 한쌍식 낳는다. 
'''
'''def fibo(n):
    if n ==1:
        return 1
    if n ==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print("피보나치", fibo(40)) #나 자신을 호출하고 계산하는데 연산 능력에 한계가 온다. '''

'''counter = 0 #외부의 값 선언
dictionary = {1:1,2:2} #딕셔너리 만들기
def fibo(n):
    print("피보나치 ({})를 구합니다.".format(n))
    global counter
    #파이썬은 함수 내부에서 함수 외부에 있는 변수를 참조하지 못한다.
    #함수 내부에서 함수 외부에 있는 변수라는 것을 설명하려면 global키워드가 필요하다.
    counter += 1
    if n ==1:
        return 1
    if n ==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

fibo(10)
print("피보나치 10에 계산된 값은 {}입니다.".format(counter))'''



counter = 0 #외부의 값 선언
dictionary = {1:1,2:2} #딕셔너리 만들기
def fibo(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibo(n-1)+fibo(n-2)
        dictionary[n] = output
        return output #메모한다

print("피보 : ", fibo(40))


