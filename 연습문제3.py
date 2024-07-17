#
def 홀짝(x):
    if x %2 ==0:
     a="짝수"
    else:
        a="홀수"
    return a


text=input("숫자를 입력하세요. :")
print(홀짝(int(text)))


#
var=1233

def find_odd_even (var):
    result = ""
    if var % 2 ==0:
        result = "짝수"
    else:
        result = "홀수"
    return result

nes= find_odd_even(123456789)
print(nes)