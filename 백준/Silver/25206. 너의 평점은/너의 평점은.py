ab=0
add=0
for _ in range(20):
    a, b = map(str, input().split()[1:])  # a: 학점, b: 등급
    grade=0  # 등급 숫자변환
    if 'P' in b:
        a=0
    elif 'F' in b:
        grade+=0
    elif '+' in b:
        grade+=0.5
        if 'A' in b:
            grade+=4
        elif 'B' in b:
            grade+=3
        elif 'C' in b:
            grade+=2
        elif 'D' in b:
            grade+=1
    else:
        if 'A' in b:
            grade+=4
        elif 'B' in b:
            grade+=3
        elif 'C' in b:
            grade+=2
        elif 'D' in b:
            grade+=1
    ab+=float(a)*grade  # ab: 학점*과목평점
    add+=float(a)  # add: 학점의 합
print(ab/add)