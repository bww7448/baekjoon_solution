import pickle
import os
import re
import sqlalchemy as db
from sqlalchemy.sql import text
import cx_Oracle

#################################################################################

###################################################################################
def main() :
    student = []
    name = ''
    kor_s = 0
    math_s = 0
    eng_s = 0
    os.environ['NLS_LANG'] = '.UTF8'
    engine = db.create_engine("oracle://hr:hr@localhost:1521/xe") 
    # student = []
    student = load_cust(student, engine)
    print(student)
    while True:
        print("""
    다음 중 작업하실 메뉴를 선택하세요
    I : 성적 입력
    S : 과목별 성적 조회
    P : 학생별 성적 조회
    U : 학생 성적 수정
    D : 학생 성적 삭제
    Q : 프로그램 종료""")
        sel_main = input("원하시는 작업을 선택해 주세요 :  ").strip().upper()
        if sel_main == "I":
            sel_I(student, name, kor_s, math_s, eng_s)
        elif sel_main == "S":
            sel_S(student)
        elif sel_main == "P":
            sel_P(student)
        elif sel_main == "U":
            sel_U(student)
        elif sel_main == "D":
            sel_D(student)
        elif sel_main == "Q":
            break
        else :
            print("다시 입력해 주세요.", end = "  ")
    return student
#################################################################################
#################################################################################
def sel_I(student, name, kor_s, math_s, eng_s):
    print("성적 입력란입니다.")
    name = ''
    point = 0
    i = 0
    score = {"name":"", "kor":"", "math":"", "eng":""}
    name = input("이름을 입력해 주세요 : " )
    #ins_score(kor_s, math_s, eng_s)
    while i < 4 :
        if i == 0 :
            sub = "국어"
            i = i  + 1
        elif i == 1 :
            sub = "수학"
            kor_s = point
            i = i  + 1
        elif i == 2 :
            sub = "영어"
            math_s = point
            i = i  + 1
        elif i == 3:
            eng_s = point
            i = i + 1
            break
        print('%s' % sub, "점수를 입력해 주세요.")
        point = input()
        if 0 <= int(point) <=100 :
            pass
        else:
            print("잘못 입력하셨습니다.")
            i = i-1
    score["name"] = name
    score["kor"] = kor_s
    score["math"] = math_s
    score["eng"] = eng_s
    student.append(score)
    print((len(student)-1), "번 학생이 저장 됐습니다.")
    return name, kor_s, math_s, eng_s, student

#################################################################################
#################################################################################
def ins_score(kor_s, math_s, eng_s) : 
    i = 0
    point = 0
    kor_s = 0
    math_s = 0
    eng_s = 0
    while i < 4 :
        if i == 0 :
            sub = "국어"
            i = i  + 1
        elif i == 1 :
            sub = "수학"
            kor_s = point
            i = i  + 1
        elif i == 2 :
            sub = "영어"
            math_s = point
            i = i  + 1
        elif i == 3:
            eng_s = point
            i = i + 1
            break
        print('%s' % sub, "점수를 입력해 주세요.")
        point = input()
        if type(point) == "int" :
            if int(point) >= 0 and int(point) <= 100 :
                pass
            else : 
                print("0 ~ 100의 숫자를 입력해 주세요.")
                i = i-1
        else : 
            print("잘못입력하셨습니다.")
    return kor_s, math_s, eng_s
