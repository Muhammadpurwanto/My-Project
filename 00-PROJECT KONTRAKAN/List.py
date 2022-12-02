#  data = [[12],[1,2,3],[3,3,4],[5,3]]
# x=0
# p=0
# for i in data:
#     for r in i[x]:

#         # hasil=4 is r
#         # print(r)
#         if 3 == r:
#             p=9
            
#     x+=1
#     print(i)

# print(p)
data=[]   
while True:
    nama=input("nama: ")
    nomor=input("nomor: ")
    hasil= nama in data
    if hasil==True :
        print("ok")

    data.insert(nomor,nama)
    # data.append(nomor)
    for i in data:
        print(f"{i}")
    print(data)

# data=[1,2,3,5,6,7,4,2,1]
# hasil = 9 in data
# print(data)


