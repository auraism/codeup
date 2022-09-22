# def digit_sum(nums):
#     sumnums = 0
#     for i in nums:
#         i = int(i)
#         sumnums += i

#     return sumnums

def getdigitSum(n):
    digitsum = 0
    while n != 0:
        digitsum = digitsum + n % 10
        n = n // 10
    return digitsum


nums = int(input())

firstcalc = getdigitSum(nums)
secondcalc = getdigitSum(firstcalc)

# for i in range(firstcalc+1):
#     if firstcalc < 10:
#         break
#     is_all = getdigitSum(i)

while True:
    if firstcalc < 10:
        print(firstcalc)
        break
    else:
        is_all = getdigitSum(secondcalc)
        print(is_all)
        break
    