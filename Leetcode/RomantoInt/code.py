values = {'I':1, 'V':5, 'X':10, 'L':50,'C':100,'D':500,'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90,'CD':400, 'CM':900}
print(values)
romanNumbers = ['I','V','X','L','C','D','M','IV','IX','XL','XC','CD','CM']
number = 'CXLII'  #1000 + 500 + 40 + 9 => 1549
sum = 0 

    # I can be placed before V (5) and X (10) to make 4 and 9. 
    # X can be placed before L (50) and C (100) to make 40 and 90. 
    # C can be placed before D (500) and M (1000) to make 400 and 900.
#  IV, IX XL, XC, CD, CM CMXCI
# dusriList = []
# # print(number.split(',',3))
# n = 2
# for i in range(0, len(number), n):
    
#     temp = number[i:i+n]
#     print(temp)
#     if temp in romanNumbers:
#         print(f"in if loop {temp}")
#         dusriList.append(temp)
#     else:
#         print(f"in else loop {temp}")
#         temp = number[i]
#         dusriList.append(temp)
# print(dusriList)

# # list_values = list(number)
# # # print(list_values[0] + list_values[1])
# # sum = 0
# # for i in range(len(list_values)-1):
# #     # print(i)
# #     print(list_values[i])
# #     if i != len(list_values):
# #         num = list_values[i] + list_values[i+1]
# #         if num in romanNumbers:
# #             # print(num)
# #             value = values.get(num)
# #             sum += value 
# #             i = i + 1
# #             print(i)
# #             print(value)
# #             list_values.remove(list_values[i])
# #             list_values.remove(list_values[i+1])
# #         else:
# #             sum += values.get(list_values[i])
# # print(list_values)

    
# # #         sum += 9
# # #         continue
# # #     if list_values[i] + list_values[i+1] == 'VI':
# # #         sum += 4
# # #     if list_values[i] + list_values[i+1] == 'LX':
# # #         sum += 40
# # #     if list_values[i] + list_values[i+1] == 'CX':
# # #         sum += 90
# # #     if list_values[i] + list_values[i+1] == 'DC':
# # #         sum += 400
# # #     if list_values[i] + list_values[i+1] == 'MC':
# # #        sum += 900

# # print(sum)
# # # print(value)
# # # for i in number:
# # #     value = values.get(i)
# # #     sum += value

# # # print(sum)

i = 0
num = 0
while i < len(number):
    print(i)
    print(number[i:i+2])
    if i+1<len(number) and number[i:i+2] in values:
        print(number[i:i+2])
        num += values[number[i:i+2]]    
        i += 2
    else:
        num += values[number[i]]
        i += 1

print(num)    