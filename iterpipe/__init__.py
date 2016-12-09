__version__ = '0.1'

from multiprocessing import Pool

class NotSpecified(object):
    pass

null = NotSpecified()

class Pipeline(object):
    def __init__(self, *funcs, filter_value=null, procs=1):
        self.funcs = funcs
        self.filter_value = filter_value
        self.procs = procs

    def _run(self, item):
        """ Run all functions in the pipeline on a single item
        """
        for func in self.funcs:
            item = func(item)
            if item == self.filter_value:
                break
        return item

    def __call__(self, data):
        if self.procs == 1:
            for item in data:
                x = self._run(item)
                if x != self.filter_value:
                    yield x
        elif self.procs > 1:
            with Pool(processes=self.procs) as pool:
                for x in pool.imap(self._run, data, chunksize=10):
                    if x != self.filter_value:
                        yield x
