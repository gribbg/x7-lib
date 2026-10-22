import time
from unittest import TestCase
from x7.lib.annotations import tests
from x7.lib.timer import Timer


@tests(Timer)
class TestTimer(TestCase):
    @tests(Timer.__enter__)
    @tests(Timer.__exit__)
    @tests(Timer.__init__)
    def test___init__(self):
        # __init__(self, tag='Timer')
        t = Timer('test timer')
        with t:
            time.sleep(0.1)
        self.assertGreater(t.elapsed, 0.09)
        self.assertLess(t.elapsed, 0.11)

    @tests(Timer.elapsed_friendly)
    def test_elapsed_friendly(self):
        t = Timer('test timer')
        t.start = 0
        t.end = 5
        self.assertEndsWith(t.elapsed_friendly(), '0.005μs')
        t.end = 1_500
        self.assertEndsWith(t.elapsed_friendly(), '1.5μs')
        t.end = 1_600_000
        self.assertEndsWith(t.elapsed_friendly(), '1.6ms')
        t.end = 1_400_000_000
        self.assertEndsWith(t.elapsed_friendly(), '1.4s')
