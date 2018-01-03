#!/usr/bin/python
# -*- coding: utf-8 -*-
import math


def fibo(n):
    if n == 0 or n == 1 or n == 2:
        return n
    return fibo(n-1) + fibo(n-2)


def prob2():
    sum = 0
    n = 0
    while True:
        n += 1
        result = fibo(n)
        if result > 4000000:
            break
        if result % 2 == 0:
            sum += result
    print(sum)



def get_largest(number):
    num = number

    # 2 로 나누어 떨어질 때까지 나누고, 그다음 3, 그다음 5, ... 나눈 수보다 작을 때까지
    factor = 2
    max_factor = 2
    while True:

        if factor > num:
            break  # num 보다 커지면 그만!

        # 나누어 떨어질 때까지 반복
        while True:
            if num % factor == 0:  # 나누어 떨어진다면,
                num /= factor  # 나누고, 반복
                max_factor = factor
            else:  # 이제 안 나누어 떨어지면 그만
                break
        factor += 1

    return max_factor



def prob3():
    print(get_largest(600851475143))


def is_palindrome(num):
    num_str = str(num)
    size = len(num_str)
    for i in range(size/2):
        if num_str[i] != num_str[-i-1]:
            return False
    return True


def prob4():
    max_mult = 0
    for i in range(999):
        for j in range(999):
            number = i*j
            if is_palindrome(number) and max_mult < number:  # if larger number, update
                max_mult = i*j

    print(max_mult)


disjoints = [2, 3, 5, 7, 11, 13, 17, 19]
counts_of_disjoint = [0, 0, 0, 0, 0, 0, 0, 0]


def find_counts_of_disjoints(number):
    number_to_divide = number
    for i in range(0, 8):
        division_factor = disjoints[i]
        freq_of_factor = 0

        while True:
            if number_to_divide % division_factor == 0:  # 나누어 떨어지면
                freq_of_factor += 1  # 해당 소인수 빈도수 증가
                number_to_divide /= division_factor  #  나누고난 몫으로 또 반복해야함
            else:
                break

        if counts_of_disjoint[i] < freq_of_factor:  # update
            counts_of_disjoint[i] = freq_of_factor


def prob5():
    for number in range(11, 20):
        find_counts_of_disjoints(number)

    print(disjoints)
    print(counts_of_disjoint)

    result = 1

    # 모두 곱해서 최소공배수를 구합니다.
    for i in range(0, 8):
        result *= math.pow(disjoints[i], counts_of_disjoint[i])
    print(result)


def main():
    prob3()


if __name__ == "__main__":
    main()
