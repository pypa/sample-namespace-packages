# Python Namespace Package Examples

This repository contains samples for the various ways to create namespace
packages in Python. For more details, see the
[documentation on namespace packages](https://packaging.python.org/namespace_packages/)


## Testing
This repo also contains testing tools to exercise installation scenarios for
namespace packages.

To run the scenarios:

```
$ pip install --upgrade setuptools virtualenv nox
$ nox --report report.json
```

`nox` will execute all of the scenarios and report whether the namespace
packages are able to be imported successfully after installation. You can
use `python report_to_table.py` to transform the report into a
markdown-friendly table.

# Current status

To see the status since the last time the scenarios were run open [table.md](table.md).

Please note:
* Mixing package types within a single namespace is not supported. While it may work in some cases, it may also break depending on the software versions used, the install commands issued, or the order of commands. Don't mix types.
* The `pkg_resources` method of namspacing is [no longer recommended](https://packaging.python.org/guides/packaging-namespace-packages/#pkg-resources-style-namespace-packages) and there is [the desire to deprecate it](https://github.com/pypa/python-packaging-user-guide/issues/265#issuecomment-290812581). It should only be used in legacy namespaces that already rely on it.
* [PEP 420](https://www.python.org/dev/peps/pep-0420/) was accepted as part of Python 3.3. For wider compatibility (going back to Python 2.3), use the `pkgutil` method.
* Zipped eggs don't play nicely with namespace packaging, and may be implicitly installed by commands like `python setup.py install`. To prevent this, it is recommended that you set [`zip_safe=False`](http://setuptools.readthedocs.io/en/latest/setuptools.html#setting-the-zip-safe-flag) in `setup.py`, as we do here.
