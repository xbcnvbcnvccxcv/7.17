#
def my_var(numbers):
    b=0
    result=[]
    for a in numbers:
        b= int(a*1.1)
        result.append(b)
    return result

numbers = [100,200,300]
print(my_var(numbers))

#
var=[100,200,300]

def VAT(var):
    result_list = []
    for i in var:
         result_list.append(i*1.1)
    return (result_list)

x = [100,200,300]
print(VAT(x))
