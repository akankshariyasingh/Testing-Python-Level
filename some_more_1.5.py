'''
some_more_1.5 - Find all unique pairs whose sum equals target.
'''

def unique_pairs(nums,target):
    pairs=[]
    unique_set=set()
    for num in nums:
        needed = target - num
        if needed in unique_set:
            pair = tuple(sorted((num,needed)))
            if pair not in pairs:
                pairs.append(pair)
        unique_set.add(num)
    return pairs

print(unique_pairs([1,2,3,4],6))