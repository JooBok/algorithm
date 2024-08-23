N = int(input())
count = 0

for _ in range(N):
    S = input()
    seen_chars = set()
    last_char = ''
    valid = True  # 조건을 만족하는지 확인하는 플래그

    for i in range(len(S)):
        if S[i] != last_char:  # 새로운 문자가 등장했을 때
            if S[i] in seen_chars:  # 이미 등장한 문자라면 잘못된 문자열
                valid = False
                break
            seen_chars.add(S[i])  # 새로운 문자를 기록
        last_char = S[i]

    if valid:
        count += 1

print(count)