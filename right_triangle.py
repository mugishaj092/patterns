'''
Enter the row size for the pattern: 5
* 
* * 
* * * 
* * * * 
* * * * * 

'''

rows = int(input("Enter number of rows: "))

for row in range(1,rows+1):
    for col in range(1,row+1):
        print("*", end=" ")
    print()
