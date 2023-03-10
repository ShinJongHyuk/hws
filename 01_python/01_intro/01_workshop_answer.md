# workshop

### 1. 문자 print

`It's SSAFY9` 를 출력하는 프로그램을 작성하시오. (중간에 작은따옴표가 있다.)

```python
# 문자열 내부에 작은 따옴표가 있어
# 큰 따옴표로 감싸 주었다.

print("it's SAFFY 9")

# escape sequence를 사용하여
# 작은 따옴표로 작성하였다.
print('It\'s SSAFY 9')
```

### 2. 숫자 print

`458345 + 623576` 를 계산하여 출혁하는 프로그램을 작성하시오.

```python
a = 458345 
b = 623576
print(a+b)
```

```python
# 어떠한 값을 반환하는 내용을 모두
# expression (표현식) 이라고 부른다.
# tmp = list(range(5)) -> [0, 1, 2, 3, 4]
# tmp = 0 and 1 -> 1
# tmp = len([1, 2, 3]) -> 3
answer = 458345 + 623576
print(answer)
```

### 3. 변수를 사용해서 데이터 출력하기

두 변수 greeting, month를 사용해서 `Hello July` 를 출력하는 프로그램을 작성하시오.

```python
greeting = 'Hello'
month = 'July'
print(greeting, month)
print(f'{greeting} {month}')
answer = greeting + ' ' + month
print(answer)
```

### 4. 문자형의 입력과 출력

입력 받은 문자를 출력하는 프로그램을 작성하시오. (힌트: `input()` 함수를 활용하여 테이터를 입력받을 수 있다.)

```python
hello = input() # '3'
hi = input() # '2'
print(hello + hi) # >>> '32'
# '3' + '2' == '32'
# 문자열을 정수로 형변환 한 후에 계산한다.
hello = int(input()) # '3'
hi = int(input()) # '2'
print(hello + hi) # >>>'5'
```


