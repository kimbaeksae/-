def display_multiplication_table(start, end):
    for i in range(1, 10):
        for j in range(start, end + 1):       
                print(f'{j} * {i} = {j * i}', end='\t')
        print() 

display_multiplication_table(2, 5)
print()
display_multiplication_table(6, 9)