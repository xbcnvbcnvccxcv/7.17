
def my_sum (list):
     b=0
     for a in list:
         b=a+b
     c = len(list)
     d = b/c
     return d


list3=[1,2,3,4,5]

print(my_sum(list3))

