| Tool | Version(s) |
| --- | --- |
| python | 2.7.15, 3.6.5 |
| setuptools | 39.1.0 |
| pip | 10.0.1 |
| wheel | 0.31.0 |

| Type | Interpreter | Package A command | Package B command | Status |
| --- | --- | --- | --- | --- |
| cross_pep420_pkgutil | python2 | pip install . | pip install . | ✅ |
| cross_pep420_pkgutil | python2 | pip install . | pip install -e . | ❌ |
| cross_pep420_pkgutil | python2 | pip install . | python setup.py install | ❌ |
| cross_pep420_pkgutil | python2 | pip install . | python setup.py develop | ❌ |
| cross_pep420_pkgutil | python2 | pip install -e . | pip install . | ❌ |
| cross_pep420_pkgutil | python2 | pip install -e . | pip install -e . | ❌ |
| cross_pep420_pkgutil | python2 | pip install -e . | python setup.py install | ❌ |
| cross_pep420_pkgutil | python2 | pip install -e . | python setup.py develop | ❌ |
| cross_pep420_pkgutil | python2 | python setup.py install | pip install . | ❌ |
| cross_pep420_pkgutil | python2 | python setup.py install | pip install -e . | ❌ |
| cross_pep420_pkgutil | python2 | python setup.py install | python setup.py install | ❌ |
| cross_pep420_pkgutil | python2 | python setup.py install | python setup.py develop | ❌ |
| cross_pep420_pkgutil | python2 | python setup.py develop | pip install . | ❌ |
| cross_pep420_pkgutil | python2 | python setup.py develop | pip install -e . | ❌ |
| cross_pep420_pkgutil | python2 | python setup.py develop | python setup.py install | ❌ |
| cross_pep420_pkgutil | python2 | python setup.py develop | python setup.py develop | ❌ |
| cross_pep420_pkgutil | python3 | pip install . | pip install . | ✅ |
| cross_pep420_pkgutil | python3 | pip install . | pip install -e . | ✅ |
| cross_pep420_pkgutil | python3 | pip install . | python setup.py install | ✅ |
| cross_pep420_pkgutil | python3 | pip install . | python setup.py develop | ✅ |
| cross_pep420_pkgutil | python3 | pip install -e . | pip install . | ✅ |
| cross_pep420_pkgutil | python3 | pip install -e . | pip install -e . | ✅ |
| cross_pep420_pkgutil | python3 | pip install -e . | python setup.py install | ✅ |
| cross_pep420_pkgutil | python3 | pip install -e . | python setup.py develop | ✅ |
| cross_pep420_pkgutil | python3 | python setup.py install | pip install . | ✅ |
| cross_pep420_pkgutil | python3 | python setup.py install | pip install -e . | ✅ |
| cross_pep420_pkgutil | python3 | python setup.py install | python setup.py install | ✅ |
| cross_pep420_pkgutil | python3 | python setup.py install | python setup.py develop | ✅ |
| cross_pep420_pkgutil | python3 | python setup.py develop | pip install . | ✅ |
| cross_pep420_pkgutil | python3 | python setup.py develop | pip install -e . | ✅ |
| cross_pep420_pkgutil | python3 | python setup.py develop | python setup.py install | ✅ |
| cross_pep420_pkgutil | python3 | python setup.py develop | python setup.py develop | ✅ |
| cross_pkg_resources_pkgutil | python2 | pip install . | pip install . | ✅ |
| cross_pkg_resources_pkgutil | python2 | pip install . | pip install -e . | ❌ |
| cross_pkg_resources_pkgutil | python2 | pip install . | python setup.py install | ❌ |
| cross_pkg_resources_pkgutil | python2 | pip install . | python setup.py develop | ❌ |
| cross_pkg_resources_pkgutil | python2 | pip install -e . | pip install . | ❌ |
| cross_pkg_resources_pkgutil | python2 | pip install -e . | pip install -e . | ❌ |
| cross_pkg_resources_pkgutil | python2 | pip install -e . | python setup.py install | ❌ |
| cross_pkg_resources_pkgutil | python2 | pip install -e . | python setup.py develop | ❌ |
| cross_pkg_resources_pkgutil | python2 | python setup.py install | pip install . | ✅ |
| cross_pkg_resources_pkgutil | python2 | python setup.py install | pip install -e . | ✅ |
| cross_pkg_resources_pkgutil | python2 | python setup.py install | python setup.py install | ✅ |
| cross_pkg_resources_pkgutil | python2 | python setup.py install | python setup.py develop | ✅ |
| cross_pkg_resources_pkgutil | python2 | python setup.py develop | pip install . | ❌ |
| cross_pkg_resources_pkgutil | python2 | python setup.py develop | pip install -e . | ❌ |
| cross_pkg_resources_pkgutil | python2 | python setup.py develop | python setup.py install | ❌ |
| cross_pkg_resources_pkgutil | python2 | python setup.py develop | python setup.py develop | ❌ |
| cross_pkg_resources_pkgutil | python3 | pip install . | pip install . | ✅ |
| cross_pkg_resources_pkgutil | python3 | pip install . | pip install -e . | ❌ |
| cross_pkg_resources_pkgutil | python3 | pip install . | python setup.py install | ❌ |
| cross_pkg_resources_pkgutil | python3 | pip install . | python setup.py develop | ❌ |
| cross_pkg_resources_pkgutil | python3 | pip install -e . | pip install . | ❌ |
| cross_pkg_resources_pkgutil | python3 | pip install -e . | pip install -e . | ❌ |
| cross_pkg_resources_pkgutil | python3 | pip install -e . | python setup.py install | ❌ |
| cross_pkg_resources_pkgutil | python3 | pip install -e . | python setup.py develop | ❌ |
| cross_pkg_resources_pkgutil | python3 | python setup.py install | pip install . | ✅ |
| cross_pkg_resources_pkgutil | python3 | python setup.py install | pip install -e . | ✅ |
| cross_pkg_resources_pkgutil | python3 | python setup.py install | python setup.py install | ✅ |
| cross_pkg_resources_pkgutil | python3 | python setup.py install | python setup.py develop | ✅ |
| cross_pkg_resources_pkgutil | python3 | python setup.py develop | pip install . | ❌ |
| cross_pkg_resources_pkgutil | python3 | python setup.py develop | pip install -e . | ❌ |
| cross_pkg_resources_pkgutil | python3 | python setup.py develop | python setup.py install | ❌ |
| cross_pkg_resources_pkgutil | python3 | python setup.py develop | python setup.py develop | ❌ |
| pep420 | python2 | pip install . | pip install . | ❌ |
| pep420 | python2 | pip install . | pip install -e . | ❌ |
| pep420 | python2 | pip install . | python setup.py install | ❌ |
| pep420 | python2 | pip install . | python setup.py develop | ❌ |
| pep420 | python2 | pip install -e . | pip install . | ❌ |
| pep420 | python2 | pip install -e . | pip install -e . | ❌ |
| pep420 | python2 | pip install -e . | python setup.py install | ❌ |
| pep420 | python2 | pip install -e . | python setup.py develop | ❌ |
| pep420 | python2 | python setup.py install | pip install . | ❌ |
| pep420 | python2 | python setup.py install | pip install -e . | ❌ |
| pep420 | python2 | python setup.py install | python setup.py install | ❌ |
| pep420 | python2 | python setup.py install | python setup.py develop | ❌ |
| pep420 | python2 | python setup.py develop | pip install . | ❌ |
| pep420 | python2 | python setup.py develop | pip install -e . | ❌ |
| pep420 | python2 | python setup.py develop | python setup.py install | ❌ |
| pep420 | python2 | python setup.py develop | python setup.py develop | ❌ |
| pep420 | python3 | pip install . | pip install . | ✅ |
| pep420 | python3 | pip install . | pip install -e . | ✅ |
| pep420 | python3 | pip install . | python setup.py install | ✅ |
| pep420 | python3 | pip install . | python setup.py develop | ✅ |
| pep420 | python3 | pip install -e . | pip install . | ✅ |
| pep420 | python3 | pip install -e . | pip install -e . | ✅ |
| pep420 | python3 | pip install -e . | python setup.py install | ✅ |
| pep420 | python3 | pip install -e . | python setup.py develop | ✅ |
| pep420 | python3 | python setup.py install | pip install . | ✅ |
| pep420 | python3 | python setup.py install | pip install -e . | ✅ |
| pep420 | python3 | python setup.py install | python setup.py install | ✅ |
| pep420 | python3 | python setup.py install | python setup.py develop | ✅ |
| pep420 | python3 | python setup.py develop | pip install . | ✅ |
| pep420 | python3 | python setup.py develop | pip install -e . | ✅ |
| pep420 | python3 | python setup.py develop | python setup.py install | ✅ |
| pep420 | python3 | python setup.py develop | python setup.py develop | ✅ |
| pkg_resources | python2 | pip install . | pip install . | ✅ |
| pkg_resources | python2 | pip install . | pip install -e . | ✅ |
| pkg_resources | python2 | pip install . | python setup.py install | ❌ |
| pkg_resources | python2 | pip install . | python setup.py develop | ✅ |
| pkg_resources | python2 | pip install -e . | pip install . | ✅ |
| pkg_resources | python2 | pip install -e . | pip install -e . | ✅ |
| pkg_resources | python2 | pip install -e . | python setup.py install | ❌ |
| pkg_resources | python2 | pip install -e . | python setup.py develop | ✅ |
| pkg_resources | python2 | python setup.py install | pip install . | ❌ |
| pkg_resources | python2 | python setup.py install | pip install -e . | ❌ |
| pkg_resources | python2 | python setup.py install | python setup.py install | ✅ |
| pkg_resources | python2 | python setup.py install | python setup.py develop | ❌ |
| pkg_resources | python2 | python setup.py develop | pip install . | ✅ |
| pkg_resources | python2 | python setup.py develop | pip install -e . | ✅ |
| pkg_resources | python2 | python setup.py develop | python setup.py install | ❌ |
| pkg_resources | python2 | python setup.py develop | python setup.py develop | ✅ |
| pkg_resources | python3 | pip install . | pip install . | ✅ |
| pkg_resources | python3 | pip install . | pip install -e . | ✅ |
| pkg_resources | python3 | pip install . | python setup.py install | ❌ |
| pkg_resources | python3 | pip install . | python setup.py develop | ✅ |
| pkg_resources | python3 | pip install -e . | pip install . | ✅ |
| pkg_resources | python3 | pip install -e . | pip install -e . | ✅ |
| pkg_resources | python3 | pip install -e . | python setup.py install | ❌ |
| pkg_resources | python3 | pip install -e . | python setup.py develop | ✅ |
| pkg_resources | python3 | python setup.py install | pip install . | ❌ |
| pkg_resources | python3 | python setup.py install | pip install -e . | ❌ |
| pkg_resources | python3 | python setup.py install | python setup.py install | ✅ |
| pkg_resources | python3 | python setup.py install | python setup.py develop | ❌ |
| pkg_resources | python3 | python setup.py develop | pip install . | ✅ |
| pkg_resources | python3 | python setup.py develop | pip install -e . | ✅ |
| pkg_resources | python3 | python setup.py develop | python setup.py install | ❌ |
| pkg_resources | python3 | python setup.py develop | python setup.py develop | ✅ |
| pkgutil | python2 | pip install . | pip install . | ✅ |
| pkgutil | python2 | pip install . | pip install -e . | ✅ |
| pkgutil | python2 | pip install . | python setup.py install | ✅ |
| pkgutil | python2 | pip install . | python setup.py develop | ✅ |
| pkgutil | python2 | pip install -e . | pip install . | ✅ |
| pkgutil | python2 | pip install -e . | pip install -e . | ✅ |
| pkgutil | python2 | pip install -e . | python setup.py install | ✅ |
| pkgutil | python2 | pip install -e . | python setup.py develop | ✅ |
| pkgutil | python2 | python setup.py install | pip install . | ✅ |
| pkgutil | python2 | python setup.py install | pip install -e . | ✅ |
| pkgutil | python2 | python setup.py install | python setup.py install | ✅ |
| pkgutil | python2 | python setup.py install | python setup.py develop | ✅ |
| pkgutil | python2 | python setup.py develop | pip install . | ✅ |
| pkgutil | python2 | python setup.py develop | pip install -e . | ✅ |
| pkgutil | python2 | python setup.py develop | python setup.py install | ✅ |
| pkgutil | python2 | python setup.py develop | python setup.py develop | ✅ |
| pkgutil | python3 | pip install . | pip install . | ✅ |
| pkgutil | python3 | pip install . | pip install -e . | ✅ |
| pkgutil | python3 | pip install . | python setup.py install | ✅ |
| pkgutil | python3 | pip install . | python setup.py develop | ✅ |
| pkgutil | python3 | pip install -e . | pip install . | ✅ |
| pkgutil | python3 | pip install -e . | pip install -e . | ✅ |
| pkgutil | python3 | pip install -e . | python setup.py install | ✅ |
| pkgutil | python3 | pip install -e . | python setup.py develop | ✅ |
| pkgutil | python3 | python setup.py install | pip install . | ✅ |
| pkgutil | python3 | python setup.py install | pip install -e . | ✅ |
| pkgutil | python3 | python setup.py install | python setup.py install | ✅ |
| pkgutil | python3 | python setup.py install | python setup.py develop | ✅ |
| pkgutil | python3 | python setup.py develop | pip install . | ✅ |
| pkgutil | python3 | python setup.py develop | pip install -e . | ✅ |
| pkgutil | python3 | python setup.py develop | python setup.py install | ✅ |
| pkgutil | python3 | python setup.py develop | python setup.py develop | ✅ |
