# 목록
1. [BetterWay27. map과 filter 대신 컴프리헨션을 사용하라](#betterway27-map과-filter-대신-컴프리헨션을-사용하라)
2. [BetterWay28. 컴프리헨션 내부에 제어 하위 식을 세 개 이상 사용하지 말라](#betterway28-컴프리헨션-내부에-제어-하위-식을-세-개-이상-사용하지-말라)
3. [BetterWay29. 대입식을 사용해 컴프리헨션 안에서 반복 작업을 피하라](#betterway29-대입식을-사용해-컴프리헨션-안에서-반복-작업을-피하라)
4. [BetterWay30. 리스트를 반환하기보다는 제너레이터를 사용하라](#betterway30-리스트를-반환하기보다는-제너레이터를-사용하라)
5. [BetterWay31. 인자에 대해 이터레이션 할 때는 방어적이 되어라](#betterway31-인자에-대해-이터레이션-할-때는-방어적이-되어라)
6. [BetterWay32. 긴 리스트 컴프리헨션보다는 제너레이터 식을 사용하라](#betterway32-긴-리스트-컴프리헨션보다는-제너레이터-식을-사용하라)
7. [BetterWay33. yield from을 사용해 여러 제너레ㅔ이터를 합성하라](#betterway33-yield-from을-사용해-여러-제너레ㅔ이터를-합성하라)
8. [BetterWay34. send로 제너레이터에 데이터를 주입하지 말라](#betterway34-send로-제너레이터에-데이터를-주입하지-말라)
8. [BetterWay35. 제너레이터 안에서 throw 상태를 변화시키지 말라](#betterway35-제너레이터-안에서-throw-상태를-변화시키지-말라)
8. [BetterWay36. 이터레이터나 제너레이터를 다룰 때에는 itertools를 사용하라](#betterway36-이터레이터나-제너레이터를-다룰-때에는-itertools를-사용하라)

# Chapter4 : 컴프리헨션과 제너레이터

> 컴프리헨션
- 리스트, 딕셔너리, 집합등의 타입을 간결하게 이터레이션하면서 원소로부터 파생되는 데이터 구조를 생성하는 기능이비다.
- 컴프리헨션을 사용하면 일반적인 작업을 수행하는 코드의 가독성을 높일 수 있습니다.

> 제너레이터
- 함수가 점진적으로 반환하는 값으로 이뤄지는 스트림을 만들어줍니다.
- 이터레이터를 사용할 수 있는 곳(for 루프, 별표 식 등)이라면 어디든 사용할 수 있습니다.
- 제너레이터를 사용하면 성능을 향상시키고 메모리 사용량을 줄이고 가독성을 높일 수 있습니다.


## BetterWay27. map과 filter 대신 컴프리헨션을 사용하라

- python은 시퀀스나 이터러블에서 새 리스트를 만들어내는 간결한 구분을 제공합니다. **리스트 컴프리헨션**
- 인자가 하나의 함수를 적용하는 경우가 아니라면 간단한 경우에도 `map()`내장 함수보다 `리스트 컴프리헨션`이 더 명확합니다.

```python
a= [1,2,3,4,5,6,7,8,9,10]

## 기존방법
squares = []
for x in a:
    squares.append(x**2)
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## map()
alt = map(lambda x:x**2, a)
print(alt)

## list comprehension
squares = [x**2 for x in a]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
<br>

- 만일 조건을 추가해서 짝수의 제곱만 계산한다고 한다면 다음과 같습니다.
    - 이 때에도 리스트 컴프리헨션이 맵과 필터를 사용한 것 보다 가독성이 좋습니다.

```python
## list comprehension
even_squares = [x**2 for x in a if x%2==0]
print(even_squares) # [4, 16, 36, 64, 100]

## map and filter
## 읽기힘들다
alt = map(lambda x:x**2, filter(lambda x:x%2==0, a))
print(alt) # [4, 16, 36, 64, 100]
```
<br>

- `딕셔너리`와 `집합`에도 리스트 컴프리헨션과 동등한 컴프리헨션이 있습니다.
    - 딕셔너리 컴프리헨션
    - 셋 컴프리헨션
- 이 또한 map과 filter를 사용할 수 있지만 컴프리헨션의 가독성이 더 좋습니다.
```python
## 컴프리헨션
even_squares_dict = {x: x**2 for x in a if x%2==0}
threes_cubed_set = {x**3 for x in a if x%3 == 0}
print(even_squares_dict) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
print(threes_cubed_set) # {216, 729, 27}

## map and filter
alt_dict = dict(map(lambda x: (x,x**2), filter(lambda x: x%2==0, a)))
alt_set = set(map(lambda x:x**3, filter(lambda x:x%3==0, a)))
print(alt_dict)
print(alt_set)
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
# {216, 729, 27}
```
<br>

### 기억해야 할 Point
> - 리스트 컴프리헨션은 `lambda`식을 사용하지 않기 때문에 같은 일을 하는 `map`과 `filter`내장 함수를 사용하는 것보다 명확합니다.<br>
> - 리스트 컴프리헨션을 사용하면 쉽게 입력 리스트의 원소를 건너뛸 수 있습니다.<br>
> - 딕셔너리와 셋도 컴프리헨션을 사용할 수 있습니다.<br>

<br>

## BetterWay28. 컴프리헨션 내부에 제어 하위 식을 세 개 이상 사용하지 말라

- 컴프리헨션은 기본적인 사용법 외에도 루프를 여러 수준으로 내포하도록 허용합니다.
- 행렬을 1차원으로 변환하는 예제
    - 왼쪽 `for`문 부터 차례대로 순회하면서 출력합니다.
    - 컴프리헨션에서 다중 루프를 사용하는 좋은 예
    - 

```python
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat = [x for row in matrix for x in row]
print(flat) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
<br>

- 행렬 원소를 제곱하는 예제를 하려면 컴프리헨션 안에 컴프리헨션을 추가로 해야 합니다.
```python
matrix = [[1,2,3], [4,5,6], [7,8,9]]
squared = [[x**2 for x in row] for row in matrix]
print(squared) # [[1, 4, 9], [16, 25, 36], [49, 64, 81]] 
```
<br>

- 리스트 안에 더 깊은 리스트 계층이 있으면 컴프리헨션이 복잡해집니다.
- 하지만 for문으로 구현하면 가독성이 좋아지고 순회 대상이 명확해집니다.
```python
my_list = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
flat = [x for sublist1 in my_list
        for sublist2 in sublist1
        for x in sublist2]

print(flat) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

flat2 = []
for sublist1 in my_list:
    for sublist2 in sublist1:
        flat2.extend(sublist2)

print(flat2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```
<br>

- 또한 컴프리헨션 식 바로 뒤에 `if`문을 추가해서 각 수준마다 조건을 지정할 수 있습니다.
- 행렬에서 3으로 나워 떨어지는 셀만 남기고 합계가 10 보다 더 큰 행만 맘기고 싶다고 하자.
    - 코드가 길어지지느 않지만 읽기가 힘들어집니다.

```python
matrix = [[1,2,3], [4,5,6], [7,8,9]]
filtered = [[x for x in row if x%3==0] for row in matrix if sum(row)>=10]
print(filtered) # [[6], [9]]
```
<br>

> 컴프리헨션에 들어가는 하위 식이 세 개 이상 되지 않게 제한하는 규칙을 꼭 지키는 것을 권합니다.
- 조건식 두 개, 루프 두 개, 혹은 조거문 한개와 루프 한 개 까지만 사용 권장합니다.
- 이보다 복잡해지면 컴프리헨션 보다 일반 if와 for를 사용하는 것을 지향합니다.


### 기억해야 할 Point
> - 컴프리헨션으 여러 수준의 루프를 지원하며 각 수준마다 여러 조건을 지원합니다.<br>
> - 제어 하위 식이 세 개 이상인 컴프리헨션은 이해하기 매우 어려우므로 가능하면 피해야 합니다.<br>

<br>

## BetterWay29. 대입식을 사용해 컴프리헨션 안에서 반복 작업을 피하라

- 컴프리헨션(리스트, 딕셔너리, 셋 등)에서 같은 계산을 여러 위치에서 공유하는 경우는 흔합니다.

- 재고를 파악하는 기능 예제
    - 요청품목을 받아서 주문 최소개수(8)이상인지 판별해서 보여주는 기능.
    - 반복되는 계산을 컴프리헨션으로 처리하서 간단하게 표현할 수 있습니다.
    - 하지만 `stock.get`을 활용한 `get_batch()`가 여러번 호출되어 가독성이 떨어지고, 실수할 가능성이 높아집니다.
```python
## 예제
stock = {
    '못': 125,
    '나사못': 35,
    '나비너트': 8,
    '와셔': 24,
}

order = ['나사못', '나비너트', '클립']

def get_batches(count, size):
    return count//size

result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches
print(result) # {'나사못': 4, '나비너트': 1}

## 컴프리헨션 적용하면
found = {name: get_batches(stock.get(name, 0), 8) for name in order if get_batches(stock.get(name, 0), 8)}
print(found) #{'나사못': 4, '나비너트': 1}
```
<br>

- 개선 방법은 왈러스 연산자(`:=`)를 활용하는 것입니다.
    - 대입식을 활용하면 한 `get_batch`함수를 한 번만 호출해서 그 결과를 변수에 저장할 수 있습니다.
    - 그래서 다시 호출할 필요 없이 딕셔너리의 내용을 만들 수 있습니다.
    - 불필요한 호출이 없으므로 불필요한 연산을 수행하지 않으므로 성능도 향상됩니다.
- 하지만 왈러스 연산자를 사용할 때 변수의 범위를 잘 생각해야 합니다.
    - 에러 예제에서
    - `for`와 `if`의 변수 범위가 같은데 tenth라는 변수는 `for`이나 `if`에서 정의되어 있지 않아서 에러가 납니다.
    - 즉 컴프리헨션이 평가되는 순서 때문에 에러가 발생합니다.
```python
## 왈러스 연산자 도입으로 깔끔 및 선능향상
real_found = {name: batches 
              for name in order 
              if (batches := get_batches(stock.get(name, 0), 8))}
print(real_found) #{'나사못': 4, '나비너트': 1}

## 왈러스 에러
# NameError: name 'tenth' is not defined
result = {name: (tenth := count // 10) for name, count in stock.items() if tenth >0}
## 에러개선
# 왈러스를 if문으로 옮겨주면 됨
result = {name: tenth for name, count in stock.items() if (tenth := count // 10) > 0}
print(result) # {'못': 12, '나사못': 3, '와셔': 2}
```
<br>

- 컴프리헨션에서 값 부분에 왈러스를 사용했을 때 값에 대한 조건 부분이 없다면 왈러스연산자로 정의한 변수가 밖으로 노출됩니다.
- 이런 변수 누출은 일반적인 for 루프에서 발생하는 루프 변수 누출과 비슷합니다.
    - 하지만 컴프리헨션 `for`구문에서는 누출되지 않습니다.
```python
half = [(last := count // 2) for count in stock.values()]
print(f'{half}의 마지막 원소는 {last}') #  [62, 17, 4, 12]의 마지막 원소는 12

## for loop 변수 누출
for count in stock.values():
    pass
print(f'{list(stock.values())}의 마지막 원소는 {count}')
# [125, 35, 8, 24]의 마지막 원소는 24

## 컴프리헨션 for에서는 누출되지 않음
half = [count2 // 2 for count2 in stock.values()]
print(half)
# print(count2) #NameError: name 'count2' is not defined
```
<br>

- 루프 변수는 누출되지 않는 편이 좋습니다. 따라서 컴프리헨션에서 대입식을 조건에만 사용합니다.
- 대입식은 제너레이터의 경우에도 같은 방식으로 동작합니다.
    - 다음 예제는 딕셔너리 인스턴스 대신 제품 이름과 현재 재로 수량 쌍으로 이뤄진 이터레이터를 만듭니다.
```python
found = ((name, batches) for name in order if (batches := get_batches(stock.get(name, 0), 8)))

print(next(found)) # ('나사못', 4)
print(next(found)) # ('나비너트', 1)
```

### 기억해야 할 Point
> - 대입식(왈러스 연산)을 통해 컴프리헨션이나 제너레이터 식의 조건 부분에서 사용한 값을 같은 컴프리헨션이나 제너레이터의 다른 위치에서 재사용할 수 있습니다. 이 방법으로 가독성이 좋아지고 성능 향상이 됩니다. <br>
> - 조건이 아닌 부분에도 대입식을 사용할 수 있찌만, 그런 형태의 사용은 피해야 합니다.(반복문 변수 누출의 위험)<br>

<br>

## BetterWay30. 리스트를 반환하기보다는 제너레이터를 사용하라

- 시퀀스를 결과로 반환하는 경우 가장 간단한 선택은 리스트를 반환하는 것입니다.

- 문자열에서 띄어쓰기 구분 리스트 예제
    - 리스트를 반환하는 경우 
        1. 코드 잡음이 많고 핵심을 알아보기 어렵습니다.
        2. 반환하기 전에 리스트에 모든 결과를 다 저장해야 해서 메모리 문제가 발생할 수 있습니다.
    - `yield`를 사용해서 `제너레이터`를 활용
        1. 코드 기능을 명확하게 표현할 수 있습니다.
        2. 한번에 한개씩만 반환하기 때문에 메모리가 매우 작습니다.
```python
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

address = '컴퓨터(영어: Computer, 문화어: 콤퓨터  , 순화어: 전산기)는 진공관'

print(index_words(address)) # [0, 8, 18, 23, 27, 28, 30, 35, 41]

## 개선
def index_word_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

it = index_word_iter(address)
print(next(it)) # 0
print(next(it)) # 8
```
<br>

- 제너레이터를 호출하는 부분에서 주의할 점이 있습니다. 제너레이터가 반환하는 이터레이터에 상태가 있기 때문에 호출하는 쪽에서 재사용이 불가능합니다.

### 기억해야 할 Point
> - 제너레이터를 사용하면 결과를 리스트에 합쳐서 반환하는 것보다 더 깔끔합니다.<br>
> - 제너레이터가 반환하는 이터레이터는 제너레이터 함수의 본문에서 `yield`가 반환하는 값들로 이뤄진 집합을 만들어냅니다.<br>
> - 제너레이터를 사용하면 작업 메모리에 모든 입력과 출력을 저장할 필요가 없기 때문에 입력 길이가 아주 길어도 출력 시퀀스를 만들 수 있습니다.<br>

<br>

## BetterWay31. 인자에 대해 이터레이션 할 때는 방어적이 되어라


### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay32. 긴 리스트 컴프리헨션보다는 제너레이터 식을 사용하라


### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay33. yield from을 사용해 여러 제너레ㅔ이터를 합성하라


### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay34. send로 제너레이터에 데이터를 주입하지 말라


### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay35. 제너레이터 안에서 throw 상태를 변화시키지 말라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay36. 이터레이터나 제너레이터를 다룰 때에는 itertools를 사용하라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>


## 여러 이터레이터 연결하기
## 이터레이터 원소 거리그
## 이터레이터 원소의 조합 만들어내기