<h1> python_miniproject_blog </h1>
📝 python 기본 문법으로 블로그 기능 구현해보기 !

---

<h4> 프로젝트 설계 </h4>

- 프로그램 기능 **(CRUD)** 을 구현하자.
  - C : Create
  - R : Read
  - U : Update
  - D : Delete

---

<h4>기능</h4>

- 메뉴 출력하기 (Read)
- 게시글 쓰기 (Create)
- 게시글 저장하기 (Create)
- 게시글 수정하기 (Update)
- 게시글 삭제하기 (Delete)
- 게시글 로딩하기 (Read)
- 게시글 목록 확인하기 (Read)
- 게시글 상세 확인하기 (Read)

---

<h4>게시글 ( Class로 구현 )</h4>

속성

- 글 번호, 제목, 본문내용, 조회수

매서드

- 게시물 수정하기, 조회수 증가하기, 속성 가져오기

---

<h4>게시글 로딩하기</h4>

- if data.csv 파일이 있으면
  -> **게시글을 로딩한다.**

- if data.csv 파일이 없으면
  -> **data.csv 파일을 만든다.**

- 게시글 로딩하기 Logic
  -> data.csv 파일을 읽는다
  -> 데이터 한줄 마다
  -> Post 인스턴스를 만든다.
  -> Post 리스트에 인스턴스를 저장한다.

---
