import os
import csv
from post import Post

# data.csv 파일 경로
file_path = "./blog/data.csv"

# post 객체를 저장할 리스트 선언
post_list = []

# data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    print('게시글 로딩중...')
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        # Post 인스턴스 생성하기
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
else:
    # data.csv 파일이 없다면 파일 생성하기
    f = open(file_path, "w", encoding="utf8", )
    f.close()

# 출력 Test
print(post_list[0].get_title())
print(post_list[1].get_title())
