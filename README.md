

# How to encrypt MIRA program?

<br/>

### 1. create table in random numbers

> table = [564, 465, 201 ... 324, 782, 328]

<br/>

### 2. change data to unicode

> 'a' -> 97 (== ord('a'))

<br/>

### 3. multiply changed data and table

> [564, 465, 201, ... 324, 782, 328] * [97(=='a'), 98(=='b'), ... 112(=='p'), 113(=='q')]

<br/>

### 4. save encrypted data in file

> 124245 1242123 43654374 7547 76585768 2354 ... -> abc.txt

<br/>

### 5. send table to server

> server.emit(table)

<br/>