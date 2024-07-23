# [ 조건문 if ]
if "참일때 실행":
    print("참인결과")

# if 예제
a=1111
b=11
if a>=b:
    print(a-b)
if a<b:
    print(b-a)
    
# if, else
if a>=b:
    print(a-b)
else:
    print(b-a)
    
#예제
a=(input("1번째 숫자: ")),
b=(input("2번째 숫자: ")),
print()
if (a>b):
    print("처음 입력했던 {a}가 {b}보다 더 큽니다.")
if (a<b):
    print("두번째로 입력했던 {b}가 {a}보다 더 큽니다.")
    
## if만 사용한 경우

score=int(input("점수를 입력해주세요."))

# 100 이하 90 이상이면 A, 90 미만 80이상이면 B, 
# 80 미만 70이상이면 C, 70 미만 60이상이면 D, 60 미만은 F

if(100>=score>=90):
    print("A학점입니다.")
if(90>score>=80):
    print("B학점입니다.")
if(80>score>=70):
    print("C학점입니다.")
if(70>score>=60):
    print("D학점입니다.")
if(60>score):
    print("F학점입니다.")
    
## if와 else if, else를 사용한 경우

score=int(input("점수를 입력해주세요."))

if(score>=90):
    print("A학점입니다.")
elif(score>=80):
    print("B학점입니다.")
elif(score>=70):
    print("C학점입니다.")
elif(score>=60):
    print("D학점입니다.")
else:
    print("F학점입니다.")
    
## if와 else만 사용한 경우

score=int(input("점수를 입력해주세요."))

if score >= 90:
    print('A')
else:
    if score >= 80:
        print('B')
    else:
        if score >= 70:
            print('C')
        else:
            if score >= 60:
                print('D')
            else:
                print('F')

##오전, 오후 구분 프로그램
#기본형
if now_time.hour >= 12:
    print(f'현재 시간은 {now_time.hour}시, 오후입니다.')
else:
    print(f'현재 시간은 {now_time.hour}시, 오전입니다.')

##오전, 오후 구분 프로그램
#변형(최대한 짧고 최적으로)
if now_time.hour >= 12:
    print(f'현재 시간은 오후, {now_time.hour-12}시입니다.')
else:
    print(f'현재 시간은 오전, {now_time.hour}시입니다.')



##계절출력 - 일반형

month=int(input("월을 입력해주세요."))

if 5>= month >=3:
                print('봄')
elif 8>= month >=6:
                print('여름')
elif 11>= month >=9:
                print('가을')
elif month==12 or month==1 or month==2 :
                print('겨울')
else:
        print('존재하지 않는 월입니다.')
        
##계절출력 - 변형

for month in range(1,13):
    if month==12 or month<=2:
        print(f"{month}월은 winter")
    elif month<=5:
        print(f"{month}월은 spring")
    elif month<=8:
        print(f"{month}월은 summer")
    elif  month<=11:
        print(f"{month}월은 fall")