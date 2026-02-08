'''
Enter the row size for the pattern: 5
        * 
      *   * 
    *       * 
  *           * 
* * * * * * * * * 

=== Code Execution Successful ===
'''

rows = int(input("Enter the row size for the pattern: "))

for row in range(1,rows+1):
    for space in range(rows-row):
        print(' ', end=" ")
    for col in range(1,row*2):
        if col==1 or col==(row)*2-1 or row == rows:
            print("*",end=" ")    
        else: print(" ",end=" ")
    print()