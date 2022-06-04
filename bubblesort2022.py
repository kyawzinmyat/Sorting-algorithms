def bubble_sort(array):
	swap_counter =-1
	while swap_counter != 0:
		swap_counter=0
		for index,item in enumerate(array[:-1]):
			if item  >= array[index+1]:
			
				array[index],array[index+1]=array[index+1],array[index]
				swap_counter+=1
	return array
				

			
def generate_test_case(n=10):
		k=[ i for i in reversed(range(n))]
		return k

		
#print(generate_test_case())	

#j=[3,4,5,10,8,7,6]	
print(bubble_sort(generate_test_case(1000)))
#print(bubble_sort(j))				
#		