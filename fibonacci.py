first_term = 0
second_term = 1
third_term = 0
terms = int(input("Enter number of terms: "))

print(first_term,second_term,end=" ")
for i in range(terms-2):
    third_term = first_term + second_term
    first_term = second_term
    second_term = third_term
    print(third_term,end=" ")