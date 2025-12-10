# Ham
# So nguyen to la so chi chia het cho 1 va chinh no--- so nguyen to phai lon hon hoac bang 1 


import math # Thu vien cua python dung de lam viec voi cac phép toan cho don gian thay vi su dung phep tinh thong thuong
# import dung de khai bao thu vien trong python

a = int(input("Enter the number a: ")) # Biến toàn cục --- Sử dụng trong toán bộ chương trình
b = int(input("Enter the number b: "))

list_prime = [] # Khoi tao list de chua so nguyen to trong khoang a va b
# Dung ham de cho code gon va kha nang tai su dung
# Ham bat dau bang def name(tham so neu co):
def prime(a, b): # Muon ham thuc thi bang gi thi tham so la cai do
    # Khoi tao vong for de duyet so nguyen to
     # Vong for co 3 tham so (start, end+1, step)
    # is_prime = False
    for i in range(a, b+1): # Duyet nhung so tu b toi b --- Vi dụ: 2, 3, 5
        # Vị du: a = 2, b = 10
        # For no duyet tu 2 -> 11
        # Tuong ung voi moi con i thi no se duyet tat ca con j
        is_prime = True
        if i < 2:
            is_prime = False
        else:
            is_prime = True
        # Vong for thu 2 dung de duyet SO CHIA (so ngay chi duoc la 1 va chinh no(i) -- Lay so 2 de duyet: 2: 1 -> 2:2
        for j in range(2, int(i**0.5)+1): # Vi khong so nao co the chia het cho mot so ma lon hon so**0.5 +1
            if i % j == 0:
                is_prime = False
                break # Dung lai vong for --- de xet so khác
            # THU VONG FOR KHI CHAY O BEN TRONG MA XET DIEU KIEN >< CUNG LUC
            # else: 
            #     list.append(i) 
        # SIÊU LƯU Ý: NẾU TRONG VÒNG FOR XẾT ĐIỀU KIỆN ĐÚNG NẾU MUỐN XÉT ĐIỀU KIỆN SAI THÌ PHẢI OUT RA VÒNG FOR (VÀ NGƯỢC LẠI )
        if is_prime:
            list_prime.append(i) # Them con i vao list_prime de luu lai
    
    # QUY TAC DON TRACH NHIEM
    
    # ĐỊNH NGHĨA VỀ BIẾN:
    # Những biến khởi tạo trong hàm gọi là biến cục bộ --> Khi thoát ra khỏi hàm thì sẽ bị huỷ đi --- Trừ khi return kết quả về
    return list_prime
    

# ham dung de in so nguyen to ra
# QUY TẮC ĐẶT TÊN: ĐẠT TÊN THEO NGUYÊN TẮC CAMEL CASE (QUY TẮC CON LẠC ĐÀ) -- Ví dụ: TranHuuQuocDuy
                    # Đặt tên không được trùng với tên biến đã tạo và hàm có sẵn (hàm đạc biện) -- Ví dụ không được đặt là print, append
def print_list_prime(list_prime):
    # Neu ma in thong thuong thi su dung print() --- Chi in duoc 1 so
    for i in list_prime:
        print(i, end =", " if i != list_prime[-1] else "")

# CACH GOI HAM: 
# C1: tên hàm(tham số) ----- Ví dụ hàm viết def duyet(a, b): -- Khi goi ham se viet duyet(1, 2) hoặc là duyet_moi = duyet(1, 2)
# C2: tên mới = tên hàm(tham số)
prime(a, b) # Vi tham so nay luc khoi tao la khoi tao bien toan cuc nen them vao binh thuong
print_list_prime(list_prime)


# CACH KHAC DE SU DUNG VONG FOR 
# trai_cay = ["Cam", "Dao"]
# for i in trai_cay:
#     print(i, end =", " if i != trai_cay[-1] else "") # trai_Cay[-1] phan tu cuoi cung cua list

#     # Viet day du:
#     # if i !=- trai_cay[-1]:
#     #     end = ", "
#     # else:
#     #     end = ""