__version__ = '1.694.21'
try:
    from ._nameless import longest  # noqa
except ImportError:
    def longest(args):
        return max(args, key=len)
