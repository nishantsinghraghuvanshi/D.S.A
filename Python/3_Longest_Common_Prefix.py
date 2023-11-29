def common_prefix():
    for i in range(len(lst_1)):
        if (lst_1[i[1]] == lst_2[i[1]]):
            print("PREFIX")



lst_1 = []
while True:
    lst_1.append(input("Enter a word : "))
    res = int(input("Press 1 to enter again 2 to exit"))
    if(res == 2):
        break
print(lst_1)