'''
Enter the row size for the pattern: 5
* * * * * 
* * * * 
* * * 
* * 
* 

=== Code Execution Successful ===
'''

rows = int(input("Enter number of rows: "))

for row in range(1,rows+1):
    for col in range(row,rows+1):
        print("*", end=" ")
    print()