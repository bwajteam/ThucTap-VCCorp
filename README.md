# Task 6 Recomment Film
Ý tưởng thực hiện bài toán:
Sử dụng giải thuật lọc cộng tác dựa trên items.
Các bước thực hiện:
  +Vì input là các bộ phim mà user đó thích, cho nên, ta tìm tất cả những người dùng cũng thích các phim mà user thích bằng cách từ file ratings, chọn ra những rating có id phim = id phim input, rating >= 3 (hoặc rating >= rating của input- trong bài t chọn >= 3)
  +Từ danh sách trên, lọc ra những người dùng có số đánh giá tương ứng với input là cao nhất (t chọn tỉ lệ 80% đánh giá thích giống input)
  +Sau khi chọn được những người có đánh giá tương đồng input, bắt đầu chọn ra tất cả các phim mà những người đó cũng thích (rating >=3 tiếp).
  +Sau khi có danh sách phim ưa thích của những người đó, ta chọn ra những phim mà có số người thích cao nhất và có đánh giá trung bình cũng cao, ở đây, t chọn ra các phim có 80 số người thích và ratings >= 4. Kết quả thu được sẽ là những phim mà input có thể sẽ thích.

