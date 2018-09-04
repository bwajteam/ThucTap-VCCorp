#!/usr/bin/env python

import csv
# ====================================STEP1====================================
# Lấy ra userId,movieId,rating trong file "ratings" thõa mãn movieId = input_movieId và rating = input_rating

def s1(input_file, rating_file): 
    input_data = open(input_file, "r").readlines()[1:]
    input_user = []
    input_movie_and_ratings = {}
    input_movie = []


    for ln in input_data:
        ln = ln.split(",")

        input_movie.append(ln[1])
        input_movie_and_ratings[ln[1]] = ln[2]
        if ln[0] not in input_user:
            input_user.append(ln[0]) 

    ratings = open(rating_file, "r").readlines()[1:]
    with open("s1.csv", "w") as f:
        for ln in ratings:
            ln2 = ln.split(",")
            if ln2[1] in input_movie:
                # if (float(ln2[2]) >= float(input_movie_and_ratings[ln2[1]]) and ln2[0] not in input_user):
                if (float(ln2[2]) >= 3 and ln2[0] not in input_user):
                    f.write(ln)
    f.close()
# ====================================STEP2====================================
# Lấy ra danh sách userId, filmRatingCounts với filmRatingCounts là số bộ film có cùng đánh giá với input_user.
# filmRatingCounts >= min_film_rating_counts (số bộ phim có cùng đánh giá tối thiểu tối thiểu)
def s2(min_film_rating_counts_percent):
    data = open("s1.csv", "r").readlines()
    f = open("s2.csv", "w")
    pair = {}
    user = []
    for n in range(0, len(data)):
        row = data[n].split(",")
        key = row[0].strip()
        if(key in pair.keys()):
            pair[key] += 1
        else:
            pair[key] = 1
    max_film_rating_counts = max(pair.values())
    min_film_rating_counts = min_film_rating_counts_percent * max_film_rating_counts

    for item in pair.items():
        if item[1] >= min_film_rating_counts:
            f.write(str(item[0])+ "," + str(item[1])+ "\n")
            user.append(item[0])
    
    f.close()
    return len(user)


# ====================================STEP3====================================
# Lấy ra userId,movieId,rating trong file "ratings" thõa mãn userId = userId trong file s2 và movieId != input_movieId

def s3(rating_file):
    ratings_data = open(rating_file, "r").readlines()[1:]
    users_data = open("s2.csv", "r").readlines()
    input_data = open("input.csv", "r").readlines()[1:]

    input_movie_and_ratings = [] # [movieId][rating] của input
    recomment_user = [] # Danh sách user để gợi ý

    for ln in input_data:
        ln = ln.split(",")
        input_movie_and_ratings.append([ln[1], ln[2]]) # [movieId][rating]

    for ln in users_data:
        ln = ln.split(",")
        recomment_user.append(ln[0])

    f = open("s3.csv", "w")
    for ln in ratings_data:
        ln_split = ln.split(",")
        pair = [ln_split[1], ln_split[2]]

        if ln_split[0] in recomment_user and pair not in input_movie_and_ratings and float(ln_split[2]) >= 4:
                f.write(ln)
    f.close()


# ====================================STEP4====================================
# Đưa ra movieId, số người đánh giá, điểm đánh giá trung bình
def s4():

    data = open("s3.csv", "r").readlines()

    count_dict = {} # Lưu số người đánh giá theo movieId
    sum_dict = {} #Lưu tổng điểm đánh giá theo movieId
    
    for n in range(0, len(data)):
        row1 = data[n].split(",")
        count1 = int(row1[1].strip())
        temp_sum = float(row1[2].strip())

        if count1 not in count_dict:
            count_dict[count1] = 0
            sum_dict[count1] = 0
        if count1 in count_dict:
            count_dict[count1] += 1
            sum_dict[count1] += temp_sum

    count_sorted = sorted(count_dict.items(),reverse = True, key = lambda x: x[0])
    sum_sorted = sorted(sum_dict.items(),reverse = True, key = lambda x: x[0])

    counts = []
    sums = []
    avgs = []

    for count in count_sorted:
        counts.append(count[1])

    for temp_sum in sum_sorted:
        sums.append(temp_sum[1])

    for i in range(0, len(counts)):
        temp_arg = sums[i] / counts[i]
        avgs.append(temp_arg)

    f = open("s4.csv", "w")
    i = 0
    for count in count_sorted:
        f.write(str(count[0]) + ',' + str(count[1]) + ',' + str(avgs[i]) +'\n')
        i += 1
    f.close()


