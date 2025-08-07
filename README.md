김동주(Hepheir)의 백준 문제풀이 모음입니다.

[![hepheir's solved.ac stats](https://github-readme-solvedac.hyp3rflow.vercel.app/api/?handle=hepheir)](https://solved.ac/profile/hepheir)

## 커밋 컨벤션이 있습니다.

커밋 메시지는 아래와 같이 작성하고 있습니다.

```plaintext
제출결과(제출결과메타정보): 풀이시간복잡도 #알고리즘/자료구조


[체감난이도]
"Solved.ac 난이도 투표 기여 메시지"
```

> 2025년 07월 및 그 이전 커밋들은 컨벤션이 정립이 덜 되어 일부 내용이 누락되어 있을 수도 있습니다.


**제출 결과**
* AC: Accepted, 맞았습니다.
* PA: Accepted, 맞았습니다.
* WA: Wrong Answer, 틀렸습니다.
* TLE: Time Limit Exceeded, 시간 초과
* MLE: Memory Limit Exceeded, 메모리 초과

**제출 결과의 메타 정보**
* 맞았을 경우, 대체로 수행시간을 밀리 초 단위로 적습니다.
* 틀렸을 경우, 비워두거나 테스트케이스 통과 진척도를 퍼센트로 표시합니다.
* 파이썬 코드를 PyPy3 로 제출한 경우, 이를 간혹 표기하기도 합니다.

**풀이의 시간 복잡도**
* 풀이 작성자가 분석한 풀이의 전반적인 시간 복잡도를 표기합니다.
* Big-O 표기법을 사용하는 것을 목표로 합니다.
    * Big-O 표기가 어렵거나 이해를 더 어렵게 할 경우, 실제 수행시간에 비례하여 `T(f(n))` 꼴로 표기하기도 합니다.

**알고리즘/자료구조 표기**
* 한 문제에 여러 개의 DSA을 표기할 수 있습니다.
    * DSA: Data structures and Algorithms
* 가급적 `#` 기호 뒤에 공백없이 snake-case로 표기합니다.
* 가급적 Solved.ac 에서 사용하는 태그 키워드를 사용하려고 노력하나, 종종 변형하여 표기하기도 합니다.

**난이도 표기**
* 백준과 솔브드의 난이도 체계를 따릅니다.
* 각 난이도의 영문 표기의 이니셜과 숫자 조합으로 표기합니다.
    * (예시) 브론즈 V는 `B5`로 표기

## 커밋 메시지 작성 예시

맞았습니다를 받은 경우
```
AC(872ms): O(n π(n)) #sieve_of_eratosthenes #bruteforcing #number_theory

[S2]
wonowon 숫자의 길이는 O(N)으로, ...
```

PyPy3로 제출하여 맞았을 경우
```
AC(1052ms, PyPy3): O((N+M)*sqrt(N)+(M log M)) #mo's

[D5]    # 커밋 컨벤션이 정립되기 이전 커밋에는 없을 수도 있음.
```

시간 초과를 받은 경우
```
TLE: O(N^K) #recursive #dp
```

틀렸습니다를 받은 경우
```
WA(9%): #caseworks #greedy
```
