num_list = []
for i in range(10):
    num = int(input()) % 42
    num_list.append(num)
    num_list_drop = list(set(num_list))
print(len(num_list_drop))