#!/usr/bin/env python

import csv
# import numpy as np

# Lấy ra userId,movieId,rating trong file "ratings" thõa mãn movieId = input_movieId và rating = input_rating

input_file = "input.csv"
ratings_file = "ratings_test.csv"
min_film_rating_counts_percent = 0.8 #Số bộ fiml đánh giá giống nhau giữa input.csv và rating.csv
min_user_count_rating_percent = 0.8 #Số lượng người đánh giá tối thiểu

ratings_data = open(ratings_file, "r").readlines()[1:]
input_data = open(input_file, "r").readlines()[1:]

input_user = []
input_movie = []
input_movie_and_ratings = [] # [movieId][rating] của input

for ln in input_data:
    ln = ln.split(",")
    input_movie.append(ln[1])
    input_movie_and_ratings.append([ln[1], ln[2]]) # [movieId][rating]
    if ln[0] not in input_user:
        input_user.append(ln[0])


# print("Input user len = ", len(input_user))
# print(input_user)

# print("Input movies len = ", len(input_movie))
# print(input_movie)

# print("input movies and ratings len ", len(input_movie_and_ratings))
# print(input_movie_and_ratings)

# if '29' in [a[0] for a in input_movie_and_ratings]:
#     print("yes")


with open("s1.csv", "w") as s1:
    for ln in ratings_data:
        ln_temp = ln.split(",")
        if ln_temp[1] in input_movie:
            if (str(ln_temp[0]) not in input_user and str(ln_temp[1]) in input_movie and float(ln_temp[2]) > 3 ):
                s1.write(ln)
s1.close()

# Lấy ra danh sách userId, filmRatingCounts với filmRatingCounts là số bộ film có cùng đánh giá với input_user.
# filmRatingCounts >= min_film_rating_counts (số bộ phim có cùng đánh giá tối thiểu tối thiểu)

s1_data = open("s1.csv", "r").readlines()
s2 = open("s2.csv", "w")
movies_counts_ratings = {} #movies and ratings của input user
recomment_user = [] # Danh sách user để gợi ý
for n in range(0, len(s1_data)):
    ln = s1_data[n].split(",")
    key = ln[0].strip()
    if(key in movies_counts_ratings.keys()):
        movies_counts_ratings[key] += 1
    else:
        movies_counts_ratings[key] = 1

# print("Movies and ratings count")
# print(movies_counts_ratings)

max_film_rating_counts = len(input_movie)
min_film_rating_counts = min_film_rating_counts_percent * max_film_rating_counts

print("Số lượng phim input", max_film_rating_counts)
print("Số lượng phim tương đồng tối thiểu", min_film_rating_counts)


for item in movies_counts_ratings.items():
    if item[1] >= min_film_rating_counts:
        s2.write(str(item[0])+ "," + str(item[1])+ "\n")
        recomment_user.append(item[0])

s2.close()



# Lấy ra userId,movieId,rating trong file "ratings" thõa mãn userId = userId trong file s2 và movieId != input_movieId

s3 = open("s3.csv", "w")
for ln in ratings_data:
    ln_split = ln.split(",")
    pair = [ln_split[1], ln_split[2]]

    if ln_split[0] in recomment_user and pair not in input_movie_and_ratings and float(ln_split[2]) > 3:
            s3.write(ln)
s3.close()



# Đưa ra movieId, số người đánh giá

s3 = open("s3.csv", "r").readlines()
counts_dict = {} # key = movieId, item = count ratings

for ln in s3:
    ln = ln.split(",")
    count1 = int(ln[1].strip())

    if count1 not in counts_dict:
        counts_dict[count1] = 1
    else :
        counts_dict[count1] += 1

# print("Danh sách movies and ratings count")
# print(counts_dict)


# Đưa ra danh sách film gợi ý với điểm đánh giá trung bình (min_avg_rating) và số người đánh giá (min_user_count_rating) được xác định
user_lengh = len(recomment_user)
min_user_count_rating = user_lengh * min_user_count_rating_percent

print("Số user tương đồng: ", user_lengh)
print("Số user tương đồng tối thiểu: ", min_user_count_rating)
    
movies = open("ml-movies.csv", encoding="utf8").readlines()[1:]


with open("s4.csv", "w") as f:
    f.write(','.join(['movieId', 'agreeCount', 'title', 'genres', '\n']))
f.close()

for item in counts_dict.items():
    movie_id = int(item[0])
    user_count_rating = int(item[1])
    # print("movieId = ", movie_id)
    # print("user count rating = ",user_count_rating)
    if user_count_rating >= min_user_count_rating:
        for row in movies:
            row = row.split(",", 1)
            if int(row[0]) == movie_id:
                movie_title_genre = row[1]
                with open("s4.csv", "a") as s4:
                    s4.write(str(item[0]) + ',' + str(item[1]) + ',' + movie_title_genre)






    

    

