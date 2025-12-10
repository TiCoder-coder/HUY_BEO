a = int(input("Nhap so: "))
save = []
while a > 4: # Tên while là m đặt một điều kiện nào đó để kiểm tra

    # Trong while là thực thi những gì mong muốn
    save.append(a)
    break  # Dùng để kết thuc while

for i in save:
    print(i)