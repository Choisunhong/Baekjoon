def zip_fun(zip):
    #중복제거
    num = sorted(set(zip))
    #인덱스 미노너리
    dic = {index: idx for idx, index in enumerate(num)}
    #리스트 저장
    res = [dic[index] for index in zip]
    return res

N = int(input())
zip = list(map(int, input().split()))

final = zip_fun(zip)
print(" ".join(map(str, final)))
