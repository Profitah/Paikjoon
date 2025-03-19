def count_primes(n, numbers):
    prime_count = 0
    for num in numbers:
        error = 0
        if num > 1:
            for i in range(2, num):  # 2부터 num-1까지
                if num % i == 0:
                    error += 1  # 2부터 num-1까지 나눈 나머지가 0이면 error가 증가
            if error == 0:
                prime_count += 1  # error가 없으면 소수.
    return prime_count

n = int(input())
numbers = map(int, input().split())
result = count_primes(n, numbers)
print(result)


# 민성님 코드의 다운그레이드 버전입니다..