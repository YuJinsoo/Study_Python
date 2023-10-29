# Chapter1 : 파이썬답게 생각하기

## 1-1. 사용중인 파이썬의 버전을 알아두라

- 콘솔에 `python --version`
- 혹은 `python3 --version`

```python
import sys
print(sys.version_info)
print(sys.version)
```
- 2020 부터는 python2가 정식 지원되지 않음.

## 1-2. PEP8 스타일 가이드를 따르라

- Python Enhancement Proposal 8
- 코드를 어떤 형식으로 작성할 지 알려주는 스타일 가이드
- 일관된 스타일을 사용하면 코드에 더 친숙하게 접근하고 코드를 더 쉽게 읽을 수 있다.

### 공백
공백은 파이썬 문법과 직접 연관되어있어 매우 중요합니다.
- 탭 대신 스페이스를 사용해서 들여쓰기
- 문법적으로 중요한 들여쓰기에는 4칸 스페이스
- 라인 길이는 79개 문자 이하
- 긴 식 다음 줄에 이어서 쓸 경우에, 4스페이스를 더 들여쓰기
- 파일 안에서 각 함수와 클래스 사이에는 빈 줄 2줄
- 클래스 안에서 메서드 사이에는 빈줄 1줄
- 딕셔너리에서 키와 콜론(:)사이에는 공백없고, 한 줄 안에 키-값을 같이 넣는경우 콜론 다으멩 스페이스 1개
- 변수 대입에서 = 전후에는 스페이스 1개
- 타입 표기를 붙이는 경우에는 변수 이름과 콜론 사에이 공백을 넣지 않도록 주의하고, 콜론과 타입 정보 사이에는 스페이스 1개

### 명명규약
- 함수, 변수, 어트리뷰트(attribute)는 lowercase_underscore 처럼
- 보호해야하는 인스턴스 어트리뷰트는 밑줄 한 개로 시작 _leading_underscore 처럼
- 비공개(클래스 안에서만 쓰여야 하는 것)인스턴스 어트리뷰트는 일반적인 이름규칙을 따르되 밑줄 두 개로 시작 __leading_underscore 처럼
- 클래스는 CapitalizeWord처럼 여러 단어를 이어 붙이되 각 단어의 첫 글자는 대문자
- 모듈 수준의 상수는 ALL_CAPS처럼 모든 글자를 대문자로 하고 단어 사이는 _
- 클래스의 인스턴스 메서드 첫 번째 인자의 이름으로 반드시 self
- 클래스의 클래스 메서드 첫 번째 인자의 이름으로 반드시 cls

### 식과 문
- 긍정적인 식을 부정(if not a is b)하지 말고 부정을 내부에 넣어라(if a is not b)
- 빈 컨테이너([])나 시퀀스('')를 검사할 때 길이를 0과 비교하지 말고, 길이가 0일 때 False로 취급되는 것을 활용 (if [])
- 비어있지 않은 컨테이너나 시퀀스에도 길이가 0보다 큰지 비교하지 말고 비어있지 않으면 True로 취급되는 것을 활용 (if 'hi')
- 한 줄짜리 if문이나 한줄짜리 for while 루프, 한 줄짜리 except 복합문을 사용하지 말아라. 명확성을 위해 여러 줄에 나눠 배치(읽기 쉬워짐)
- 식을 한 줄 안에 다 쓸 수 없는 경우, 식을 괄호로 둘러싸고 줄바꿈과 들여쓰기를 적용 (읽기 쉬워짐)
- 여러 줄에 걸쳐 식을 쓸 때에는 `\` 문자보다는 괄호를 사용해라

### 임포트
- import문은 항상 파일 맨 앞에
- 모듈을 임포트할 떄는 절재적인 이름(absolute name)을 사용하고, 현 모듈의 경로에 상대적인 이름은 사용하지 말라.
- 반드시 상대경로로 import 하는 경우 `from . import foo` 처럼 명시적인 구문을 사용
- 표준 라이브러리 모듈 > 서드파티 모듈 > 직접개발한 모듈 순서로 섹션을 나눠서 임포트해라. 각 세션에는 알파벳 순서로 모듈을 임포트하라

### Note
- Pylint : 파이썬 소스코드를 분석하는 정적 분석기.
-

## 1-3. bytes와 str의 차이를 알아두라
> 파이썬 문자열 데이터의 시퀀스를 표현하는 방법은 `bytes`와 `str`입니다.
`bytes`타입의 인스턴스에는 부호가 없는 8 바이트 데이터가 그대로 들어갑니다.
`str`타입의 인스턴스에는 유니코드 코드포인트가 들어있습니다.

```python
## 문자열을 encode하면 ascii 값과 같은 binary 값을 가짐
## 그리고 bytes는 시퀀스이기 때문에 해당 값을 조회하기위해서는 인덱스로 확인해야 함
char = 'a'
binary_char = char.encode()
print(char)                 # a
print(binary_char)          # b'a'
print(binary_char[0])       # 97
print(bin(binary_char[0]))  # 0b1100001
print(hex(binary_char[0]))  # 0x61

