#!/usr/bin/env python
# coding: utf-8

# In[24]:


fruit = 'apple, rottenBanana, apple, RoTTenorange, Orange'
n = []
fruit = fruit.replace('rottenBanana', 'banana')
fruit = fruit.replace('RoTTenorange', 'orange')
fruit = fruit.replace('Orange', 'orange')
fruit = fruit.split(',') # ,를 기준으로 분할
n = fruit

print(n)


# In[32]:


char = input()
char = list(char)
if len(char) % 2:
    print(char[len(char)//2])
else:
    print(char[len(char)//2 - 1],char[len(char)//2])


# In[40]:


infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
sum_age = list(age_list['age'] for age_list in infos)

print(sum(sum_age))


# In[47]:


blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

blood_dict = {}
for types in blood_types:
    if types in blood_dict:
        blood_dict[types] += 1
    else:
        blood_dict[types] = 1
print(blood_dict)


# In[ ]:


percent, amount = map(int, input('소금물의 농도(%)와 소금물의 양(g)을 입력하십시오:').split())


# In[ ]:





# In[ ]:




