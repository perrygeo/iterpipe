from iterpipe import Pipeline
from functools import partial
import operator

multiply = partial(operator.mul, 10)

def even_filter(x):
    if x % 2 == 0:
        return x

def test_pipeline_one():
    pipe = Pipeline(
        even_filter, multiply, filter_value=None)

    data = list(pipe(range(10)))
    assert data == [0, 20, 40, 60, 80]


def test_pipeline_many():
    pipe = Pipeline(
        even_filter, multiply, filter_value=None, procs=2)

    data = list(pipe(range(10)))
    assert data == [0, 20, 40, 60, 80]


def test_pipeline_identity():
    pipe = Pipeline()
    assert list(pipe(range(10))) == list(range(10))
