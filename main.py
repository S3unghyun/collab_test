a = int(input())
b = int(input())
c = str(input())
n = int(input())

def div(a,b):
    return a / b

def reverse(c):
    return c[::-1]

def is_even(n):
    return n % 2 == 0

print("나누기 결과 : ", div(a,b))
print("거꾸로 했을때 : " , reverse(c))
print("이 숫자가 짝수인가?? : ", is_even(n))