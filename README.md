

# How to encrypt MIRA program?

<br/>

### 1. create table in random numbers

> table = [564, 465, 201 ... 324, 782, 328]

![random_table](https://user-images.githubusercontent.com/71556009/169689365-c79f1a3f-9eff-4ecb-932c-fbc80c32167a.PNG)

<br/>

### 2. change data to unicode and multiply with table

>[564, 465, 201, ... 324, 782, 328] * [97(=='a'), 98(=='b'), ... 112(=='p'), 113(=='q')]

![emcrypt_data](https://user-images.githubusercontent.com/71556009/169689375-5691d821-56c1-4e64-a7bf-794466fdfdcd.PNG)

<br/>

### 3. save encrypted data in file

> 124245 1242123 43654374 7547 76585768 2354 ... -> abc.txt

![file_save](https://user-images.githubusercontent.com/71556009/169689401-e985b309-1c79-4932-9294-8bca3041f820.PNG)

<br/>

### 4. send table to server

> server.emit(table)

![emit](https://user-images.githubusercontent.com/71556009/169689495-ee95dd36-c601-40c1-b865-5d183525e5b0.PNG)

<br/>