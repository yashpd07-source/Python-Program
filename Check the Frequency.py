test_dict = {'Codingal': 2, 'is' : 1, 'best' : 3, 'for' : 4, 'Coding' : 67}
print("The original dictionary :" + str(test_dict))
K = 2
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1
print("Frequency of K is : " + str(res))