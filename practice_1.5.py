'''
practice_1.5 - Given a list of lists, return elements common in all.

'''

def common_element(lists):
    common=set(lists[0])
    for num in lists[1:]:
        common = common & set(num)
    return list(common)

print(common_element([[1,2,3],[2,3,4],[2,3]]))
