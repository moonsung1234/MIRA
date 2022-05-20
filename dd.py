
count = 0

def call() :
    global count
    
    count += 1

    if count >= 4 :
        print("실행가능한 횟수를 초과하셨습니다.")

    else :
        print("안녕하세요")





call()
call()
call()