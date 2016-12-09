from functools import partial
from iterpipe import Pipeline
import operator
import time



def churn(x):
    n = x**2
    while n > 0:
        n -= 1
    return x


multiply = partial(operator.mul, 20)


def even_filter(x):
    if x % 2 == 0:
        return x


if __name__ == "__main__":
    pipe = Pipeline(
        # args are functions that take single object
        # Filters: f(obj)-> obj or None
        # Calculations: f(obj) -> obj
        even_filter,  # remove odds
        multiply,     # multiply
        churn,        # stress the CPU

        # kwargs can define some interesting behavior
        filter_value=None,  # if any function returns None, skip it
    )

    for i in range(4, 0, -1):
        pipe.procs = i
        start = time.time()
        data = list(pipe(range(100)))
        elaps = time.time() - start
        print('pipe.procs == {0}: {1:0.4f} seconds'.format(i, elaps))
        print('\t[{}, {}, ..., {}]'.format(data[0], data[1], data[-1]))
