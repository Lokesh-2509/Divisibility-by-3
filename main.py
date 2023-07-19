def is_divisible_by_3(A):
    total_sum = sum(A)
    return total_sum % 3 == 0
A1 = list(map(int, input("Enter the elements of A1 (space-separated): ").split()))
output1 = int(is_divisible_by_3(A1))
print("Output 1:", output1)
