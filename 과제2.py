#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = 3
b = 6
c = - 5
s1 = (-b + (b**2-4*a*c)**0.5) / (2*a)
s2 = (-b - (b**2-4*a*c)**0.5) / (2*a)
s1 = round(s1,3)
s2 = round(s2,3)

print((s1, s2))


# In[9]:


# 입력 예시
# <p>취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.</p>

# 출력 예시
# 취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.

a = input()
print(a[3:-4])


# In[17]:


str_lst = input('문자열을 입력하세요. : ')
word = []
for i in str_lst.split(sep=' '):
    word.append(i)
print(word)
if word[0][-1] == word[1][0] and word[1][-1] == word[2][0]:
    print('Pass')
else:
    print('Fail')


# In[26]:


# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500
steak = 50000
vat = int(steak * 0.15)

print(f'스테이크   {steak:,}\n+ VAT     {vat:,}\n 총계 \    {steak + vat:,}')


# In[57]:


todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]
a = input()
b = int(input())
plus = [(f'{a}', b)]
todo.extend(plus)

print(todo)


# In[38]:


orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
lst1 = orders.split(',') #리스트화
total = len(lst1)
lst2 = list(set(lst1))
lst2.sort()

print(total)
print(lst2)


# In[49]:


orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
lst1 = orders.split(',')
lst2 = []
for word in lst1:
    if '아이스' in word:
        lst2.append(word)
print(len(lst2))
print(f'아이스아메리카노:', lst1.count('아이스아메리카노'))
print(f'카라멜마키야또:', lst1.count('카라멜마키야또'))
print(f'에스프레소:', lst1.count('에스프레소'))
print(f'아메리카노:', lst1.count('아메리카노'))
print(f'아이스라떼:', lst1.count('아이스라떼'))
print(f'핫초코:', lst1.count('핫초코'))
print(f'아이스카라멜마키야또:', lst1.count('아이스카라멜마키야또'))
print(f'카푸치노:', lst1.count('카푸치노'))
print(f'라떼마키야또:', lst1.count('라떼마키야또'))

