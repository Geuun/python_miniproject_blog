<h1> python_miniproject_blog </h1>
๐ python ๊ธฐ๋ณธ ๋ฌธ๋ฒ์ผ๋ก ๋ธ๋ก๊ทธ ๊ธฐ๋ฅ ๊ตฌํํด๋ณด๊ธฐ !

---

<h4> ํ๋ก์ ํธ ์ค๊ณ </h4>

- ํ๋ก๊ทธ๋จ ๊ธฐ๋ฅ **(CRUD)** ์ ๊ตฌํํ์.
  - C : Create
  - R : Read
  - U : Update
  - D : Delete

---

<h4>๊ธฐ๋ฅ</h4>

- ๋ฉ๋ด ์ถ๋ ฅํ๊ธฐ (Read)
- ๊ฒ์๊ธ ์ฐ๊ธฐ (Create)
- ๊ฒ์๊ธ ์ ์ฅํ๊ธฐ (Create)
- ๊ฒ์๊ธ ์์ ํ๊ธฐ (Update)
- ๊ฒ์๊ธ ์ญ์ ํ๊ธฐ (Delete)
- ๊ฒ์๊ธ ๋ก๋ฉํ๊ธฐ (Read)
- ๊ฒ์๊ธ ๋ชฉ๋ก ํ์ธํ๊ธฐ (Read)
- ๊ฒ์๊ธ ์์ธ ํ์ธํ๊ธฐ (Read)

---

<h4>๊ฒ์๊ธ ( Class๋ก ๊ตฌํ )</h4>

์์ฑ

- ๊ธ ๋ฒํธ, ์ ๋ชฉ, ๋ณธ๋ฌธ๋ด์ฉ, ์กฐํ์

๋งค์๋

- ๊ฒ์๋ฌผ ์์ ํ๊ธฐ, ์กฐํ์ ์ฆ๊ฐํ๊ธฐ, ์์ฑ ๊ฐ์ ธ์ค๊ธฐ

---

<h4>๊ฒ์๊ธ ๋ก๋ฉํ๊ธฐ</h4>

- if data.csv ํ์ผ์ด ์์ผ๋ฉด
  -> **๊ฒ์๊ธ์ ๋ก๋ฉํ๋ค.**

- if data.csv ํ์ผ์ด ์์ผ๋ฉด
  -> **data.csv ํ์ผ์ ๋ง๋ ๋ค.**

- ๊ฒ์๊ธ ๋ก๋ฉํ๊ธฐ Logic  
  -> data.csv ํ์ผ์ ์ฝ๋๋ค.  
  -> ๋ฐ์ดํฐ ํ์ค ๋ง๋ค  
  -> Post ์ธ์คํด์ค๋ฅผ ๋ง๋ ๋ค.  
  -> Post ๋ฆฌ์คํธ์ ์ธ์คํด์ค๋ฅผ ์ ์ฅํ๋ค.

---

<h4>๋ฉ๋ด ์ถ๋ ฅํ๊ธฐ</h4>

```
- My Blog -
- ๋ฉ๋ด๋ฅผ ์ ํํด ์ฃผ์ธ์ -
1. ๊ฒ์๊ธ ์ฐ๊ธฐ
2. ๊ฒ์๊ธ ๋ชฉ๋ก
3. ํ๋ก๊ทธ๋จ ์ข๋ฃ
```

---

<h4>๊ฒ์๊ธ ์ฐ๊ธฐ</h4>

๊ฒ์๊ธ ๋ฑ๋ก

1. Post ์ธ์คํด์ค ์์ฑ
2. Post ๋ฆฌ์คํธ์ ์ ์ฅ

Post ์ธ์คํด์ค

- ๊ธ๋ฒํธ
  - ํ์ฌ post_list์ ๋ง์ง๋จน ์์์ id๊ฐ + 1
- ์ ๋ชฉ
- ๋ด์ฉ
- ์กฐํ์

---

<h4> ๊ฒ์๊ธ ๋ชฉ๋ก</h4>

๊ธ ๋ฒํธ ์ ํ

- ์๋ ๊ธ ๋ฒํธ
  - ๋ฌดํ๋ฐ๋ณต

- -1 ์๋ ฅ
  - ๋ฉ๋ด๋ก ๋ณต๊ท

- ์ฌ๋ฐ๋ฅธ ๊ธ ๋ฒํธ
  - ๊ฒ์๊ธ ์์ธ ํ์ด์ง

---

<h4> ๊ฒ์๊ธ ์์ธ ํ์ธํ๊ธฐ </h4>

๊ฒ์๊ธ ์์ธ

- ์ฌ์ฉ์๊ฐ ์๋ ฅํ ๊ธ ๋ฒํธ์ ๊ฐ์ ๊ฒ์๊ธ์ ์ฐพ๊ธฐ

- ์กฐํ์ ์ฆ๊ฐ ๋ฐ ์์ธ ๋ด์ฉ ์ถ๋ ฅ

- ์์ , ์ญ์  ๊ธฐ๋ฅ์ ์ํํ  ๋ Post ๊ฐ์ฒด ๋๊ฒจ์ฃผ๊ธฐ

---

<h4> ๊ฒ์๊ธ ์์ , ์ญ์ , ์ ์ฅํ๊ธฐ </h4>

๊ฒ์๊ธ ์์ 

- ์ฌ์ฉ์๊ฐ ์๋ก ์ ๋ชฉ, ๊ธ ๋ด์ฉ์ ์๋ ฅํ๋ค
   set_post ๋ฉ์๋๋ก Post ๊ฐ์ฒด๋ฅผ ์์ ํ๋ค.

๊ฒ์๊ธ ์ญ์ 

- post_list์์ ํด๋น Post ๊ฐ์ฒด๋ฅผ ์ญ์ ํ๋ค.

๊ฒ์๊ธ ์ ์ฅํ๊ธฐ

- post_list์ ์ ์ฅ๋ ๋ด์ฉ์ data.csv ํ์ผ์ ์ ์ฅํ๊ธฐ

---