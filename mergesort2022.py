def merge(left,right):
	i,j=0,0
	result=[]
	while i<len(left) and j<len(right):
		if left[i]<=right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	if i>=len(left):
		while j<len(right):
			result.append(right[j])
			j+=1
	elif j>= len(right):
		while i<len(left):
			result.append(left[i])
			i+=1
	return result
		
		
			

def merge_sort(num_lists):
	if len(num_lists) >=2:
		middle= int(len(num_lists)/2)
		left=merge_sort(num_lists[:middle])
		right=merge_sort(num_lists[middle:])
		return merge(left,right)
	return num_lists

	
		
k =[i for i in range(999999)]
print("done")
print(merge_sort(k[::-1]))	