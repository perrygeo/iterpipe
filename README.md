# iterpipe

> Build functional, parallelized processing pipelines for Python iterables

`iterpipe` lets you run sequences (*Iterables*) of Python objects through a series
of processing functions (the *Pipeline*). Pipelines can be seamlessly distributed
across cores for fully parallelized execution.

Inspired by Clojure's threading macros, the `parallel` command and Unix pipes, `iterpipe`
aims to make processing iterables in Python faster, easier to test and more functional.

```python
from iterpipe import Pipeline

# All functions in the pipeline
# - take a single item as an argument
# - return a single item

def churn(x):
    n = x**2
    while n > 0:
        n -= 1
    return x

from functools import partial
import operator
multiply = partial(operator.mul, 10)

def even_filter(x):
    if x % 2 == 0:
        return x

if __name__ == "__main__":
    pipe = Pipeline(
        even_filter,       # remove odd values
        multiply,          # multiply
        churn,             # stress the CPU
        filter_value=None, # if any function returns None, filter it
        procs=4            # Use 4 CPU cores
    )

    data = list(pipe(range(100)))  # [0, 20, ..., 980]
```

## Status

Alpha. Please try it out and give me some feedback.


## Installation

```
pip install -e "git+https://github.com/perrygeo/iterpipe.git#egg=iterpipe"
```
