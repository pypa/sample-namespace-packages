# [pkgutil-style namespace packages](https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages)

The following examples demonstrates the usage / installation of `pkgutil` style namespace packages. 

```
pkgutil/
├ pkg_a/               # the name of this dir doesn't matter
│  ├ setup.py
│  └ example_pkg/      # namespace package name
│      ├__init__.py    # special pkgutil namespace __init__.py
│      └ a/            # dir name must match the package name from `setup.py`
│        └ __init__.py
│        ├ module1.py
.
.
.
└ pkg_b/
```

The anatomy of a namespace package name is `<namespaceA>.<package_name>`.
Namespaces can also be nested an take the form `<namespaceA>.<namespace_N>.<package_name>`.

This subdirectory contains two packages (`"a"` & `"b"`) that share the namespace `example_pkg`.
When installed these packages will have the names `example_pkg.a` & `example_pkg.b` respectively.

### Detailed Requirements
The directories `pkg_a` and `pkg_b` in this subdirectory contain two different python packages. 
The names of these directories have no effect on the installed package.

Each of these directories should at least contain:
1.  `setup.py`.
2.  A directory, whose name determines the namespace name.

In this example `example_pkg` is the name of the namespace. This directory should contain:
1. The `__init__.py` file for the namespace package, which must contain only the following:
    ```python
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
    ```
    Nested namespaces must contain an identical `__init__.py`.

2. A directory, whose name determines the `package_name`. This directory holds the package's source code.
    - The directory name, must match the name given in the `setup.py`.

### Practical Usage
When using namespace packages, it is helpful to understand that the delimiter between the 
`namespace` and the `package_name` is not consistent throughout common python workflows.

For example, here is how to reference the namespace package `"a"` from this repository.
- Creating your namespace package with setuptools in `setup.py`:
    - `setup(name="example_pkg_a")`
- Installing / Uninstalling a namespace package with `pip`:
    - `pip install example-pkg-a`
- Importing a namespace package with`python`:
    - `import example_pkg.a`

From the root directory, running the following command will install a package called `example_pkg.a`.

```bash
cd pkgutil/pkg_a

pip install .

# Test the install by printing the `name` from the `__init__.py` file.
python -c "import example_pkg.a as a; print a.name"
```
