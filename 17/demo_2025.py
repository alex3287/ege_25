A = [int(i) for i in open('text_25.txt')]
# print(A)
mini = min(A)
count = 0
sum_max = 0
for i in range(len(A)-1):
    if i % 1000 == 0:
        print(i, end=' ')
    for j in range(i+1, len(A)):
        if A[i] % 16 == mini or A[j] % 16 == mini:
            sum_max = max(sum_max, A[i]+A[j])
            count += 1
print('\n', count, sum_max)
# for i in range(len(A)-1):
#     if A[i] % 16 == mini or A[i+1] % 16 == mini:
#         sum_max = max(sum_max, A[i]+A[i+1])
#         print(A[i], A[i+1])
#         count += 1
# print(count, sum_max)