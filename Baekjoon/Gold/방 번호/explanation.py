import sys
n = int(input())
prices = list(map(int, input().split()))
money = int(input())

def solution(n, prices, money):
    if n == 1:
        return "0"

    min_price = min(prices)
    min_price_index = prices.index(min_price)
    non_zero_min_price = min(prices[1:])
    non_zero_min_price_index = prices.index(non_zero_min_price)

    if non_zero_min_price > money:
        return "0"

    digit = (money - non_zero_min_price) // min_price + 1
    answer = [min_price_index] * digit
    answer[0] = non_zero_min_price_index

    money -= non_zero_min_price + min_price * (digit - 1)

    for i in range(n-1, non_zero_min_price_index, -1):
        if prices[i] - non_zero_min_price <= money:
            answer[0] = i
            money -= prices[i] - non_zero_min_price
            break

    for p in range(1, digit):
        for i in range(n-1, min_price_index, -1):
            if prices[i] - min_price <= money:
                answer[p] = i
                money -= prices[i] - min_price
                break

    return "".join(map(str, answer))

print(solution(n, prices, money))