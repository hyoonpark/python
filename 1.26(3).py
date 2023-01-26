test_list = [1, 2, 3, 7, 4, 6, 5]
test_list.sort()
print(test_list)

scores = [('eng', 88), ('sci', 90), ('math', 80)]
print(scores)

def check(x):
    return x[1]


#정렬
# scores.sort(key=check)
scores.sort(key=lambda x: x[1])
print(scores)