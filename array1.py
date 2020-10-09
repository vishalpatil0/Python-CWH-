# First method to create a 1 D array 
N = 5
b=34
arr = [b]*N 
print(arr) 

# Second method to create a 1 D array 
N = 5
arr = [b for i in range(N)] 
print(arr) 

# Using above first method to create a 
# 2D array 
rows, cols = (0,0) 
arr = [[0]*cols]*rows 
print(arr) 

# Using above second method to create a 
# 2D array 
rows, cols = (5, 5) 
arr = [[b for i in range(cols)] for j in range(rows)] 
print(arr) 

# Using above second method to create a 
# 2D array 
rows, cols = (5, 5) 
arr=[] 
for i in range(cols): 
	col = [] 
	for j in range(rows): 
		col.append(b) 
	arr.append(col) 
print(arr) 

for row in arr:
    print(row)

rows, cols = (0,0) 
arr1 = [[0]*cols]*rows 
print(arr1) 
for i in range(2):
    for j in range(3):
        arr1[i][j]=int(input("enter the input"))
        




print(arr1)