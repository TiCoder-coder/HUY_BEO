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
    B1: git init                                            (lệnh dùng để tạo một file .git liên kết với link github ở web)
    B2: git remote add origin link_github                   (lệnh dùng để điều khiển link github)
    B3: git config --global user.name "name....."           (lênh dùng để khải báo tên lên github cho moi người biết)
    B4: git config --global user.email "voanhnhat1612@gmail.com"            (lệnh dùng để khai báo email)
    B5: git add .                                           (để thêm các các file ở source code lên github -- ngoại trừ các file được khai báo trong venv)