EIn=SNn=TFn=JPn=0 
result=[]

import time
print('학과 진입시기가 가까워지는 요즘, 어떤 학과를 갈지 고민인가요?')
time.sleep(2)
print('MBTI를 통해서 나의 성향을 알고 어떤 학과와 직업에 어울리는지 알아봐요!')
time.sleep(2)
print('검사를 너무 빨리 진행하면 오류가 생길 수 있으니, 답변을 신중하게 해주세요!')
time.sleep(3)
print('MBTI 질문은 총 40문항이고 검사는 총 10분정도 소요됩니다.')
time.sleep(3)


#이름 입력
name=input("name:")
result.append(name)

def quest(x): #선택지 반복을 위한 함수
    print(x)
    print('1.절대 아니다.','2.약간 아니다.','3.보통이다.','4.약간 그렇다.','5.매우 그렇다.')
    num=int(input())
    return num


num=0
list_num=[EIn, SNn, TFn, JPn] #각 알파벳의 수치를 담을 변수들 (ex: EIn - E or I 중 하나)
list_EI=[] #질문 받는 리스트 생성 (MBTI를 결정하는 4가지 성향을 알아내기 위한 질문)
list_SN=[]
list_TF=[]
list_JP=[]

f=open("questionEI.txt","rt",encoding='UTF8') #파일 읽기를 통한 질문 채우기
list_EI=f.read().split('\n')
f.close()

f=open("questionSN.txt","rt",encoding='UTF8')
list_SN=f.read().split('\n')
f.close()

f=open("questionTF.txt","rt",encoding='UTF8')
list_TF=f.read().split('\n')
f.close()

f=open("questionJP.txt","rt",encoding='UTF8')
list_JP=f.read().split('\n')
f.close()

list_quest=[list_EI, list_SN, list_TF, list_JP]
#질문 동률이 같은 것을 최대한 방지하기 위한 장치
list_A=[]
list_B=[]
list_C=[]
count=0

for i in range(4):
    for j in range(10):
        if j<5: #ex) E, I 선택의 경우: E에 대한 질문-양수값, I에 대한 질문-음수값으로 쌓기
            num=quest(list_quest[i][j])
            list_num[i]+=num
            list_A.append(num)
            
        elif j>=5:
            num=quest(list_quest[i][j])
            list_num[i]-=num
            list_B.append(num)
    list_A.sort()
    list_B.sort()
    for k in range(5):
        if list_A[k]>list_B[k]:
            count+=1
        else:
            count-=1
    if count>0:
        list_C.append(1)
    else:
        list_C.append(0)
    list_A.clear()
    list_B.clear()

mbti_name=[["E","I"],["S","N"],["T","F"],["J","P"]]
mbti=[]
#이중리스트
#mbti_intro=[]
for i in range(4):
    if list_num[i]>0:
        mbti.append(mbti_name[i][0])
    elif list_num[i]<0:
        mbti.append(mbti_name[i][1])
    elif list_num[i]==0:
        if list_C[i]==1:
            mbti.append(mbti_name[i][0])
        elif list_C[i]==0:
            mbti.append(mbti_name[i][1])


mbti_result=("").join(mbti)
print(mbti_result)
result.append(mbti_result)

import turtle
turtle.colormode(255)
line = turtle.Turtle()
EIt=turtle.Turtle()
SNt=turtle.Turtle()
TFt=turtle.Turtle()
JPt=turtle.Turtle()

turtles=[line, EIt, SNt, TFt, JPt]
MBTI_axis=[['P','E'],['S','T'],['J','I'],['N','F']]

for i in range(5):    
    turtles[i].speed(10)
    turtles[i].hideturtle()
    if i>0:
        turtles[i].pencolor(0,128,255)
        turtles[i].fillcolor(128,255,255)
        turtles[i].pensize(3)
        turtles[i].setheading(90)
        turtles[i].penup()


def move(a, x, y): #움직이기 위한 함수
    a.penup()
    a.goto(x,y)
    a.pendown()

def draw_circle(a, t): #원을 그리는 함수
    a.begin_fill()
    a.circle(t)
    a.end_fill()

#x축 y축 과 격자 원 그리기
move(line, -200, 0)
line.forward(400)
move(line, -200, -200)
line.left(45)
line.forward(565.685)
move(line, 0, -200)
line.left(45)
line.forward(400)
move(line, 200, -200)
line.left(45)
line.forward(565.685)
line.right(135)

for i in range(1, 3):
    move(line, 0, i*(-100))
    line.circle(i*100)

#기타 글씨쓰기
move(line, 0, 300)
line.write('MBTI 분석표', False, 'center', ('consolas', 30, 'bold'))
move(line, -210, 200)
line.penup()
for i in range(4):
    for j in range(2):
        line.write(MBTI_axis[i][j], False, 'center', ('consolas', 15, 'bold'))
        line.forward(210)
    line.right(90)


#MBTI 수치에 따른 원 그리기
def loop(i):
    if i<4:
        turtles[i+1].right(45*i)
        turtles[i+1].forward(list_num[i]*7)
        turtles[i+1].setheading(270)
        if list_num[i]<0:
             turtles[i+1].forward(list_num[i]*(-3))
             turtles[i+1].left(90)
             turtles[i+1].pendown()
             draw_circle(turtles[i+1], list_num[i]*(-3))
        else:
             turtles[i+1].forward(list_num[i]*3)
             turtles[i+1].left(90)
             turtles[i+1].pendown()
             draw_circle(turtles[i+1], list_num[i]*3)
        return loop(i+1)