#################################################################################
#################################################################################
def sel_S(student):
    while True :
        print("""
과목별 점수 조회 화면입니다.
원하는 작업을 골라주세요
kor : 국어 점수 조회
math : 수학 점수 조회
eng : 영어 점수 조회
max : 최고 점수 조회
min : 최저 점수 조회
back : 뒤로 가기 """)
        sub_s = input()
        if sub_s in ("kor", "math", "eng") : 
            sub_s2 = sub_s.replace("kor", "국어")
            sub_s2 = sub_s2.replace("math", "수학")
            sub_s2 = sub_s2.replace("eng", "영어")
            print('%s' % sub_s2, "과목입니다.")
            for i in range(len(student)) : 
                print(student[i]["name"],"  ", student[i][sub_s], "점")
            break
        elif sub_s in ("max", "min") :
            comparison = []
            m_name = []
            while True : 
                print ("""
어떤 과목을 조회할까요""")
                sub_s2 = input("""
kor : 국어점수
math : 수학점수
eng : 영어점수
""")
                if sub_s2 in ("kor", "math", "eng") : 
                    for i in range(len(student)):
                        comparison.append(int(student[i][sub_s2]))
                            
                    if sub_s == "max" : 
                        a1 = max(comparison)
                    else :
                        a1 = min(comparison)
                    for i in range(len(student)):
                        if a1 == int(student[i][sub_s2]):
                            m_name.append(student[i]["name"])


                    sub_s2 = sub_s2.replace("kor", "국어 ")
                    sub_s2 = sub_s2.replace("math", "수학 ")
                    sub_s2 = sub_s2.replace("eng", "영어 ")
                    sub_s = sub_s.replace("max", "최고")
                    sub_s = sub_s.replace("min", "최저")
                    for i in range (len(m_name)):
                        print ("{} 득점자는".format(sub_s), m_name[i], "이고")
                    print("{} {}".format(sub_s2, sub_s), "점수는 ", a1, "점 입니다.")
                    break
                else :
                    print("다시 입력해 주세요.")
        elif sub_s in ("back") :
            break
        else : 
            print("다시 입력해 주세요.")
#################################################################################
#################################################################################
def sel_P(student):
    stu_s = input("""
조회할 학생 이름을 입력해 주세요. :  """)
    r1 = 0
    for i in range(len(student)) : 
        if student[i]["name"] == stu_s :
            print(student[i])
            r1 = r1+1
            break
    if r1 == 0:
        print("학생이 없습니다.")
#################################################################################
#################################################################################
def sel_U(student):
    while True :
        stu_u = input("""
    수정할 학생 이름을 입력해 주세요.
    취소를 원하시면 Q를 입력해 주세요 : """)
        if stu_u == "Q":
            break
        else :
            r1 = 0
            for i in range(len(student)) :
                if student[i]["name"] == stu_u :
                    r1 = r1+1
                    print (
        "%s" %stu_u,"의 정보입니다.",
        student[i])
                    while True :
                        stu_u2 = input(
            """수정할 과목을 입력해 주세요(국어, 수학, 영어, 취소)  """)
                        stu_u3 = stu_u2.replace("국어", "kor")
                        stu_u3 = stu_u3.replace("수학", "math")
                        stu_u3 = stu_u3.replace("영어", "eng")
                        # while True :
                        if stu_u3 in ("kor", "math", "eng"):
                            stu_u4 = input("""
        몇점으로 수정하시겠습니까  """)
                            student[i][stu_u3] = stu_u4
                            print("""
        {0}의 {1}점수가 {2}점으로 수정됐습니다.""".format(stu_u, stu_u2, stu_u4))
                            break
                        elif stu_u2 == "취소":
                            break
                        else : 
                            print("잘못입력하셨습니다.")
            if r1 == 0:
                    print("다시 입력해 주세요")
            else : 
                break
    return student
#################################################################################
#################################################################################
def sel_D(student):
    while True:
        r1 = 0
        stu_d = input("""
삭제할 학생 이름을 입력해 주세요.""")
        for i in range (len(student)):
            if stu_d == student[i]["name"]:
                del student[i]
                print("%s" %stu_d, "의 정보가 삭제됐습니다.")
                r1 = r1+1
                break
        if r1 == 0:
            print("학생 이름이 없습니다.")
        else : break
#################################################################################
#################################################################################
def load_cust(student, engine):
    with engine.connect() as conn:
        result = conn.execute("SELECT * FROM score")
        student = [dict(row) for row in result]
    return student
            





main()


##앞으로 구현해야 할것
##오라클 디벨로퍼랑 연결하기
##student list에 '반' 넣고 과목별, 개인별, 반별 평균, 표준편차 구해보기
##t분포,F분포 이용해서 검추정 및 회귀분석 이용해서 회귀분석 구현하기
##가능하다면 html 과 연결해서 html(f.e)-python-오라클(b.e)로 연결되게 만들기