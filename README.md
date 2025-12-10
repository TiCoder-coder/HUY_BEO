SETTING MÔI TRƯỞNG ẢO:
B1: python -m venv venv

B2:
    - Đối với window: venv/Scripts/activate
    - Đối với ubuntu: source venv/Scripts/activate

B3: Thức hành


INSTALL CÁC THƯ VIỆN CÒN THIẾU (NẾU CẦN): pip install tên_thư_viên


QUY TRING CLONE (DOWNLOAD CODE VỀ MÁY):
    - Chạy lệnh: cd Tên_thư_mục_muốn_clone_về 
    - Chạy lệnh: git clone link_code


QUY TRINH PUSH LÊN GIT:
C1 (CHUYÊN NGHIÊP):
    B0: Tạo file .gitignore (nếu cần)
    B1: git init                                            (lệnh dùng để tạo một file .git liên kết với link github ở web)
    B2: git remote add origin link_github                   (lệnh dùng để điều khiển link github)
    B3: git config --global user.name "name....."           (lênh dùng để khải báo tên lên github cho moi người biết)
    B4: git config --global user.email "voanhnhat1612@gmail.com"            (lệnh dùng để khai báo email)
    B5: git add .                                           (để thêm các các file ở source code lên github -- ngoại trừ các file được khai báo trong .gitignore) ----- MUỐN BIẾT ADD ĐÚNG CHƯA THÌ KIỂM TRA BẰNG LỆNH: git status
    B6: git commit -m "Ghi chú"
    B7: git checkout -b "tên nhánh"
        - Nếu là admin thì chạy git checkout -b main
        - Nếu là phàm nhân: git checkout -b feature (NHÁNH HAY DÙNG LÀ FEATURE CÒN CÓ THỂ TẠO NHÁNH NÀO CŨNG ĐƯƠC)

        KIỂM TRA LAI ĐÚNG NHÁNH CHƯA BẰNG LỆNH: git branch
    B8: chạy lệnh: git push -u origin main (Nếu dự án chưa có file gì)
        HOẶC chạy lệnh: git push -u origin main --force (nếu đã có file mà muốn cập nhập lại)


    -- LẦN ĐẦU LÀ LÀM TỪ BƯỚC 0 TỚI BƯỚC 8; LẦN THỨ 2 THÌ CHỈ CẦN LÀM TỪ BƯỚC 5 TRỞ XUỐNG

C2 (KHÔNG CHUYÊN NGHIÊP):
    B1: cd thư_mục muốn_tải_code_về
    B2: Chạy lệnh: git clone link_code
    B3: Mở thư mục đó lên và chỉnh tay
    B4: Làm từ buoc 3 như cách 1 trở xuống.