# ====================================STEP5====================================
# Đưa ra danh sách film gợi ý với điểm đánh giá trung bình (min_avg_rating) và số người đánh giá (min_user_count_rating) được xác định

def s5(min_avg_rating, min_user_count_rating):
    
    movies = []
    with open("ml-movies.csv", encoding="utf8") as f:
        for row in f:
            movies.append(row)
    rec_data = open("s4.csv", "r").readlines()

    with open("s5.csv", "w") as f:
        f.write(','.join(['movieId', 'agreeCount', 'avgRating', 'title', 'genres', '\n']))

    for ln in rec_data:
        ln2 = ln.split(",")
        movie = ln2[0]
        user_count_rating = int(ln2[1])
        avg_rating = float(ln2[2])
        


        if avg_rating >= min_avg_rating and user_count_rating >= min_user_count_rating:
            for row in movies:
                row = row.split(",", 1)
                if movie == row[0]:
                    movie_title_genre = row[1]
                    with open("s5.csv", "a") as f:
                        f.write(ln.strip() + ',' + movie_title_genre)

def check():
    check_file = open("check.csv", "r").readlines()
    output_file = open("s5.csv", "r").readlines()

    check = []
    output = 0

    for line in check_file:
        line_temp = line.split(",")
        film = line_temp[1].strip()
        rating = float(line_temp[2].strip())
        if rating >= 3:
            check.append(film)

    for line in output_file:
        line_temp = line.split(",")
        if line_temp[0] in check:
            output += 1

    output_percent = (output / len(check))*100

    print("Ti le chinh xac " + str(output_percent) + " %")


if __name__ == '__main__':


    input_file_name = "input.csv"
    # ratings_file_name = "20m-ratings.csv"
    # input_file_name = "input-check.csv"
    ratings_file_name = "100k-ratings.csv"
    film_rating_counts_percent = 0.8 #Số bộ fiml đánh giá giống nhau giữa input.csv và rating.csv
    min_avg_rating = 3.0 #Điểm đánh giá trung bình tối thiểu
    min_user_count_rating_percent = 0.8 #Số lượng người đánh giá tối thiểu

    
    
    s1(input_file_name, ratings_file_name)
    user_lengh = s2(film_rating_counts_percent)
    s3(ratings_file_name)
    s4()
    min_user_count_rating = user_lengh * min_user_count_rating_percent
    s5(min_avg_rating, min_user_count_rating)

    
    print("số user gợi ý " + str(user_lengh))
    print( "Số user tối thiểu " + str(min_user_count_rating))

    check()


    #================================================================================================
    # rating_intput = open("20m-ratings.csv", "r").readlines()[1:]
    # rating_intput_before = rating_intput[0].split(",")
     
    # for line in rating_intput:
    #     user_data = open("user-data.csv", "a")
    #     line_split = line.split(",")

    #     if int(line_split[0]) == int(rating_intput_before[0]):
    #         if float(line_split[2].strip()) >= 3:
    #             rating_intput_before = line_split
    #             user_data.write(line)
    #             user_data.close()
    #     else:
            
    #         user_data = open("user-data.csv", "r").readlines()
    #         f1 = open("input-check.csv", "w")
    #         f2 = open("check.csv", "w")
    #         lengh = len(user_data)*0.8
    #         for i in range(0, len(user_data)):
    #             if i< lengh:
    #                 f1.write(user_data[i])
    #             else:
    #                 f2.write(user_data[i])
    #         f1.close()
    #         f2.close()

    #         # input_file_name = "input.csv"
    #         # ratings_file_name = "20m-ratings.csv"
    #         input_file_name = "input-check.csv"
    #         ratings_file_name = "100k-ratings.csv"
    #         film_rating_counts_percent = 0.8 #Số bộ fiml đánh giá giống nhau giữa input.csv và rating.csv
    #         min_avg_rating = 4.0 #Điểm đánh giá trung bình tối thiểu
    #         min_user_count_rating_percent = 0.8 #Số lượng người đánh giá tối thiểu
    #         film_rating_counts_percent = 0.8
           
            
    #         s1(input_file_name, ratings_file_name)
    #         user_lengh = s2(film_rating_counts_percent)
    #         s3(ratings_file_name)
    #         s4()
    #         min_user_count_rating = user_lengh * min_user_count_rating_percent
    #         s5(min_avg_rating, min_user_count_rating)

            
    #         print("So user goi y " + str(user_lengh))
    #         print( "So user toi thieu " + str(min_user_count_rating))

    #         check()


    #================================================================================================


    

    