# bytes 타입은 ascii문자만 지원하기 때문에 아래는 에러 발생
a = b'안녕'
SyntaxError: bytes can only contain ASCII literal characters.
```

```python
a = b'h\x65llo'
print(list(a))  # [104, 101, 108, 108, 111]
print(a)        # b'hello'

a = 'a\u0300 propos'
print(list(a))  # ['a', '̀', ' ', 'p', 'r', 'o', 'p', 'o', 's']
print(a)        # à propos
```
- 중요한 사실은 str에는 직접 대응하는 이진 인코딩이 없고, bytes에는 직접 대응하는 텍스트 인코딩이 없습니다.
- 그래서 아래와 같이 각 인스턴스의 메서드를 호출해야 변환할 수 있습니다.
    > 유니코드 데이터 >> str의 encode() >> 이진 데이터<br/>
    > 이진 데이터 >> bytes의 decode() >> 유니코드 데이터

- 유니코드 데이터를 인코딩하거나 디코딩 하는 부분을 인터페이스 가장 먼 경계 지점에 위치시켜야 합니다. 이런 방식을 `유니코드 샌드위치`라고 부릅니다.

- 인코딩: 사람이 인지하는 정보를 규칙에 따라 컴퓨터가 이해하는 언어로 바꾸는것 
    - 코드화, 암호화, 부호화
    - 문자 / 사진&오디오&비디오
    - 문자인코딩: ASCII, UTF-8/16/32, Base64, Hex 등등..
- 디코딩: 이진 데이터를 사람이 인지하는 정보로 변환하는 것
    - 복호화, 역코드화
    - 저장공간 효율화, 보안 등의 이유로 하기도 함

```python
# 항상 str를 반환
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_str(b'foo')))             #'foo'
print(repr(to_str('bar')))              #'bar'
print(repr(to_str(b'\xed\x95\x9c')))    #'한'

# 항상 bytes를 반환
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_bytes(b'foo')))#b'foo'
print(repr(to_bytes('bar'))) #b'bar'
print(repr(to_bytes('한글'))) #b'\xed\x95\x9c\xea\xb8\x80'
```
### 첫 번째 문제점
> bytes와 str이 똑같이 작동하는 것처럼 보이지만 각가의 인스턴스는 서로 호환되지 않습니다. 전달 중인 문자 시퀀스가 어떤 타입인지를 항상 잘 알고 있어야 합니다.

- `+`연산자로 str끼리, bytes끼리 더할 수 있습니다. ( `>`, `<`, `==` 연산도 가능)
- 하지만 서로 다른 타입끼리는 더할 수 없습니다.
```python
print(b'one' + b'two')  # b'onetwo'
print('one' + 'two')    # 'onetwo'
print('one' + b'two')   # 불가능
```

- `str`의 포맷팅에 bytes인스턴스를 넘길 수 있지만 단순 `repr()`함수의 호출이기 때문에 원하던 것이랑 다르게 표기될 것 입니다.
```python
print('red %s' % b'blue') # red b'blue'
```

### 두 번째 문제점
> (내장 함수인 open을 호출해 얻은)파일 핸들과 관련한 연산들이 디폴트로 유니코드 문자열을 요구하고, 이진 바이트 문자열을 요구하지 않는다는 점입니다.

- 파일을 열 때 파일에 기록된 데이터에 맞는 형식으로 열어야 하고, 아니라면 인코딩 파라메터를 확실히 주어야 정확한 데이터를 확인할 수 있습니다.
- 시스템 디폴트 인코딩이 어떻게 다른지 이해하기 위해 시스템 인코딩을 항상 검사해야 합니다.
- `python 3 -c 'import locale; print(locale.getpreferredencoding())'`
- 지금 내 컴은 cp949

```python
# 파일 쓸 때
with open('data.bin', 'w') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5') ## 에러

with open('data.bin', 'wb') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5') ## 실행됨

# 저장된것 열때
with open('data.bin', 'r') as f:
    data = f.read() ## 에러

with open('data.bin', 'rb') as f:
    data = f.read() ## 실행됨
    print(data) # '\xf1\xf2\xf3\xf4\xf5 '

