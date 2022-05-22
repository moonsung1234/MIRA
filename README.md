

# How to encrypt MIRA program?

<br/>

### 1. create table in random numbers

> table = [564, 465, 201 ... 324, 782, 328]

![random_table](https://user-images.githubusercontent.com/71556009/169689365-c79f1a3f-9eff-4ecb-932c-fbc80c32167a.PNG)

<br/>

### 2. change data to unicode

> 'a' -> 97 (== ord('a'))

### 3. multiply changed data and table

> [564, 465, 201, ... 324, 782, 328] * [97(=='a'), 98(=='b'), ... 112(=='p'), 113(=='q')]

![emcrypt_data](https://user-images.githubusercontent.com/71556009/169689375-5691d821-56c1-4e64-a7bf-794466fdfdcd.PNG)

<br/>

### 4. save encrypted data in file

> 124245 1242123 43654374 7547 76585768 2354 ... -> abc.txt

![file_save](https://user-images.githubusercontent.com/71556009/169689401-e985b309-1c79-4932-9294-8bca3041f820.PNG)

<br/>

### 5. send table to server

> server.emit(table)

<br/>