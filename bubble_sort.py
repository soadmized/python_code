from random import randint


N = 200
bubble_list = []

for num in range(0, N):
    bubble_list.append(randint(1, 999))

bubble_list_uniq = set(bubble_list)
print(len(bubble_list_uniq), len(bubble_list))
bubble_list = list(bubble_list_uniq)

print(bubble_list)

for i in range(len(bubble_list)-1):
    for j in range(len(bubble_list)-i-1):
        if bubble_list[j] > bubble_list[j+1]:
            bubble_list[j], bubble_list[j+1] = bubble_list[j+1], bubble_list[j]


print(bubble_list)
