'''
Docstring for diamond_pattern
Enter the row size for the pattern: 4
      * 
    * * * 
  * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      * 

=== Code Execution Successful ===
'''

rows = int(input("Enter number of rows: "))

for row in range(1,rows + 1):
    for space in range(rows - row):
        print(" ", end=" ")
    for col in range(1,row*2):
        print("*", end=" ")
    print()
for row in range(rows-1,0,-1):
    for space in range(rows-row):
        print(" ", end=" ")
    for col in range(1,row*2):
        print("*", end=" ")
    print()