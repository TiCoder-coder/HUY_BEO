for i in range(1, 10):
    if i == 2:
        break
    for j in range(1, 5 + 1): # Vòng for luôn chạy tới end-1, nếu muốn chạy 5 làn + 1 dô end
        a = 5
        print(f"a = {a+1}")


