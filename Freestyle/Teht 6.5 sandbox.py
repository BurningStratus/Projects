list = [1,2,3,4,5]



#for luku_jota_vastaan_testataan in range(3, luku_jota_testataan - 1):

for c in list:
    for i in range(3, c-1):
        if c % i == 0:
            list.remove(i)
            print(i)

print(list)