"""
    Shell tools for x7.lib

    Usage: from x7.shell import *
"""

from pprint import pp

__all__ = ['tools', 'Dir', 'pp']


def tools():
    """Help for tools"""
    from x7.lib.shell_tools_load import loaded_tools, loaded_modules

    print('x7 shell: %d tools from %s' % (len(loaded_tools), ', '.join('x7.%s' % lm for lm in loaded_modules)))
    width = max(map(len, loaded_tools.keys()))
    for name, val in sorted(loaded_tools.items(), key=lambda item: item[0].lower()):
        print('  %*s - %s' % (-width, name, val.__doc__))


# noinspection PyPep8Naming
def Dir(v):
    """Like dir(v), but only non __ names"""

    return [n for n in dir(v) if not n.startswith('__')]


