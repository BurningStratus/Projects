list = [1,83,2,3,53,4,5,15]



#for luku_jota_vastaan_testataan in range(3, luku_jota_testataan - 1):

# for c in list:
#     for i in range(3, c-1):
#         if c % i == 0:
#             list.remove(i)
#             print(i)
#
# print(list)

for i in list:
    for c in range(3, i-1):
        if i % 2 != 0:
            list.remove(i)
print(list)