hour_1 = int(input())
minet_1 = int(input())
sec_1 = int(input())
hour_2 = int(input())
minet_2 = int(input())
sec_2 = int(input())
total_1 = hour_1*360+minet_1*60+sec_1
total_2 = hour_2*360+minet_2*60+sec_2
z = abs(total_1 - total_2)
print(z)
