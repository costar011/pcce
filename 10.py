# AI 엔지니어인 현식이는 데이터를 분석하는 작업을 진행하고 있습니다.
# 데이터는 ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]으로 구성되어 있으며 현식이는 이 데이터들 중 조건을 만족하는 데이터만 뽑아서 정렬하려 합니다.

# 예를 들어 다음과 같이 데이터가 주어진다면
# data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]

def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    return answer