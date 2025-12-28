# 32761번: 가위바위보 타일

from collections import deque


def main():
    input()
    S = input().strip()
    assert len(set(S)) == 3
    print(min(
        solve(S, 'SPR'),
        solve(S, 'PRS'),
        solve(S, 'RSP'),
    ))


def solve(S: str, pattern: str) -> int:
    count = 0
    s_queue = deque(S)
    while s_queue[0] != pattern[0]:
        s_queue.rotate(1)
    while s_queue:
        pass
        while s_queue and s_queue[0] != pattern[0]:
            s_queue.popleft()
        if not s_queue:
            break
        s_queue.popleft()
        while s_queue and s_queue[0] != pattern[1]:
            s_queue.popleft()
        if not s_queue:
            break
        s_queue.popleft()
        while s_queue and s_queue[0] != pattern[2]:
            s_queue.popleft()
        if not s_queue:
            break
        s_queue.popleft()
        count += 1
    return len(S) - len(pattern) * count


if __name__ == '__main__':
    main()
