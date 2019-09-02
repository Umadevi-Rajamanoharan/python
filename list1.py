def arr(list1):
	for i in range(len(list1)-2):
		if list1[i]==1 and list1[i+1]==2 and list1[i+2]==3:
			return True
	return False
list2=[1,1,2,3,1]
print(arr(list2))
