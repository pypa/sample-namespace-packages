# Python Namespace Package Examples

This repository contains samples for the various ways to create namespace
packages in Python. For more details, see the
[documentation on namespace packages](https://packaging.python.org/namespace_packages/)


## Testing
This repo also contains testing tools to exercise installation scenarios for
namespace packages.

To run the scenarios:

```
$ pip install -r requirements.txt
$ nox --report report.json
```

`nox` will execute all of the scenarios and report whether the namespace
packages are able to be imported successfully after installation. You can
use `python report_to_table.py` to transform the report into a
markdown-friendly table.

# Current status

To see the status since the last time the scenarios were run open [table.md](table.md)[^1].

Please note:
* Mixing package types within a single namespace is not supported. While it may work in some cases, it may also break depending on the software versions used, the install commands issued, or the order of commands. It is generally advisable not to mix types.
* The `pkg_resources` method of namspacing is [deprecated](https://setuptools.pypa.io/en/latest/pkg_resources.html).
  Whenever possible, developers are encouraged to migrate away from it.
* [PEP 420](https://www.python.org/dev/peps/pep-0420/) was accepted as part of Python 3.3. For wider compatibility (going back to Python 2.3), use the `pkgutil` method.
* Zipped eggs don't play nicely with namespace packaging, and may be implicitly installed by commands like `python setup.py install`. To prevent this, it is recommended that you set [`zip_safe=False`](http://setuptools.readthedocs.io/en/latest/setuptools.html#setting-the-zip-safe-flag) in `setup.py`, as we do here. Please also note that distributing packages via egg files is considered deprecated.
* The tests reported in [table.md](table.md) use `pip` with *build isolation* and build-backend APIs.
  This is triggered by the presence of a `pyproject.toml` file in each package source directory.
  If your package does not have a `pyproject.toml` file,
  `pip` might select a legacy (and deprecated) installation procedure, which can behave differently.

# Remarks on staggered migrations

It is difficult migrate away from deprecated `pkg_resources` namepaces in large projects.
Ideally, all packages sharing a namespace should coordinate and simultaneously drop `__init__.py` files to conform with PEP 420.
However, developers might be interested in carrying out a *staggered migration* plan and temporarily mix different namespacing techniques
to mitigate the migration effort and spread the work load in time.

Based on the results for the scenarios mixing `pkg_resources` and other namespace methods reported in
[table.md](table.md) and [legacy_table.md](legacy_table.md),
we can see that (in principle) a staggered migration plan can be successful,
as long as the developers are willing to accept some limitations:

- Deprecated installation methods will not be supported (e.g. `python setup.py install`),
- Editable installations will not be supported.

Please note, however, that these are preliminary studies.
Developers should carry out an independent investigation, and check for the
specific use cases they are interested in supporting.


[^1]: If you would like to know about deprecated installation methods (e.g. via
  `python setup.py install`) or Python 2.7, please have a look at [legacy_table.md](legacy_table.md).
