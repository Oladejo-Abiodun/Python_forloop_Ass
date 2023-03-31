    # WRITE A PROGRAM THAT USES A FOR LOOP TO PRINT OUT THE 
    # NUMBERS 1 TO 10

for i in range(1, 11):
    print (i)


# ASS 2:
# WRITE A PROGRAM THAT USES A FOR LOOP TO PRINT OUT THE EVEN
# BETWEEN 1 AND 20

for i in range(1,21): 
    if i % 2 == 0:
        print(i)


# ASS 3:
# WRITE A PROGRAM THAT USES A FOR LOOP TO PRINT OUT THE ODD
# BETWEEN 10 AND 30

for i in range(10, 30):
    if i % 2 == 1:
        print(i)


# ASS 4:
# WRITE A PROGRAM THAT USES A FOR LOOP TO PRINT OUT THE FIRST 10 SQUARE NUMBERS
# (i.e THE NUMBERS: 1,4,9,16,25)

for i in range (1, 11):
    n = pow(i, 2)
    print(n)

"ASS 5:"
# WRITE A PROGRAM THAT USES A FOR LOOP TO CALCULATE SUM OF THE NUMBERS FROM 1 TO 100

total = 0
for i in range (1, 101):
    total += i
print(total)

# ASS 6:
#  WRITE A PROGRAM THAT USES A FOR LOOP TO FIND THE LARGEST NUMBER IN LIST OF INTEGERS

list = [1,2,3,4,5,6,7,89,9]
largest_num = list[0]
for num in list:
    if num > largest_num:
        largest_num = num
print(largest_num)

# ASS 7
# WRITE A PROGRAM THAT USES A FOR LOOP TO COUNT THE NUMBER OF VOWELS IN A STRING

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

# ASS 8
# WRITE A PROGRAM THAT USES A FOR LOOP TO PRINT OUT THE FIRST 10 FIBONACCI 
# NUMBERS(I.E THE NUMBERS 0,1,1,2,3,5,8,13,21 AND 34) 

a, b = 0, 1

# use a for loop to print out the first 10 Fibonacci numbers
for i in range(10):
    print(a)
    a, b = b, a + b

prev = 0
curr = 1

for i in range(10):
    print(prev)
    next = prev + curr
    prev = curr
    curr = next

prev = 0
curr = 1

for i in range(10):
    print(prev)
    next = prev + curr
    prev = curr
    curr = next
print(curr)


# ASS 9
# WRITE A PROGRAM THAT USES A FOR LOOP TO PRINT OUT THE MULTIPLICATION 
# TABLE FOR THE NUMBERS 1 THROUGH 10

for i in range (1, 11):
    print(f"Multiplication table for {i}:")
    for j in range (1, 11):
        print("f{i} x {j} = {i*j}")
    print()

for i in range(1, 11):
    print("Multiplication table for", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print()  # add a blank line after each table

#  ASS 9
# WRITE A PROGRAM THAT USES A FOR LOOP TO PRINT OUT THE LYRICS TO THE SONG
# "99 BOTTLES OF BEER ON THE WALL"

for i in range(99, 0, -1):
    if i == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take it down and pass it around, no more bottles of beer on the wall.")
    elif i == 2:
        print("2 bottles of beer on the wall, 2 bottles of beer.")
        print("Take one down and pass it around, 1 bottle of beer on the wall.")
    else:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")
    print()  # Add an empty line for spacing


