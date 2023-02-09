import sys
sys.stdin = open('input.txt', encoding= 'utf-8')

def search(pattern, char):
    # 어디까지 동일한 값을 가지고 있는지 확인
    for i in range(len(pattern)-2 , -1, -1):
        # 동일한 값이 있다면
        if pattern[i] == char:
            return len(pattern) -i -1
    # 없으면
    return len(pattern)


def boyrt_moore(pattern, target):
    count = 0
    t_idx = 0

    # 조사 범위가 조금 다르다
    # 조사 대상 idx가 전체 길이 - 패턴길이를 넘기 전까지
    while t_idx <= len(target) - len(pattern):
        # 뒤에서부터 조사
        p_idx = len(pattern) -1
        # p_idx가 0이 되기 전까지
        while p_idx >= 0:
            # 두 조사 대상이 같지 않을 때
            if pattern[p_idx] != target[t_idx + p_idx]:
                # 다음 조사 위치로 이동하기 위한 값을 만들어야 한다.
                next = search(pattern, target[t_idx + len(pattern)-1])
                break
            p_idx -= 1
        if p_idx == -1:
            count += 1
            t_idx += 1
        # 아니면?
        else:
            t_idx += next
    return count



for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()

