# Implementation 구현

- 머릿속에 있는 알고리즘을 저확하고 빠르게 프로그램으로 작성하기

## 아이디어를 코드로 바꾸는 구현

### 피지컬로 승부하기
- 다음과 같은 문제도 구현 부분에 포함하였습니다.
    - `완전탐색`: 모든 경우의 수를 다 계산하는 방식
    - `시뮬레이션`: 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행하는 방식


### 구현 시 고려해야 할 메모리 제약 사항
- C/C++에서는 자료형의 범위까지 생각해서 코디해야 했습니다.
    - int[4바이트]: -2,147,483,648 ~ 2,147,438,647
    - long long[8바이트]: ~~
    - BigInteger(클래스): 제한없음
- 하지만 Python에서는 정수형 범위, 실수형 범위 때문에 고민하지 않아도 됩니다.


#### 파이썬에서 리스트 크기
- 대체로 코딩테스트에서는 128~512MB정도의 메모리를 제한하는데, 경우에 따라서 수백만 개의 데이터를 처리하는 경우가 있기 때문에 대략적인 크기를 알고 있는 것이 도움이 될 수 있습니다.
- 리스트 길이 별 메모리 사용량
    - 1,000 : 약 4 KB
    - 1,000,000 : 약 4MB
    - 10,000,000 : 약 40 MB (천만)

- 일반적인 코딩테스트 수준에서는 메모리 사용량 제한보다 더 적은 크기의 메모리를 사용해야 한다는 점만 기억해두자.

### 채점환경
- 보통 제한시간과 제한 메모리를 알려줍니다.
- python은 C++보다 속도가 느린데, 1초에 2000만번 연산을 수행한다고 가정하고 문제를 풀면 실행 시간 제한에 안정적입니다.
    - 제한 시간이 1초, 데이터 개수가 100만개인 문제가 있다면 일반적으로 시간복잡도 O(NlogN) 이내의 알고리즘을 이용하여 문제를 풀어야 합니다.

### 구현 문제에 접근하는 방법
- 고차원적인 사고력을 요구하는 문제는 나오지 않는 편입니다.
- 사소한 입력 조건 등을 문제에서 명시해주며 문제의 길이가 꽤 긴 편입니다.

- pypy3은 c++에 버금갈 정도로 빠릅니다. 1초에 2000만번~1억번 연산가능


### 예제 4-1 상하좌우
- 110p
```python
n = 5
direct = {
    'L': [-1, 0],
    'R': [1, 0],
    'U': [0, -1],
    'D': [0, 1],
}

x, y = 1, 1

run = ['R', 'R', 'R', 'U', 'D', 'D']

for r in run:
    d = direct[r]
    if x+d[0] >=1 and x+d[0]<=n and y+d[1]>=1 and y+d[1]<=n:
        x += d[0]
        y += d[1]

print(x, y) # 4 3 
```

### 예제 4-2 시각
- 113p

```python
n = 5

h, m, s = 0,0,0
count = 0

while h < n+1 :
    if s == 60:
        m += 1
        s = 0
        if m == 60:
            h += 1
            m = 0
    s+=1
    if "3" in str(h)+str(m)+str(s):
        count += 1
print(count) # 11475
```

## 문제: 왕실의 나이트
- 115p

```python
n = 8
pos = 'a1'
temp = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
move = [(-2, 1),(-2,-1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,2)]
count = 0
x = temp[pos[0]]
y = int(pos[1])

for m in move:
    if x + m[0] >=1 and x + m[0] <=n and y + m[1] >=1 and y+m[1]<=n:
        count +=1

print(count) #2
```

## 문제: 게임 개발
- 119p

```python
n, m = 4, 4
x, y = 1, 1
d = 0 ## 왼쪽으로 도는거는 (d + 3) % 4
map = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1],
]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count = 0

while True:
    d = (d+3)%4 ## 왼쪽회전
    nx = x + dx[d]
    ny = y + dy[d]
    if nx >= 0 and nx < m and ny >= 0 and ny < n and map[ny][nx] == 0:
        x, y = nx, ny
        map[ny][nx] = 2
        count += 1
    
    c = 0
    s = 0
    for i in range(4):
        if x+dx[i] >= 0 and x+dx[i] < m and y+dy[i] >= 0 and y+dy[i] < n:
            c += 1
            s += map[y+dy[i]][x+dx[i]]
    
    if c <= s:
        d = (d+2) % 4 ##뒤로회전
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= 0 and nx < m and ny >= 0 and ny < n and map[ny][nx] != 1:
            count += 1
        break

print(count) #3
            
```