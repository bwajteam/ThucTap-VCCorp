#!/usr/bin/env python

import csv

def slove(ratings_file_name):
    
    min_film_rating_counts_percent = 0.6 #Số bộ phim đánh giá giống nhau giữa input.csv và rating.csv
    min_user_count_rating_percent = 0.6 #Số lượng người đánh giá tối thiểu
    number_of_recomment_films = 5
    ratings_data = open(ratings_file_name, "r").readlines()[1:]

    input_user = [] # Lưu userId đang xét
    input_movie = [] # Lưu danh sách movieId user đó đã xem
    input_movie_and_ratings = [] # [movieId][rating] của input

    for ln in input_data:
        input_movie.append(ln[1])
        input_movie_and_ratings.append([ln[1], ln[2]]) # [movieId][rating]
        if ln[0] not in input_user:
            input_user.append(ln[0])
    output_list_ln.append(input_user[0])

# Lưu các ratings_data trong file rating vào s1.csv nếu các data đó thỏa mãn điều kiện
    with open("s1.csv", "w") as s1:
        for ln in ratings_data:
            ln_temp = ln.split(",")
            if (str(ln_temp[0]) not in input_user and str(ln_temp[1]) in input_movie and float(ln_temp[2]) > 3 ):
                s1.write(ln)
    s1.close()


    s1_data = open("s1.csv", "r").readlines()
    
    movies_counts_ratings = {} #movies and ratings của input user
    recomment_user = [] # Danh sách user để gợi ý
    for n in range(0, len(s1_data)):
        ln = s1_data[n].split(",")
        key = ln[0].strip()
        if(key in movies_counts_ratings.keys()):
            movies_counts_ratings[key] += 1
        else:
            movies_counts_ratings[key] = 1

    max_film_rating_counts = len(input_movie)
    min_film_rating_counts = min_film_rating_counts_percent * max_film_rating_counts

    
# Lưu các userId và số bộ phim tương đồng với input ra file s2.csv
    s2 = open("s2.csv", "w")
    for item in movies_counts_ratings.items():
        if item[1] >= min_film_rating_counts:
            s2.write(str(item[0])+ "," + str(item[1])+ "\n")
            recomment_user.append(item[0])

    s2.close()



# Lưu các bộ phim có ratings > 3 của các user tương đồng ra file s3.csv

    s3 = open("s3.csv", "w")
    for ln in ratings_data:
        ln_split = ln.split(",")
        pair = [ln_split[1], ln_split[2]]

        if ln_split[0] in recomment_user and pair not in input_movie_and_ratings and float(ln_split[2]) > 3:
                s3.write(ln)
    s3.close()



# Đưa ra movieId, số người đánh giá

    s3 = open("s3.csv", "r").readlines()
    counts_dict = {} # key = movieId, item = số người đánh giá
    sum_dict = {} #key = moviedId, item = tổng điểm đánh giá

    for ln in s3:
        ln = ln.split(",")
        count1 = int(ln[1].strip())

        if count1 not in counts_dict:
            counts_dict[count1] = 1
        else :
            counts_dict[count1] += 1
        
        if count1 not in sum_dict:
            sum_dict[count1] = float(ln[2].strip())
        else:
            sum_dict[count1] += float(ln[2].strip())

# Sắp xếp theo số người đánh giá từ nhiều nhất đến it nhất
    counts_dict_sorted = sorted(counts_dict.items(),key = lambda arv: arv[1], reverse = True)

# Ghi ra file s4.csv movieId và số người đánh giá theo thứ tự từ nhiều nhất -> ít nhất
    s4 = open("s4.csv", "w")
    for item in counts_dict_sorted:
        s4.write(str(item[0]) + "," + str(item[1]) +  "\n")
    s4.close()

    recomment_user_len = len(recomment_user)
    min_user_count_rating = recomment_user_len * min_user_count_rating_percent

    output_list_ln.append(recomment_user_len)
        
    movies = open("ml-movies.csv", encoding="utf8").readlines()[1:]

    with open("s5.csv", "w") as f:
        f.write(','.join(['movieId', 'title', 'genres', '\n']))
    f.close()

