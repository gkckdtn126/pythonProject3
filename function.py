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







