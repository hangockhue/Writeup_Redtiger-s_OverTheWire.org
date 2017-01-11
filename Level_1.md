### LEVEL 1

Ta nhận thấy người ta đã cho chúng ta về tên bảng nên đơn giản chúng ta chỉ cần tìm số cột của nó mà thôi

Ta dùng lệnh order by để xác định số cột có trong bảng đó 

Cuối cùng khi ta tìm được số cột là 4 sau đó ta dùng lệnh union để select tất cả các cột để tìm ra cột nào bị lỗi

<img src="https://uphinhnhanh.com/images/2017/01/08/level1-14dd95.png" alt="level1-14dd95.png" border="0" />

Việc còn lại chúng ta chỉ cần truy xuất dữ liệu của username và password mà thôi 

Ta dùng lệnh UNION SELECT 1,2,username, password FROM level1_users

<img src="https://uphinhnhanh.com/images/2017/01/08/level17f51f.png" alt="level17f51f.png" border="0" />
