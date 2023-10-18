terms = int(input("Enter number of numbers: "))
sum_of_odd = 0
sum_of_even = 0
for number in range(terms+1):
    if number%2 == 0:
        sum_of_even = sum_of_even + number
    else:
        sum_of_odd = sum_of_odd + number

print("Sum of even numbers =",sum_of_even,"and sum of odd numbers =",sum_of_odd)
