#!/usr/bin/env python

__author__ = 'Shaun Rong'
__version__ = '0.1'
__maintainer__ = 'Shaun Rong'
__email__ = 'rongzq08@gmail.com'


def config_solver(p, r, u, N):
    deviation = {}
    poss_config = get_all_poss_config(p, r, u, N)
    for (m, n) in poss_config:
        deviation[(m, n)] = m * n * abs(p - m * n * n * u * u / r)
    (para, seri) = min(deviation, key=deviation.get)
    return (para, seri)


def get_all_poss_config(p, r, u, N):
    poss_config = []
    for i in range(int(p * r / (u * u * N)) + 1, N+1):
        j = int(p * r / (u * u * i * i))
        if 0 < j <= N:
            poss_config.append((j, i))
    return poss_config


if __name__ == '__main__':
    print config_solver(10, 1, 1, 10)