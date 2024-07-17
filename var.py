
def find_len(m):
    if len(m)<=20:
        a=50
    elif len(m)>20:
        a=100

    return a



text=input("메세지를 입력하세요.:")
print(find_len(text))

#4. 사용자로부터 문자 메세지 입력 받아
text=input("메세지를 입력하세요.:")
print(len(text))
#1.문자 메세지의 길이를 파악
x="내가 입력하는 문자 메세지"
print(len(x))
#5. 함수로 만들어서 요금을 반환
def find_len(x):
    result=0
    print(x)
#2.문자 메세지의 길이 <= 20,50원
result=0
if len(x) <= 20:
    result=50
#3.문자 메세지의 길이> 20,100원
elif len(x) > 20:
    result=100

#return result

text= input("메세지를 입력해주세요")
var=find_len(text)
print(var)


find_len("이건 제가 함수 호출할 때 넣은 임의의 값입니다.")