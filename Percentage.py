print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("Maths :"))
English = int(input("English :"))
Science = int(input("Science :"))
Hindi = int(input("Hindi :"))
sum = math+English+Science+Hindi
print("sum of Math,English,Science,and Hindi", sum)
perc = (sum/400)*100
print(end="Percentage Mark = ")
print(perc)