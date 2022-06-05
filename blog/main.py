import os
import csv
from secrets import choice
from post import Post

# data.csv 파일 경로
file_path = "./data.csv"

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

# 메뉴 출력하기
while True:
    print("\n\n- My BLOG -")
    print("- 메뉴를 선택해 주세요 -")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")
    # 예외 처리
    try:
        choice = int(input(">>>"))
    except ValueError:
        print("숫자를 입력해 주세요.")
    else:
        if choice == 1:
            print("게시글 쓰기")
        elif choice == 2:
            print("게시글 목록")
        elif choice == 3:
            print("프로그램 종료")
            break