# encoding을 명시하면 명시한 인코딩 표현으로 보여줌
with open('data.bin', 'r', encoding='cp1252') as f:
    data = f.read() ## 실행됨
    print(data) # ñòóôõ
```

### 기억해야 할 point!
- bytes에는 8비트 값의 시퀀스가 들어 있고, str에는 유니코드 코드 포인트의 시퀀스가 들어 있다.
    - 코드 포인트: 문자 하나에 매핑해 둔 정수
    - 이 코드 포인트를 모아놓은 집합을 부호화된 문자 집합
- 처리할 입력이 원하는 문자 시퀀스(8비트, UTF-8로 인코딩된 문자열, 유니코드 코드 포인트들)인지 확실히 하려면 도우미 함수를 사용해라( 예제 `to_str()`, `to_bytes()`)
- bytes와 str 인스턴스는 (>, ==, +, %)와 같은 연산자에 섞어 쓸 수 있다.
- 이진 데이터 파일에서 읽거나 쓰고 싶으면 항상 이진 모드('rb', 'wb')로 파일을 열어라
- 유니코드 데이터를 파일에서 읽거나 쓰고 싶을 때는 시스템 디폴트 인코딩에 주의해야 합니다. 파일 open 함수에 encoding 파라미터를 명시적으로 전달해서 해소할 수 있습니다.


## Batter Way 4 : C스타일 형식 문자열을 str.format과 쓰기보다는 f-문자열 을 통한 인터폴레이션을 사용해라

- Better Way 27, Better way 80 에서 활용됩니다.

- 미리 정의된 텍스트 템플릿을 **형식 문자열** 이라고 부르고, 템플릿에 끼워 넣을 값들은 연산자의 오른쪽에 단일 값이나 tuple로 지정합니다.

### % 형식화 연산자 사용
- 형식 지정자(%d, %s, %x, %f 등) 지정이 필요합니다.
- 소수점 위치, 패딩, 채워넣기, 좌우 정렬 등 제공

```python
a = 0b10111011
b = 0xc5f
print('이진수: %d, 십육진수: %d' % (a,b))
# 이진수: 187, 십육진수: 3167
```

> 문제점 1. 
> - 형식화 식에서 오른쪽에 있는 tuple 내 데이터 값의 순서를 바꾸거나 값의 타입을 바꾸면 타입 변환이 불가능 (순서를 지켜줘야 함)

```python
## key와 value의 순서를 바꾸면 형식 지정자의 타입이 다르기때문에 예외 발생
key = 'my_car'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)
print(formatted) # my_car     = 1.23
```

> 문제점 2. 
> - 형식화하기 전 값을 변경해야 하는 경우(빈번함) 식을 읽기가 매우 어려워짐(가독성이 떨어짐)

```python
pantry = [
    ('아보카도', 1.25),
    ('바나나', 2.50),
    ('사과', 15.00),
    ]

for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i, item, count))
#0: 아보카도       = 1.25
#1: 바나나        = 2.50
#2: 사과         = 15.00

# 위 값을 다르게 수정하고 싶을 때
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %d' % (i+1, item.title(), round(count)))
#1: 아보카도       = 1
#2: 바나나        = 2
#3: 사과         = 15
```


> 문제점 3. 
> - 같은 값을 여러번 사용하고 싶을 때 같은 값을 반복한 튜플이 필요
```python
template = "%s야, %s야"
name = "철수
formatted = template % (name, name)
rint(formatted) # 철수야, 철수야
```

- 그래서 dictionary를 이용해 지정하는 방식을 지원합니다.
```python
name = '철수'
template = '%(name)s는 음식을 좋아해, %(name)s가 요리한다.'
result = template % {'name': name }
```
- 하지만 dictionary를 사용하는 방법은 값을 수정해야 하는 경우, 형식화 연산자인 %와 오른폰에 딕셔너리 키와 콜론 연산자가 추가됨에 따라 템플릿이 길어지고 읽기 어려워집니다.

> 문제점 4. 
> - 형식화에 딕셔너리를 사용할 경우 문장이 번잡스러워짐

### 내장함수 format과 str.format




## 복잡한 식을 쓰는 대신 도우미 함수를 작성해라
## 인덱스를 사용하는 대신 대입을 사용해 데이터를 언패킹해라

## range보다는 enumerate를 사용해라
## 여러 이터레이터에 대해 나란히 루프를 수행하려면 zip을 사용해라
## for나 while 루프 뒤에 else 블록을 사용하지 말아라
## 대입식을 사용해 반복을 피해라