### Level 4

Ta thứ các cách như cái lv trước không phát hiện đượng gì 

Sau đó ta thử thêm câu lệnh 'AND 1 = 1 thì nó trả về 1 

Còn thử câu lệnh AND 1 = 2 thì nó trả về 0

Vậy nghĩa là 1 nghĩa là đúng còn 0 nghĩa là sai 

Bước tiếp theo ta sẽ thử tìm version của SQL 

Ta thêm câu lệnh AND subtring(version(),1,1) = 4 nghĩa là version hiện tại có phải là 4 không 

Sau khi dò version thì ta sẽ tìm được version hiện tại của nó là 5

Ta thử xem nó có mấy columm . Dùng lệnh order by , và thấy nó có 2 volumm . vì thử columm thứ 3 thì nó trả về 0 nhưng khi select nó chỉ trả về đúng hoặc sai . Vậy nên ta thử tìm số ký tự trong keyword xem sao

http://redtiger.labs.overthewire.org/level4.php?id=1 and length(keyword)= 21

Kết quả trả về 1 nên ta biết nó có 21 ký tự 

Vậy ta có thể tận dụng hàm boolean để kiểm tra xem trong keyword có những từ nào bằng cách thử tất cả các từ vào

Ta thêm câu lệnh sau and ascii(substring((select keyword FROM  level4_seret)" + ",%d,1)) = %d

Với lệnh substring thì ta sẽ xét xem ở trị trí bao nhiêu ký tự đó có đúng hay không

subtring(chuoi,vitri,sokytu)

Ta xem code bằng python tại [đây](https://github.com/hangockhue/Writeup_Redtiger-s_OverTheWire.org/blob/master/python%20lv4%20url.py)
