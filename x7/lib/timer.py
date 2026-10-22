import time


class Timer(object):
    """
        Timer class to be used in :code:`with` statement::

            with Timer('example'):
                for n in range(1024):
                    math.sqrt(n)
    """
    def __init__(self, tag='Timer'):
        self.tag = tag
        self.start = 0
        self.end = 0

    def __enter__(self):
        self.start = time.time_ns()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time_ns()
        print(f'{self.tag}: {self.elapsed_friendly()}')

    @property
    def elapsed(self) -> float:
        """Total time in seconds. Only valid after :code:`with` block"""
        return (self.end - self.start) / 1_000_000_000.0

    def elapsed_friendly(self) -> str:
        """Human-friendly version of time in seconds, milliseconds, or microseconds."""
        elapsed = self.elapsed
        if elapsed >= 1:
            return f'{elapsed:.3g}s'
        elif elapsed >= 1/1000:
            return f'{elapsed * 1_000:.3g}ms'
        return f'{elapsed * 1_000_000:.3g}μs'   # aka \u03bc
