# 목록
1. [BetterWay1: 사용중인 파이썬의 버전을 알아두라](#betterway-1-사용중인-파이썬의-버전을-알아두라)
2. [BetterWay2: pep8 스타일 가이드를 따르라](#betterway-2-pep8-스타일-가이드를-따르라)
3. [BetterWay3: bytes와 str의 차이를 알아두라](#betterway-3-bytes와-str의-차이를-알아두라)
4. [BetterWay4: c스타일 형식 문자열을 strformat과 쓰기보다는 f-문자열 을 통한 인터폴레이션을 사용해라](#betterway-4--c스타일-형식-문자열을-strformat과-쓰기보다는-f-문자열-을-통한-인터폴레이션을-사용해라)
5. [BetterWay5: 복잡한 식을 쓰는 대신 도우미 함수를 작성해라](#betterway-5-복잡한-식을-쓰는-대신-도우미-함수를-작성해라)
6. [BetterWay6: 인덱스를 사용하는 대신 대입을 사용해 데이터를 언패킹해라](#betterway-6-인덱스를-사용하는-대신-대입을-사용해-데이터를-언패킹해라)
7. [BetterWay7: range보다는 enumerate를 사용하라](#betterway-7-range보다는-enumerate를-사용해라)
8. [BetterWay8: 여러 이터레이터에 대해 나란히 루프를 수행하려면 zip을 사용해라](#betterway-8-여러-이터레이터에-대해-나란히-루프를-수행하려면-zip을-사용해라)
9. [BetterWay9: for나 while 루프 뒤에 else 블록을 사용하지 말아라](#betterway-9-for나-while-루프-뒤에-else-블록을-사용하지-말아라)
10. [BetterWay10: 대입식을 사용해 반복을 피해라](#betterway-10-대입식을-사용해-반복을-피해라)


# Chapter1 : 파이썬답게 생각하기

## BetterWay 1. 사용중인 파이썬의 버전을 알아두라

- 콘솔에 `python --version`
- 혹은 `python3 --version`

```python
import sys
print(sys.version_info)
print(sys.version)
```
- 2020 부터는 python2가 정식 지원되지 않음.

## BetterWay 2. PEP8 스타일 가이드를 따르라

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

## BetterWay 3. bytes와 str의 차이를 알아두라
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


## BetterWay 4 : C스타일 형식 문자열을 str.format과 쓰기보다는 f-문자열 을 통한 인터폴레이션을 사용해라

- Better Way 27, Better way 80 에서 활용됩니다.

- 미리 정의된 텍스트 템플릿을 **형식 문자열** 이라고 부르고, 템플릿에 끼워 넣을 값들은 연산자의 오른쪽에 단일 값이나 tuple로 지정합니다.

### % 형식화 연산자 사용
- C 함수 스타일의 문자열 포매팅
- 형식 지정자(%d, %s, %x, %f 등) 지정이 필요합니다.
- 소수점 위치, 패딩, 채워넣기, 좌우 정렬 등 제공

```python
a = 0b10111011
b = 0xc5f
print('이진수: %d, 십육진수: %d' % (a,b))
# 이진수: 187, 십육진수: 3167
```

- % 표현 시 %%로 이스케이프 합니다.
```python
print('%.2f%%' % 12.5) # 12.50%
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
- C 스타일과 다른 **고급 문자열 형식화**
- format 내장 함수를 통해 모든 파이썬 값에 사용할 수 있습니다.

```python
a = 1234.5678
formatted = format(a, ',.2f') # ,는 숫자 자리수 구분자 옵션
print(formatted)
# 1,234.57

b = 'my문자열'
formatted = format(b, '^20s') # ^는 가운데 정렬, 20자리 s 문자열
print('*', formatted, '*')
# *        my문자열         *
```

- str 타입에 `format` 메서드를 이용해 여러 값에 대해 한꺼번에 이 기능 적용이 가능합니다.
- 위치 지정자`{}`를 사용합니다.
- 위치 지정자에는 콜론 뒤에 형식 지정자를 넣을 수 있습니다. help('FORMATTING')
```python
key = 'my_var'
value = 1.234
formatted = '{} = {}'.format(key, value) # 순서대로 입력됨
print(formatted) # my_var = 1.234

formatted = '{:<10} = {:.2f}'.format(key, value) # 형식 지정자
print(formatted) # my_var     = 1.23
```

- 중괄호 표현 시 중괄호를 두 번씩 써서 이스케이프 합니다.
```python
print('{} replaces {{}}'.format(1.23)) # 1.23 replaces {}
```
- 위치 지정자에 인덱스 전달 가능합니다. (C 스타일 문자열 문제점 1번 해결 가능)
- 또한 같은 위치 인덱스를 여러번 사용할 수 있습니다.(문제점 3번 해결 가능)
```python
key = 'my_var'
value = 1.234
formatted= '{1} = {0}'.format(key, value)
print(formatted) # 1.234 = my_var

formatted = '{1} = {1} = {1}'.format(key, value)
print(formatted) # 1.234 = 1.234 = 1.234
```

- 2번문제점과 4번 문제점은 해결 못하기 때문에 f-string을 사용하기를 권합니다.

### 인터폴레이션 방식
- f-string 방식
- python 3.6부터 지원
- 위치지정자에 python 식을 포함할 수 있으므로 매우 강력합니다.

```python
key = 'my_var'
value = 1.234
formatted = f'{key} = {value}'
print(formatted) # my_var = 1.234

formatted = f'{key!r:<10} = {value:.2f}'
print(formatted) # 'my_var'   = 1.23
```

- C 스타일 문자열이나 str.format을 사용하는 것 보다 짧습니다. (가독성)
```python
f_string = f'{key:<10} = {value:.2f}'
c_type = '%-10s = %.2f' % (key, value)
str_format = '{:<10} = {:.2f}'.format(key, value)
str_kw = '{key:<10} = {value:.2f}'.format(key=key, value=value)
c_dict = '%(key)-10s = %(value).2f' % {'key':key, 'value':value}

assert c_type == c_dict == f_string
assert str_format == str_kw == f_string
```

- 파이썬 식을 형식 지정자 옵션에 넣을 수 있다.
- 아래 예제는 자리수를 하드코딩하지 않고 변수로 지정하는 예제입니다.
```python
places = 3
number = 1.234567
print(f'내가 고른 숫자는 {number:.{places}f}') # 내가 고른 숫자는 1.235
```

### 기억해야 할 point!
> f-string 문자열을 사용하면 다양한 케이스에서 단순하게 해결이 가능하지만, python 버전 3.6 을 잘 확이하고 사용해야 합니다.

## BetterWay 5: 복잡한 식을 쓰는 대신 도우미 함수를 작성해라

- 파이썬은 문법이 간결하므로 상당한 로직이 들어가는 경우도 간단하게 처리할 수 있습니다. (하지만 가독성은 다소 떨어질 수 있습니다.)
- 아래 예제는 쿼리 파라미터를 파싱하는 예제입니다.
  - 딕셔너리는 첫번째 인자의 `key`가 없으면 두번째 인자를 리턴합니다. Key가 없을 때 KeyError을 발생시키기 보다 `get`메서드를 사용하세요. >> 16
  -  초록의 경우 `''` 이 원소로 있는 list이므로 None이 아니기 때문에 `True`이고, `green = True or 0` 구문에서 0이 green에 할당됩니다.
  - `or` 좌측 연산이 True일 경우 우측 값이 선택되는 것을 활용한 것입니다.

```python
from urllib.parse import parse_qs

my_values = parse_qs('빨강=5&파랑=0&초록=', keep_blank_values=True)
print(repr(my_values)) # {'빨강': ['5'], '파랑': ['0'], '초록': ['']}

## 파라메터가 없거나 비어있는 경우 0을 디폴트 값으로 하는 방법...
## 추가 함수를 사용하기보다 다음과 같이 if식을 사용
red = my_values.get('빨강', [''])[0] or 0
green = my_values.get('초록', [''])[0] or 0
opacity = my_values.get('투명도', [''])[0] or 0
print(f"빨강:{red!r}")      # 빨강:'5'
print(f"초록:{green!r}")    # 초록:0
print(f"투명도:{opacity!r}")# 투명도:0
```

- 위 식은 읽기 어렵고 원하는 기능을 모두 제공하지 못합니다.
- 모든 파라미터를 정수로 변환해서 즉시 수식에 활용하고 싶습니다.
- 위의 경우`if expression` 대신 if/else 조건식(삼항 조건식)을 사용하면 명확하게 표현할 수 있습니다.

```python
# if/else 조건식 (삼항 조건식) 으로 표현
my_values = parse_qs('빨강=5&파랑=0&초록=', keep_blank_values=True)
red_str = my_values.get("빨강", [''])
red = int(red_str[0]) if red_str[0] else 0
```

- 하지만 위의 예제도 완전히 분리한 if/else 문 보다 명확하지 않습니다. 오히려 더 복잡해 보입니다.
```python
# if else 구문으로 표현
my_values = parse_qs('빨강=5&파랑=0&초록=', keep_blank_values=True)
green_str = my_values.get('초록',[''])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0
```

- 이 로직을 **반복적으로 사용하고자 한다면(단 두세 번만 사용하더라도) 도우미 함수를 작성**하는 것을 권장합니다.(DRY 원칙을 지키자!)

```python
# 도우미 함수 작성하고 호출
def get_first_value(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

my_values = parse_qs('빨강=5&파랑=0&초록=', keep_blank_values=True)
green = get_first_value(my_values, '초록')
print(green)
```

### 기억해야 할 내용<br>
> 1. 파이썬 문법을 사용하면 아주 복잡하고 읽기 어려운 한 줄짜리 식을 쉽게 작성 가능합니다.<br>
> 2. 복잡한 식을 도우미 함수로 개발. 특히 같은 로직을 반복해 사용할 때는 도우미 함수를 꼭 사용합니다.<br>
> 3. `boolean`연산자 `or`나 `and`를 식에 사용하는 것보다 `if/else`식을 쓰는 것이 가독성이 좋습니다.<br>
> **파이썬의 DRY(Don't Repeat Yourself) 원칙을 지키자!** 

<br>


## BetterWay 6: 인덱스를 사용하는 대신 대입을 사용해 데이터를 언패킹해라

- Python에는 한 문장에 여러 변수를 대입할 수 있는 **언패킹** 구분을 지원합니다.
- 자료구조의 구조를 알고 있다면 인덱스 대신 언패킹을 통해 값에 접근할 수 있습니다.

```python
item = ("호박엿", "식혜")
first, second = item
print(first, second) # 호박엿, 식혜
```
<br>


- 언패킹이 인덱스보다 시각적으로 편하고 코드가 명확해집니다.
- `dictionary`의 `items()`는 key, value를 `tuple`로 묶은 것을 `list`로 반환합니다.
```python
favorite_snaks = {
    '짭쪼름 과자': ('프레젤', 100),
    '달콤 과자': ('쿠키', 180),
    '채소': ('당근', 20),
}
print(favorite_snaks.items()) ##  items는 key, value 쌍을 tuple로 묶어 list로 반환해줍니다.
(type1, (name1, cals1)),(type2, (name2, cals2)),(type3, (name3, cals3)) = favorite_snaks.items()

print(f'제일 좋아하는 {type1}는 {name1}, {cals1}칼로리입니다.')
print(f'제일 좋아하는 {type2}는 {name2}, {cals2}칼로리입니다.')
print(f'제일 좋아하는 {type3}는 {name3}, {cals3}칼로리입니다.')

# 제일 좋아하는 짭쪼름 과자는 프레젤, 100칼로리입니다.
# 제일 좋아하는 달콤 과자는 쿠키, 180칼로리입니다.    
# 제일 좋아하는 채소는 당근, 20칼로리입니다.
```
<br>

- 언패킹을 사용하면 한 줄로 값을 맞바꿀 수 있습니다. (한 줄로 스왑 가능)
- 원리를 알아보자면
- 우항 `a[i-1], a[i]` 이 임시 `tuple`에 저장되고 이후에 해당 튜블 값이 좌항 `a[i], a[i-1]`에 언패킹 되어 할당됩니다. 이후 임시 tuple 객체는 사라집니다.

```python
## 임시변수를 
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] > a[i-1]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp

names = ['프레첼', '당근', '쑥갓', '베이컨']
bubble_sort(names)
print(names) # ['프레첼', '쑥갓', '베이컨', '당근']

## 위 함수를
def bubble_sort2(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] > a[i-1]:
                a[i], a[i-1] = a[i-1], a[i] ## unpacking 활용하여 스왑!

names = ['프레첼', '당근', '쑥갓', '베이컨']
bubble_sort2(names)
print(names)# ['프레첼', '쑥갓', '베이컨', '당근']
```
<br>

- 언패킹의 또다른 활용!
- 리스트의 원소를 인덱스 없이 언패킹할 수 있습니다.
```python
## 인덱스를 활용한 방법
snacks =  [('베이컨', 350), ('도넛', 240), ('머핀', 190)]
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f'{i+1}: {name}은 {calories} 칼로리입니다.')
# 1: 베이컨은 350 칼로리입니다.
# 2: 도넛은 240 칼로리입니다.
# 3: 머핀은 190 칼로리입니다.

## 언패킹으로 확인하기 - 코드가 짧고 이해하기 쉽다!
snacks =  [('베이컨', 350), ('도넛', 240), ('머핀', 190)]
for rank, (name, calories) in enumerate(snacks):
    print(f'{rank+1}: {name}은 {calories} 칼로리입니다.')
# 1: 베이컨은 350 칼로리입니다.
# 2: 도넛은 240 칼로리입니다.
# 3: 머핀은 190 칼로리입니다.
```
<br>

- 추가적으로 list구조, 함수인자, 키워드 인자, 다중반환 값 등에 대한 언패킹 기능도 가능합니다.
- 이 내용은 추후 betterway 13, 22, 23, 19 에서 다룹니다.


### 기억해야 할 point!
> 1. 한 문장 안에서 여러 값을 대입할 수 있는 언패킹 문법 제공<br>
> 2. 파이썬에서 언패킹은 일반적이므로 모든 이터러블에 적용 가능. 이터러블이 여러 계층이더라도 가능 <br>
> 3. 인덱스를 사용하는 것 대신 언패킹을 사용해 시각적인 불편함을 줄이고 코드를 명확하게 할 수 있습니다.


## BetterWay 7: range보다는 enumerate를 사용해라
- range 내장 함수는 정수 집합을 이터레이션 하는 루프가 필요할 때 유용합니다.
```python
from random import randint
random_bits = 0
for i in range(32):
    if randint(0,1):
        random_bits |=1 << i

print(bin(random_bits)) # 0b10100000000011101101110110010110
```
<br>

- 이터레이션할 대상 데이터 구조가 있으면 스퀀스에 대해 바로 루프를 돌 수 있습니다.
```python
flavor_list = ['바닐라', '초코', '피칸', '딸기']
for flavor in flavor_list:
    print(f'{flavor} 맛있어요.')
# 바닐라 맛있어요.
# 초코 맛있어요.
# 피칸 맛있어요.
# 딸기 맛있어요.
```
<br>

- `list`를 이터레이션 하면서 리스트의 몇 번재 원소를 처리 중인지 알아야 할 때 range를 사용하는 방법이 있습니다.
- 하지만 이 코드는 투박합니다.
    - `list`의 길이를 알아야 합니다.
    - 인덱스를 사용해 배열 원소에 접근해야 합니다.
    - 이처럼 여러 단계를 거치기 때문에 가독성이 떨어집니다.

```python
flavor_list = ['바닐라', '초코', '피칸', '딸기']
for i in range(len(flavor_list)):
    print(f'{i}: {flavor_list[i]} 맛있어요.')

# 0: 바닐라 맛있어요.
# 1: 초코 맛있어요.
# 2: 피칸 맛있어요.
# 3: 딸기 맛있어요.
```

- 그래서 파이썬에서 **enumerator**를 제공합니다.
- `enumerator`는 이터레이터를 지연 계산 제너레이터(lazy generator)로 감쌉니다.
- `enumerator`는 루프 인덱스와 이터레이터의 다음 값으로 이워진 쌍을 넘겨줍니다.
- `next`함수를 이용해서 다음 원소를 가져옵니다.

```python
flavor_list = ['바닐라', '초코', '피칸', '딸기']
it = enumerate(flavor_list)
print(next(it)) # (0, '바닐라')
print(next(it)) # (1, '초코')
```

- `enumerator`가 넘겨주는 각 쌍을 for문에서 간결하게 언패킹 할 수 있습니다.
- 코드가 훨씬 간결합니다.
```python
flavor_list = ['바닐라', '초코', '피칸', '딸기']
for index, value in flavor_list:
    print(f'{index}: {value} 맛있어요.')
# 0: 바닐라 맛있어요.
# 1: 초코 맛있어요.
# 2: 피칸 맛있어요.
# 3: 딸기 맛있어요.
```

### 기억해야 할 Point
> - `enumerator`를 사용하면 이터레이터에 대해 루프를 돌면서 이터레이터에서 가져오는 원소의 인덱스까지 얻어 코드를 간결하게 작성할 수 있습니다.<br>
> - `range`에 대해 루프를 돌면서 시퀀스의 원소를 인덱스로 가져오기 보다는 `enumerator`를 사용합니다.<br>
> - `enumerator`의 두 번째 파라미터로 어디부터 원소를 가져오기 시작할 지 지정할 수 있습니다.(default는 0)<br>
> - enumerator는 generator이므로 길이가 길어질수록 시퀀스 순회보다 성능이 좋습니다.

<br>

## BetterWay 8: 여러 이터레이터에 대해 나란히 루프를 수행하려면 zip을 사용해라

- list에 담긴 객채와 관련된 정보를 담은 list를 생성하거나 다루는 경우가 자주 발생합니다. 
- 이때 list comprehension을 사용하면 소스 list에 대해 쉽게 관련된 list를 생성할 수 있습니다.

```python
names = ['Cecilica', '남궁민수', '헤헤헤']
name_length = [len(n) for n in names]
print(name_length) # [8, 4, 3]
```
<br>

- 생성된 두 리스트를 동시에 참조해야 하는 경우에는 리스트의 길이만큼 순회를 돌려 동시에 참조할 수 있습니다.
- 하지만 이 방법은 시각적으로 깔끔하고 알아보기 쉬운 코드가 아닙니다.
    - list 객체의 원소를 찾는 과정이 코드를 어렵게 만듭니다.
    - 배열 인덱스 연산이 2번 발생합니다.
- 이는 `enumerate`를 사용하더라도 인덱스 참조 연산이 발생합니다.

```python
names = ['Cecilica', '남궁민수', '헤헤헤']
name_length = [len(n) for n in names]

longest_name = None
max_count = 0

for i in range(len(names)):
    count = name_length[i]
    if count > max_count:
        longest_name = names[i]
        max_count = name_length[i]
print(longest_name) # Cecilica

## enumerate 적용
for i, name in enumerate(names):
    count = name_length[i]
    if count > max_count:
        longest_name = name
        max_count = name_length[i]
print(longest_name) # Cecilica
```
<br>

- 파이썬에서는 이런 코드를 더 깔끔하게 만들 수 있도록 `zip`이라는 내장함수를 제공합니다.
- `zip`은 둘 이상의 디터레이터를 지연 계산 제너레이터를 사용해 묶어줍니다.
- 리스트의 원소에 접근하는 인덱스 연산보다 깔끔합니다.

```python
names = ['Cecilica', '남궁민수', '헤헤헤']
name_length = [len(n) for n in names]

longest_name = None
max_length = 0

for name, length in zip(names, name_length):
    if length > max_length:
        longest_name = name
        max_length = length

print(longest_name, max_length) # Cecilica 8
```
<br>

- `zip`은 자신이 감싼 이터레이터 우너소를 하나씩 소비합니다. **시퀀스의 길이만큼의 메모리를 소모해서 프로그램이 중단되는 위험 없이 아주 긴 입력도 처리할 수 있습니다.**
- 길이가 다른 두 시퀀스를 `zip`으로 묶었을 때에는 짧은 길이를 기준으로만 연산을 진행합니다.
    > `zip`은 자신이 감싼 이터레이터 중 어느 하나가 끝날 때까지 튜플을 내놓는 방식으로 동작하기 떄문입니다.
- 두 이터레이터의 길이가 다를 때 긴 이터레이터의 뒷부분 정보를 모두 활용하고 싶은 경우에는 `itertools`에 있는 `zip_longest`를 대신 사용합니다.
- 이 때에는 짧은 쪽 언패킹 부분에 모두 `None`이 출력됩니다.

```python
# 길이가 다를 때 zip 동작
names = ['Cecilica', '남궁민수', '헤헤헤']
name_length = [len(n) for n in names]
names.append('Rosalind')

for name, length in zip(names, name_length):
    print(name, length)
    
# Cecilica 8
# 남궁민수 4
# 헤헤헤 3

# zip_longest적용
from itertools import zip_longest
names = ['Cecilica', '남궁민수', '헤헤헤']
name_length = [len(n) for n in names]
names.append('Rosalind')

for name, length in zip_longest(names, name_length):
    print(name, length)
    
# Cecilica 8
# 남궁민수 4
# 헤헤헤 3
# Rosalind None
```
<br>

### 기억해야 할 Point
> - `zip` 내장 함수를 사용해 여러 이터레이터를 나란히 이터레이션 할 수 있습니다.<br>
> - `zip`은 지연된 제너레이터이므로 무한히 긴 입력에서도 메모리 문제 없이 사용할 수 있습니다.<br>
> - 입력 이터레이터의 길이가 다를 경우 길이가 긴 쪽의 나머지 원소는 무시됩니다.<br>
> - 긴 길이의 이터레이터에 맞추고 싶다면 `itertools.zip_longest`를 사용합니다.
<br>

## BetterWay 9: for나 while 루프 뒤에 else 블록을 사용하지 말아라

- 다른 언어에서는 지원하지 않지만, python에서는 반복문(루프)뒤에 `else` 블록을 지원합니다.
- 반복문 이후에 오는 `else` 구문은 `break`를 만나지 않고 정상적으로 모든 순회를 만쳐야 실행합니다.
- 처음부터 종료 조건인 `[]`를 for문이나 while의 조건에 넣어도 `else` 구문이 실행됩니다.

```python
for i in range(3):
    print('Loop', i)
else:
    print('else block')

# Loop 0
# Loop 1
# Loop 2
# else block

for i in range(3):
    print('Loop', i)
    if i == 1:
        break
else:
    print('else block')
    
# Loop 0
# Loop 1
```

- 하지만 반복문 다음의 `else`의 경우 어떤 구문에서 실행되는지 의미가 모호하고 명확하지 않아 가독성이 떨어집니다.
    - try/except/finally/else 구문의 경우 try 구문이 정상적이지 않을 때 나머지 구문들을 동작하는 방식이지만 반복문의 else는 정반대로 동작하기 때문입니다.
- 그렇기 때문에 반복문의 `else`구문을 절대 사용하지 않는 것을 추천합니다.

### 기억해야 할 Point
> - python은 `for`이나 `while`뒤에 `else`블록을 허용하는 문법을 지원합니다.<br>
> - 루프 뒤의 `else`블록은 `break`를 만나지 않은 경우에만 실행됩니다.<br>
> - 동작이 직관적이지 않고 혼동을 야기하므로 사용하지 않습니다.<br>
<br>

## BetterWay 10: 대입식을 사용해 반복을 피해라
- 대입식, assignment expression, 왈러스 연산자, :=
- 고질적인 코드 중복을 줄이기 위해 **python 3.8**에 도입된 개념입니다.
- 변수에 값을 할당함과 동시에 그 값에 대해 조건문 등에서 판단이 가능한 연산자입니다.
<br>

- 아래 예제는 왈러스 연산자 미적용/적용 예시입니다.
- 왈러스 연산자를 적용해보니
  - 코드가 한 줄 짧아집니다.
  - `count` 변수가 `if`문의 첫 번째 블록에서만 의미가 있다는 점이 명확합니다.
- **대입 후 평가** 동작이 왈러스 연산자의 핵심

```python
## 레몬 제고를 확인해서 있으면 레모네이드를 만드는 기능

fruit = {'사과':10, '바나나':8, '레몬':5}

def make_lemonade(count):
    pass

def out_of_stock():
    pass

# 일반적인 기능.
## count를 할당 한 다음에 if 문에서 count에 대해 판별을 해주어햐 함.
count = fruit.get('레몬', 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()

# 왈러스 연산자 적용
if count := fruit.get('레몬', 0):
    make_lemonade(count)
else:
    out_of_stock()
```
<br>

- 대입식 부분을 괄호로 묶어 다른 값과의 비교도 가능합니다.
```python
if (count := fruit.get('레몬', 0)) >= 4 :
    make_lemonade(count)
else:
    out_of_stock()
```
<br>

- 영역 밖의 변수에 값을 대입하고 다음 함수의 인자로 들어가는 경우 코드를 줄일 수 있습니다.
- 하지만 이 부분은 개인적인 의견으로 가독성에 큰 차이가 발생하지는 않는 개선법인 것 같습니다.

```python
# 바나나 스무디를 만드는 기능 예제
fruit = {'사과':10, '바나나':8, '레몬':5}
def slice_bananas(count):
    pass

def out_of_stock():
    pass

class OutOfBananas(Exception):
    pass

def make_smoothies(count):
    pass

# 일반식
pieces = 0
count = fruit.get('바나나', 0)
if count >= 2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()
    
# 아래처럼 표현 가능하지만, 코드 흐름이 이상
count = fruit.get('바나나', 0)
if count >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

# 왈러스식으로 코드 간편화
pieces = 0
if (count := fruit.get('바나나', 0)) >= 2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

```
<br>

- 원래 python에서는 switch-case문이 없었으나 `match-case`문이 도입되어 이 부분은 개선된 부분이입니다. (파이썬 버전 3.10에 도입되었습니다.)
- 아래처럼 긴 count를 연속적으로 확인해야 하는 부분에서 왈러스 연산자를 적용해서 줄을 줄이고, 인덴트를 같은 레벨로 유지해서 가독성이 좋습니다.

```python
fruit = {'사과':10, '바나나':8, '레몬':5}
def make_lemonade(count):
    pass

def slice_bananas(count):
    pass

def out_of_stock():
    pass

class OutOfBananas(Exception):
    pass

def make_smoothies(count):
    pass

def make_cider(count):
    pass
# 바나나는 스무디, 사과는 사이다, 레몬은 레모네이드를 만드는 기능
##  왈러스 없는 식
count = fruit.get('바나나', 0)
if count >=2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fruit.get('사과', 0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        count = fruit.get('레몬', 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = '아무것도없음'

## 왈러스
if (count := fruit.get('바나나', 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fruit.get('사과', 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fruit.get('레몬', 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = '아무것도 없음'
```
<br>

- python에 없는 `do/while`기능도 지원이 가능합니다.

```python
def pick_fruit():
    pass

def make_juice(a, b):
    pass

# 일반식 do while이 안됨.
bottles = []
while True:
    fruit = pick_fruit()
    if not fruit:
        break
    
    for fruit, count in fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
        
## 왈러스
bottles = []
while fruit := pick_fruit():
    for fruit, count in fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
```
<br>

### 기억해야 할 Point
> - 대입식에서는 왈러스 연산자(:=)를 사용해 하나의 식 안에서 변수 이름에 값을 대입하면서 이 값을 평가할 수 있고 중복을 줄일 수 있습니다.<br>
> - 대입식이 더 큰 식의 일부분으로 쓰일 때는 괄호로 둘러싸야 합니다.<br>
> - 대입식을 활용하면 파이썬에 없는`do/while` 기능을 흉내낼 수 있습니다.<br>
<br>