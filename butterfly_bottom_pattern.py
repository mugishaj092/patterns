'''
Enter the row size for the pattern: 5
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 

=== Code Execution Successful ===
'''

rows = int(input("Enter the row size for the pattern: "))
for row in range(1,rows+1):
    for col in range(rows - row + 1):
        print("*",end=" ")
    for space in range(1,2*row-1):
        print(' ',end=" ")
    for col in range(rows - row + 1):
        print("*",end=" ")
    print()