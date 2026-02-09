'''
Enter the row size for the pattern: 5
* * * * * * * * * 
  *           * 
    *       * 
      *   * 
        * 

=== Code Execution Successful ===
'''

rows = int(input('Enter the row size for the pattern: '))

for  row in range(rows,0,-1):
    for space in range(rows-row):
        print(" ", end=" ")
    for col in range(1,row*2):
        if col == 1 or row == rows or col==row*2-1:
            print("*", end=" ")
        else: print(" ", end=" ")
    print()