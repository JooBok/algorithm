num_list = []
for i in range(1, 10):
    num = int(input())
    num_list.append(num)
print(f'{max(num_list)}\n{num_list.index(max(num_list))+1}')