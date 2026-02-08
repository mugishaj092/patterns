'''
Docstring for hollow_right_angled_triangle
Enter the row size for the pattern: 5
* 
* * 
*   * 
*     * 
* * * * * 

=== Code Execution Successful ===
'''

rows = int(input('Enter the row size for the pattern: '))

for row in range(1,rows+1):
    for col in range(1,row+1):
        if row==rows or col==1 or col==row:
            print("*",end=" ")
        else: print(" ", end=" ")
    print()