# Lấy ra number_of_recomment_films movies có số người đánh giá lớn nhất
    s5 = open("s5.csv", "a")
    count = 0
    for item in counts_dict.items():
        if count < number_of_recomment_films:
            count += 1
            movie_id = int(item[0])
            user_count_rating = int(item[1])
            
            if user_count_rating >= min_user_count_rating:
                for row in movies:
                    row = row.split(",", 1)
                    if int(row[0]) == movie_id:
                        movie_title_genre = row[1]
                        s5.write(str(item[0]) + ',' + str(item[1]) + ',' + movie_title_genre)

    s5.close()


# Hàm check thực hiện đếm số bộ phim gợi ý đúng trong danh sách phim gợi ý đưa ra ở slove()
# Tỉ lệ = số bộ phim đúng/ tổng số phim
# Tỉ tệ = 0 khi không gợi ý đúng 1 phim nào
# Tỉ lệ = -1 khi không gợi ý phim nào
def check(check_data, output_file):
        recomment_movies = open(output_file, "r").readlines()[1:]
        correct_movies = 0
        check_movies = []
        correct_percent = 1
        if len(recomment_movies) > 0:           
            for ln in check_data:
                check_movies.append(ln[1])

            for ln in recomment_movies:
                ln = ln.split(",")
                if ln[0] in check_movies:
                    correct_movies+= 1
            if len(recomment_movies) > 0:
                correct_percent = (correct_movies / len(recomment_movies))*100
  
        else:
            correct_movies = -1
            correct_percent = -1

        output_list_ln.append(len(recomment_movies))
        output_list_ln.append(correct_movies) 
        output_list_ln.append(round(correct_percent, 1))

# ---Main---
ratings_file_name = "ratings_test.csv"
ratings_data = open(ratings_file_name, "r").readlines()[1:]


input_data_new = [] #Lưu tất cả ratings của từng user, reset khi đến userId mới
input_data = [] #Lưu ratings của user để train
check_data = [] #Lưu ratings của user để test


output_list_ln = [] #Lưu output với format ['userId', 'movies_input_len', 'movies_like_input_min','user_same_rating','user_same_rating_min','correct_movies', 'correct_percent', '\n'

userId = input("Nhap userId: ")
with open("output.csv", "w") as f:
        f.write(','.join(['userId','soUserTuongDong','soBoPhimGoiY','soPhimGoiYDung', 'xacSuat', '\n']))
f.close()
output_ratings = open("output.csv", "a")





for ln in ratings_data:
    ln_split = ln.split(",")
    # Lấy ratings_data của từng user. Nếu muốn gợi ý cho user tùy ý, có thể thêm bước check userId ở đây là được.
    if(int(ln_split[0]) == int(userId)):
        input_data_new.append(ln_split)
if len(input_data_new) == 0:
    print("Không tồn tại user\n")
elif(len(input_data_new) >=2):
    index = int(0.5* len(input_data_new))
    # 1/2 data đưa vào train, 1/2 data đưa vào test
    for i in range(0, index):
        input_data.append(input_data_new[i])
    for i in range(index, len(input_data_new)):
        check_data.append(input_data_new[i])

    # Train
    slove(ratings_file_name)

    # Test
    check(check_data, "s5.csv")

    # Print
    print(','.join(['userId','soUserTuongDong','soBoPhimGoiY','soPhimGoiYDung', 'xacSuat']))
    print(output_list_ln)
    output_ratings.write(str(output_list_ln) + "\n")

    print("input_data")
    print(input_data)
    print("check_data")
    print(check_data)

    f = open("s5.csv", "r").readlines()
    for ln in f:
        print(ln)     
else: 
    print("Không đủ data để gợi ý\n")  
        
output_ratings.close()
    