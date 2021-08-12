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

'''#재귀: 나 자신을 호출하는 무한루프, 팩토리얼
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

print("5!: ", factorial(5))'''

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



'''counter = 0 #외부의 값 선언
dictionary = {1:1,2:2} #딕셔너리 만들기
def fibo(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibo(n-1)+fibo(n-2)
        dictionary[n] = output
        return output #메모한다

print("피보 : ", fibo(40))



counter = 0 #외부의 값 선언
dictionary = {1:1,2:2} #딕셔너리 만들기
def fibo(n):
    if n in dictionary:
        return dictionary[n] #조기 리턴 !!!!

    output = fibo(n-1)+fibo(n-2)
    dictionary[n] = output
    return output #메모한다

print("피보 : ", fibo(40))'''

#예외처리
#에러 처리

'''try:
    문장
except
    예외 처리:'''
'''def calc(value):
    sum = None
    try:
        sum = value[0]+value[1]+value[2]
    except IndexError as err:
        print("인덱스 에러")
    except Exception as err:
        print(str(err))
    else:
        print("에러 없음")
    finally:
        print(sum)
calc([1,2])'''

'''a = 10
def ary():
    global a
    print(a)'''

'''def list(k):
    temp = set(k)
    return list(temp)'''

'''객체 = open(경로, 읽기 모드)
r = 읽기
w = 쓰기 
+r = 읽기 or 쓰기 모드 = 경로를 지정한 곳에 파일이 없다면 에러 
+w = 읽기 or 쓰기 = 파일이 없다면 생성 
a = 추가 
a+ = 읽기 + 추가 모드 
close() 마지막엔 close 꼭 해주기'''

'''file= open("basic.txt", "w")

file.write("hello python")

file.close()'''

'''data = "파이썬 프로그래밍"
with open("basic.txt", "w", encoding="utf-8") as f: #with 쓰면 클로즈 안써도 됨, 모든 명령어를 줄여서 f라고 하자:as를쓴다.
    f.write(data)

data = "파이썬 프로그래밍"
with open("basic.txt", "w", encoding="utf-8") as f:  # with 쓰면 클로즈 안써도 됨, 모든 명령어를 줄여서 f라고 하자:as를쓴다.
    f.write(data)
    
import os #
print(os.getcwd())

절대 경로
C:/Users/Lenovo/PycharmProjects/4
상대경로 
4/data.txt'''  #하위폴더

'''data = "파이썬"
with open("C:/Users/Lenovo/PycharmProjects/4/ff/basic.txt", "w", encoding="utf-8") as f:  # with 쓰면 클로즈 안써도 됨, 모든 명령어를 줄여서 f라고 하자:as를쓴다.
    f.write(data) #지금 function있는쪽이 내 위치이고 이걸 기준으로 함 상대경로는 '''
'''f = open("basic.txt","r",encoding= "utf-8") #f에 객체로 저장하는거
f.close()'''

#예외처리 1. 프로그램 실행전에 발생하는 오류 2.프로그램 실행중에 발생하는경우, 파이썬은 try랑 if랑 같이 쓰는데 try가 느리고 if가 빨라서 if를 쓸때도 있다.
#플라스크
'''user_input_a = input("정수입력 :")
if user_input_a.isdigit(): #숫자로만 구성된 글자인지 확인하는거, 실수는 isfloat()
    number_input_a = int(user_input_a)
    print("원의 반지름 :", number_input_a)
    print("원의 울레 :", 2*3.14*number_input_a)
else:
    print("정수를 입력하지 않았습니다.")
    #isalpha():오직 영어로만 구성된 문자인지, isalnum():'''


'''user_input_a = input("정수입력 :")
try: #오류를 방지하게 해준다. 에러나면 무시, 모든 것이 다 들어간다.
    number_input_a = int(user_input_a)
    print("원의 반지름 :", number_input_a)
    print("원의 울레 :", 2*3.14*number_input_a)
except:# 에러나면 실행 에러를 없애기 위해서 실행되는 거임
    print("정수를 입력하지 않았습니다.")
    #isalpha():오직 영어로만 구성된 문자인지, isalnum():
else:
    print("예외가 발생하지 않았습니다.")
    #에러가 없을때 성공했을때 쓰는 코드
finally:
    print("끝났습니다.")
    #무조건 실행하는것

list_input_a = ["52","273","32","스파이","103"]
list_number = []
for item in list_input_a:
    try:
        float(item) #예외
        list_number.append(item)
    except:
        pass
print("{} 내부".format(list_input_a))
print("{} 내부".format(list_number))'''

'''try except
try except+else
try except+finally
try except+else+finally
try finally #이렇게 쓸 수 있다.'''


'''try:
    file = open("basic.txt", "w")
    file.close()
except Exception as e:
    print(e)
print("파일이 제대로 닫혀 있는지 확인")
print("file.closed : ", file.closed)'''

'''try:
    number_input_a = int(input("정수입력: "))
    print("반지름", number_input_a)
    print("둘레", 2*3.14*number_input_a)
except Exception as f:
    print("type(exception) :", type(f) )
    print("exception :", f)
    #예외가 발생 했을 때 exception 클래스를 불러옴'''


'''list_number = [15,212,31,2,3]
try:
    number_input_a = int(input("정수입력: "))
    print("{}번째 요소 {}".format(number_input_a,list_number[number_input_a]))
except ValueError:
    print("정수를 입력하세요")
except IndexError:
    print("리스트의 인덱스를 벗어났습니다.")
    #예외가 발생 했을 때 exception 클래스를 불러옴'''

'''list_number = [15,212,31,2,3]
try:
    number_input_a = int(input("정수입력: "))
    print("{}번째 요소 {}".format(number_input_a,list_number[number_input_a]))
except ValueError as exception:
    print("정수를 입력하세요")
    print("exception: ",exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났습니다.")
    print("exception: ", exception)
    #예외가 발생 했을 때 exception 클래스를 불러옴'''


'''list_number = [15,212,31,2,3]
try:
    number_input_a = int(input("정수입력: "))
    print("{}번째 요소 {}".format(number_input_a,list_number[number_input_a]))
except ValueError as exception:
    print("정수를 입력하세요")
    print("exception: ",exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났습니다.")
    print("exception: ", exception)
    #예외가 발생 했을 때 exception 클래스를 불러옴
except Exception as exception:
    print("그 외 모든 에러") #모든 에러를 예측할 수 있다. 
    print("exception: ", exception)'''




