sample_list = [11, 22, 33, 55, 66]
#주어진 리스트의 4번째 자리에 있는 항목을 제거하고 변수에 할당해 주세요.

print('original list: ', sample_list)

num = sample_list.pop(3)
print('list after: ', sample_list)
print('num: ', num)

#sample_list의 가장 뒤에 77를 추가해보세요

sample_list.append(77)

#할당해좋은 변수의 값을 sample_list의 2qjs index에 추가해보세요.

sample_list.insert(2, num)

print(sample_list)