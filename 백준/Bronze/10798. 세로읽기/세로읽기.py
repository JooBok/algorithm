array=[]  # 단어 저장 리스트
for _ in range(5):
    array.append(input())
length=0  # 단어 최대 길이 확인용
for i in range(len(array)):
    if len(array[i]) > length:
        length=len(array[i])
result=''
for i in range(length):
    tmp_words=''
    for j in range(len(array)):
        try:
            tmp_words += array[j][i]
        except:
            tmp_words+=''
    result+=tmp_words
print(result)