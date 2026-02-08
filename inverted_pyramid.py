'''
Enter the row size for the pattern: 5
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 

=== Code Execution Successful ===
'''

rows = int(input())

for row in range(rows, 0, -1):
    for space in  range(rows - row):
        print(" ", end=" ")
    for col in  range(1,row*2):
        print("*", end=" ")
    print()