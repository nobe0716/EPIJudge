from test_framework import generic_test
from collections import defaultdict

def buy_and_sell_stock_k_times(prices, k):
    # TODO - you fill in here.
    d = defaultdict(int)
    n = len(prices)

    for i in range(1, n):
        min_v = prices[i]
        max_v = prices[i]
        for j in range(i, n):
            d[(i, j)] = max_v - min_v
            max_v = min(max_v, prices[j])
            d[(i, j)] = max(d[(i, j)], max_v - min_v)
            if prices[j] < min_v:
                min_v = prices[j]
                max_v = prices[j]

    t = defaultdict(int)
    # t[(1, 0)] = 0
    for i in range(n):
        t[(1, i)] = d[(0, i)]
    for i in range(2, k + 1):
        for j in range(i, n):
            t[(i, j)] = max((t[(i - 1, k)] + d[k, j] for k in range(0, j)))

    return t[(k, n - 1)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_k_times.py",
                                       'buy_and_sell_stock_k_times.tsv',
                                       buy_and_sell_stock_k_times))
