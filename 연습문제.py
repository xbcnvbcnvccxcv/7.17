def find_len(x) :
    a=""
    if 81 <= x and x <= 100 :
        a="A"
    elif 61 <= x and x <= 80 :
        a="B"
    elif 41 <= x and x <= 60 :
        a="C"
    elif 21 <= x and x <= 40:
        a="D"
    elif 0 <= x and x <= 20 :
        a="F"
    else:
        a="올바른 점수를 입력하세요."
    return a

text= input("점수를 입력하세요.")
print(find_len(int(text)))

