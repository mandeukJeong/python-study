string_a = "{}".format(10)

print(string_a)
print(type(string_a))

format_a = "{} 만원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

output_a = "{:d}".format(52)

output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)

output_f = "{:+d}".format(52)
output_g = "{:-d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)

print(output_f)
print(output_g)
print(output_h)
print(output_i)

output_j = "{:+5d}".format(52)
output_k = "{:+5d}".format(-52)
output_l = "{:=+5d}".format(52)
output_m = "{:=+5d}".format(-52)
output_n = "{:+05d}".format(52)
output_o = "{:+05d}".format(-52)

print(output_j)
print(output_k)
print(output_l)
print(output_m)
print(output_n)
print(output_o)

output_p = "{:f}".format(52.273)
output_q = "{:15f}".format(52.273)
output_r = "{:+15f}".format(52.273)
output_s = "{:+015f}".format(52.273)

print(output_p)
print(output_q)
print(output_r)
print(output_s)

output_t = "{:15.3f}".format(52.273)
print(output_t)

output_u = 52.0
output_v = "{:g}".format(output_u)
print(output_u)
print(output_v)
