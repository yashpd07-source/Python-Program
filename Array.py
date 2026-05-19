import array as arr
array_num = arr.array('i', [6,7,6,7,6,7,6,7,6,7,6,7,6,7,6,7,6,7,6,7])
print("Original array: "+str(array_num))
print("Number of occurrences of the number 3 in the said array:"
+str(array_num.count(7)))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))