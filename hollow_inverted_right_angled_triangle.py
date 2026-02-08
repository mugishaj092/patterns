'''
Enter the row size for the pattern: 4
* * * * 
*   * 
* * 
* 

=== Code Execution Successful ==='''

rows = int(input("Enter the row size for the pattern: "))
for row in range(rows,0,-1):
    for col in range(1,row+1):
        if col == 1 or row == rows or row == col:
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()