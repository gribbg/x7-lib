"""
    Loader code for shell tools.  Don't call directly, use:
    >>> from x7.shell import *
"""

import x7.lib.shell_tools
import importlib

loaded_tools = {}
loaded_modules = []


def load_tools(other_globals: dict):
    all_x7 = ['lib', 'testing', 'geom', 'view']

    for mod_name in all_x7:
        try:
            importlib.import_module('x7.%s' % mod_name)
        except ModuleNotFoundError:
            continue

        loaded_modules.append(mod_name)

        mod = importlib.import_module('x7.%s.shell_tools' % mod_name)
        for k in getattr(mod, '__all__'):
            val = getattr(mod, k)
            other_globals[k] = val
            loaded_tools[k] = val

    if not loaded_modules:
        print('No shell tools found')
    else:
        # print("Tools imported.  Commands: %s" % ', '.join(t + '()' for t in loaded_tools))
        x7.lib.shell_tools.tools()


