a = "Hello Python Programming!..."
print(a.upper())
print(a.lower())

input_a = """
    안녕하세요
문자열의 함수를 알아봅니다
"""

print(input_a)
print(input_a.strip())

print("TrainA10".isalnum())
print("10".isdigit())

output_a = "안녕안녕하세요".find("안녕")
print(output_a)

output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)

print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")

b = "10 20 30 40 50".split(" ")
print(b)

print(f'{10}')
print(f'3 + 4 = {3 + 4}')
print(f"""1 + 2 = {1 + 2}
2 + 3 = {2 + 3}
3 + 4 = {3 + 4}""")