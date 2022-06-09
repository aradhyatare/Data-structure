values = {'I':1, 'V':5, 'X':10, 'L':50,'C':100,'D':500,'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90,'CD':400, 'CM':900}
print(values)
romanNumbers = ['I','V','X','L','C','D','M','IV','IX','XL','XC','CD','CM']
number = 'CXLII'  #1000 + 500 + 40 + 9 => 1549
sum = 0 

   
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