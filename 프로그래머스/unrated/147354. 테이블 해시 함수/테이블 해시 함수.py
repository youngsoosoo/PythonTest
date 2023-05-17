### 문제 인식 ###
# data, col, row_begin, row_end가 주어진다.
# 해당 변수들을 이용해 주어진 규칙에 따라 생성되는 해시함수를 구현하면 되는 문제이다.
### 문제 해결 ###
# 조건 2에 맞게 데이터를 정렬해줍니다.
# 조건 3에 맞게 정렬된 데이터에서 row_begin, row_end+1 두 수 사이의 모든 값을 i라고 함.
# data[i]의 값을 모두 꺼내서 j라고 칭함. j를 i로 나눈 나머지들의 합을 구해서 total에 더해줍니다.
# 누적된 total에 대해 XOR 연산을 해 answer로 반환
def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col-1], -x[0]))
    for i in range(row_begin, row_end+1):
        total = 0
        for j in data[i - 1]:
            total += (j % i)
        answer ^= total

    return answer