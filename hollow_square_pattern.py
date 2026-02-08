'''
Docstring for hollow_square_pattern
Enter the row size for the pattern: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 

=== Code Execution Successful ===
'''

rows = int(input('Enter the row size for the pattern: '))

for row in range(1,rows+1):
    for col in range(1,rows+1):
        if row == 1 or row==rows or col==1 or col==rows:
            print("*",end=' ')
        else: print(" ",end=" ")
    print()
