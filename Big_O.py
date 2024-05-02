def increment_one(a):
    return a+1
    #더하기의 기본 연산 1번 -> T(n) =1, O(1)

def number_of_bits(n):
    count = 0
    while n > 0:
        n = n //2
        count += 1
    return count
    #배정의 기본 연산 1번
    #while: 4번의 기본연산
        #배정, 나누기 -> 기본연산 2번 
        #배정 더하기 -> 2번
        #루프가 한 번 돌때마다 n/2씩 count만큼 수행하므로 count = log_2(n)
    #T(n) = 1 + 4*log_2(n) -> O(log(n))
