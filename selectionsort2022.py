def find_smallest(index,array):
	if index<len(array)-1:
		smallest=find_smallest(index+1,array)
		if array[smallest]<array[index]:
			return smallest
		return index
	return index
	
	
	
def selection_sort(array):
	for index,item in enumerate(array):
		smallest_index = find_smallest(index,array)
		array[smallest_index],array[index]=array[index],array[smallest_index]
	return array
		
		
		

	
		
array=[10,9,11,9,8,6,5,4,3,2,1]	
#print(find_smallest(1,array))
print(selection_sort(array))