loop(0)




f=open("mbti_job_list.txt",'rt',encoding="UTF8") #mbti에 해당하는 직업리스트 파일에서 불러오기
mbti_job_list=f.read().split('\n')
f.close()

mbti_job={}
for i in range(len(mbti_job_list)):
    mbti,job=mbti_job_list[i].split("-")
    mbti_job[mbti]=job

print("\n")
for values in mbti_job:
    print(mbti_job[values]) #전체 직업 print
print('\n')

s2_list=mbti_job[mbti_result].split(", ")


s1=set([])
s2=set([])

for i in range(5):
    s2.add(s2_list[i]) #mbti에 해당하는 직업 집합(s2)에 저장

print('※직업명은 띄어쓰기를 포함해서 정확히 적어주세요.')
while True:
    x=input("관심 직업을 하나 입력하시오.(없으면 '없음'을 입력) ")#전체 직업 중 관심 있는 직업 입력하고 집합(s1)에 저장
    if x=="없음":
        break
    else:
        s1.add(x)
    
    

jobs=s1.union(s2) #합집합으로 mbti별 직업과 관심 직업 구하기
job_suggest=s1.intersection(s2) #교집합 mbti에 해당하는 직업과 관심 직업 중 공통적인 직업 구하기

print("\n")
print("아래의 직업은 mbti 성향별 직업과 관심 직업입니다. ")
print(jobs)
print('\n')

joblist_input=[]
if len(job_suggest)==0: #공통적인 직업이 없을 경우 
    while True:
        print("위의 직업 중 관심있는 직업과 관심있는 정도를 입력하시오.(1~10) ") #관심있는 수치 입력받기
        y=input("이와 같이 입력하시오.(관심있는 직업:숫자)(없으면 '없음'을 입력)")
        if y=="없음":
            break
        else:
            job_input,num_input =y.split(":") #split
            joblist_input.append([job_input,int(num_input)])        
    
    for i in range(len(joblist_input)):
        print(joblist_input[i][0])
        able=int(input("위의 직업에 대해 자신의 능력이 적합 정도를 입력하시오.(1~10) "))
        joblist_input[i][1]+=able
        
    for i in range(len(joblist_input)): #수치를 내림차순으로 정렬
        for j in range(i,0,-1):
            if joblist_input[j][1]>joblist_input[j-1][1]:
                joblist_input[j],joblist_input[j-1]=joblist_input[j-1],joblist_input[j]
            else:
                break
    
    i=0
    joblist_input_same=[]
    joblist_input_same.append(joblist_input[0][0])
    while i<len(joblist_input)-1:
        if joblist_input[i][1]==joblist_input[i+1][1]:
            joblist_input_same.append(joblist_input[i+1][0])
            i=i+1
        else:
            break

    print(name+"님께 ", end='')
    for i in range(len(joblist_input_same)):
        print(joblist_input_same[i],", ",end="")
    print("(이)라는 직업을 추천합니다.")
  

elif len(job_suggest)==1:
    print("%s님께 %s(이)라는 직업을 추천합니다."%(name,job_suggest)) #공통 직업이 한 개 이상일 경우
else:
    print("%s님께 %s(이)라는 직업을 추천합니다."%(name,job_suggest))
    


job_result=input("추천받은 직업를 입력하시오.(다수 입력 불가) ")
result.append(job_result)

f=open("job_major_list.txt","rt",encoding="UTF8") #직업-학과 파일 불러오기
s=f.read().split('\n') 
f.close()

dic1={}
for i in range(len(s)):
    a,b=s[i].split("-")
    dic1[a]=b         #사전에 직업을 key로 학과를 value로 저장하기

if dic1[job_result]=="X":
    print("특정한 학과가 없습니다.")
    result.append("해당 직업에 적절한 학과가 없습니다. 다른 자격증 및 시험을 알아보세요!")
else:
    print("직업에 대한 추천 학과는",dic1[job_result],"입니다.")
    result.append(dic1[job_result])

mw=[]
f=open('MBTI 성향.txt', 'rt', encoding='UTF8')
mw=f.read().split('\n')

f.close()
for i in range(len(mw)):
    if result[1] in mw[i]:
        result.insert(2, mw[i])

mw1=result[2].split(', ')

f=open('MBTI_result.txt', 'wt', encoding='UTF8')
f.write(result[0])
f.write('님의 MBTI결과지 입니다.\n\n')
def write(a, b):
    f.write(result[0])
    f.write('님의 ')
    f.write(a)
    f.write(b)
    f.write('\n')

write('MBTI : ', result[1])
f.write('\n')
for i in range (len(mw1)):
    f.write(mw1[i])
    f.write('\n')
f.write('\n')
write('추천직업 : ', result[3])
write('추천학과 : ', result[4])
f.close()

print('검사를 마치셨습니다! MBTI_result 파일을 가서 검사를 확인하세요!')
time.sleep(10)
