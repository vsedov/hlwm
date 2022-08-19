import time
from typing import Dict


class _Profiler(object):

    def __init__(self) -> None:
        self.profiles: Dict[str, Dict[str, float]] = {}

    def profile(self, fn):

        def wrapped(*args, **kwargs):
            ts = time.time()
            ret = fn(*args, **kwargs)
            te = time.time()
            dt = te - ts
            name = fn.__name__
            if name in self.profiles.keys():
                self.profiles[name]['time'] += dt
                self.profiles[name]['n_iter'] += 1
            else:
                self.profiles[name] = {}
                self.profiles[name]['time'] = dt
                self.profiles[name]['n_iter'] = 1
                self.profiles[name]['average'] = dt

            return ret

        return wrapped

    def __repr__(self):
        for name in self.profiles.keys():
            self.profiles[name]['average'] = self.profiles[name]['time'] / self.profiles[name]['n_iter']
        return self.profiles.__repr__()


Profiler = _Profiler()
