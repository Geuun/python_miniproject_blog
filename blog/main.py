import os

# data.csv 파일 경로
file_path = "./blog/data.csv"

# data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    pass
else:
    # data.csv 파일이 없다면 파일 생성하기
    f = open(file_path, "w", encoding="utf8", )
    f.close()
