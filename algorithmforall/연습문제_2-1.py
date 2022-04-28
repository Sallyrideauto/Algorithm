# 최소값 구하기
# 입력 : 숫자가 n개 들어 있는 리스트
# 출력 : 숫자 n개 중 최소값

def find_min(a):
    n = len(a)      # 입력 크기 n
    min_v = a[0]    # 리스트의 첫 번쨰 값을 최소값으로 기억
    for i in range(1, n):   # 1부터 n-1까지 반복
        if a[i] < min_v:    # 이번 값이 현재까지 기억된 최소값보다 크면
            min_v = a[i]    # 최소값을 변경
    return min_v

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min(v))