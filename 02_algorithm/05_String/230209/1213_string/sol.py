import sys
sys.stdin = open('input.txt', encoding= 'utf-8')


for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()

    # 조사 하려고 하는 두 대상의 조사 대상을 내가 직접 컨트롤하는
    # 인덱스로 조절하면서 비교하겠다.

    p_idx = 0
    t_idx = 0

    # 최종 결과값
    cnt = 0 # 패턴이 문장에서 몇 번 나오는지 세려고
    # 조사를 할건데 언제까지 순회 할 것이냐?
    while t_idx < len(target):
        # 두 값이 같으면 idx를 증가 시키는 일
        # if target[t_idx] == pattern[p_idx]:
        #     p_idx += 1
        #     t_idx += 1
        # # 모든 패턴에 대해서 조사를 마챴다면
        # if p_idx == len(pattern):
        #     cnt += 1 # 패턴을 찾았기 때문
        #     p_idx == 0 # 다음 위치부터는 처음부터 다시 조사

        if target[t_idx] != pattern[p_idx]:
            t_idx = t_idx - p_idx
            p_idx = -1 # 0이 아니라 -1인 이유는
        # 모든 상황에 대해서 항상 증가할 것이기 때문에
        p_idx += 1
        t_idx += 1

        if p_idx == len(pattern):
            cnt += 1 # 패턴을 찾았기 때문
            p_idx = 0 # 다음 위치부터는 처음부터 다시 조사

    print(cnt)