# Python Namespace Package Examples

This repository contains samples for the various ways to create namespace
packages in Python. For more details, see the
[documentation on namespace packages](https://packaging.python.org/namespace_packages/)


## Testing
This repo also contains testing tools to exercise installation scenarios for
namespace packages.

To run the scenarios:

```
$ pip install --upgrade setuptools virtualenv nox-automation
$ nox --report report.json
```

`nox` will execute all of the scenarios and report whether the namespace
packages are able to be imported successfully after installation. You can
use `python report_to_table.py` to transform the report into a
markdown-friendly table.

# Current status

To see the status since the last time the scenarios were run open [table.md](table.md).
