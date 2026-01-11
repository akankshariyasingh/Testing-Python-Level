'''
dict_problem_1.4 - Given two dictionaries of product prices, merge them such that: 
1. if the products exists in both keep the lower price.
2. otherwise keep the existing price.

'''

shop1={"pen":10,"book":50,"eraser":5}
shop2={"pen":8,"pencil":6,"book":55}

result={}

for items in shop1:  #puting the all value in shop 1 and then comparing shop 2 with the shop one using the loops
    result[items]=shop1[items]

for items in shop2:
    if items in result:
        if shop2[items]<result[items]:
            result[items]=shop2[items]
    else:
        result[items]=shop2[items]

print(result)
