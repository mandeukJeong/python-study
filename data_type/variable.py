pi = 3.14159265
r = 10

print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2 * pi * r)
print("원의 넓이 =", pi * r * r)

number = 100
number += 10
print("number :", number)

string = "안녕하세요"
string += "!"
print("string :", string)

string = input("입력> ")

print("자료:", string)
print("자료형:", type(string))

string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력B> ")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)
print("숫자 자료:", int_a + int_b)

output_a = int("52")
output_b = float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)

input_a = float(input("첫 번째 숫자> "))
input_b = float(input("두 번째 숫자> "))

print("덧셈 결과:", input_a + input_b)
print("뺄셈 결과:", input_a - input_b)
print("곱셈 결과:", input_a * input_b)
print("나눗셈 결과:", input_a / input_b)

str_a = str(52)
str_b = str(52.273)
print(type(str_a), str_a)
print(type(str_b), str_b)