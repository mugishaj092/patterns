'''
Docstring for pyramid_pattern
Enter the row size for the pattern: 5
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

=== Code Execution Successful ===
'''
rows = int(input("Enter number of rows: "))
for row in range(1,rows+1):
    for space in range(rows - row):
        print(" ", end=" ")
    for space in range(1,row*2):
        print("*", end=" ")   
    print()
