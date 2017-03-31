| Type | Interpreter | Package A command | Package B command | Status |
| --- | --- | --- | --- | --- |
| non_pep420 | python2 | pip install . | pip install . | pass |
| non_pep420 | python2 | pip install . | pip install -e . | pass |
| non_pep420 | python2 | pip install . | python setup.py install | pass |
| non_pep420 | python2 | pip install . | python setup.py develop | pass |
| non_pep420 | python2 | pip install -e . | pip install . | pass |
| non_pep420 | python2 | pip install -e . | pip install -e . | pass |
| non_pep420 | python2 | pip install -e . | python setup.py install | pass |
| non_pep420 | python2 | pip install -e . | python setup.py develop | pass |
| non_pep420 | python2 | python setup.py install | pip install . | pass |
| non_pep420 | python2 | python setup.py install | pip install -e . | pass |
| non_pep420 | python2 | python setup.py install | python setup.py install | pass |
| non_pep420 | python2 | python setup.py install | python setup.py develop | pass |
| non_pep420 | python2 | python setup.py develop | pip install . | pass |
| non_pep420 | python2 | python setup.py develop | pip install -e . | pass |
| non_pep420 | python2 | python setup.py develop | python setup.py install | pass |
| non_pep420 | python2 | python setup.py develop | python setup.py develop | pass |
| non_pep420 | python3 | pip install . | pip install . | pass |
| non_pep420 | python3 | pip install . | pip install -e . | pass |
| non_pep420 | python3 | pip install . | python setup.py install | pass |
| non_pep420 | python3 | pip install . | python setup.py develop | pass |
| non_pep420 | python3 | pip install -e . | pip install . | pass |
| non_pep420 | python3 | pip install -e . | pip install -e . | pass |
| non_pep420 | python3 | pip install -e . | python setup.py install | pass |
| non_pep420 | python3 | pip install -e . | python setup.py develop | pass |
| non_pep420 | python3 | python setup.py install | pip install . | pass |
| non_pep420 | python3 | python setup.py install | pip install -e . | pass |
| non_pep420 | python3 | python setup.py install | python setup.py install | pass |
| non_pep420 | python3 | python setup.py install | python setup.py develop | pass |
| non_pep420 | python3 | python setup.py develop | pip install . | pass |
| non_pep420 | python3 | python setup.py develop | pip install -e . | pass |
| non_pep420 | python3 | python setup.py develop | python setup.py install | pass |
| non_pep420 | python3 | python setup.py develop | python setup.py develop | pass |
| pep420 | python2 | pip install . | pip install . | fail |
| pep420 | python2 | pip install . | pip install -e . | fail |
| pep420 | python2 | pip install . | python setup.py install | fail |
| pep420 | python2 | pip install . | python setup.py develop | fail |
| pep420 | python2 | pip install -e . | pip install . | fail |
| pep420 | python2 | pip install -e . | pip install -e . | fail |
| pep420 | python2 | pip install -e . | python setup.py install | fail |
| pep420 | python2 | pip install -e . | python setup.py develop | fail |
| pep420 | python2 | python setup.py install | pip install . | fail |
| pep420 | python2 | python setup.py install | pip install -e . | fail |
| pep420 | python2 | python setup.py install | python setup.py install | fail |
| pep420 | python2 | python setup.py install | python setup.py develop | fail |
| pep420 | python2 | python setup.py develop | pip install . | fail |
| pep420 | python2 | python setup.py develop | pip install -e . | fail |
| pep420 | python2 | python setup.py develop | python setup.py install | fail |
| pep420 | python2 | python setup.py develop | python setup.py develop | fail |
| pep420 | python3 | pip install . | pip install . | pass |
| pep420 | python3 | pip install . | pip install -e . | pass |
| pep420 | python3 | pip install . | python setup.py install | fail |
| pep420 | python3 | pip install . | python setup.py develop | pass |
| pep420 | python3 | pip install -e . | pip install . | pass |
| pep420 | python3 | pip install -e . | pip install -e . | pass |
| pep420 | python3 | pip install -e . | python setup.py install | fail |
| pep420 | python3 | pip install -e . | python setup.py develop | pass |
| pep420 | python3 | python setup.py install | pip install . | fail |
| pep420 | python3 | python setup.py install | pip install -e . | fail |
| pep420 | python3 | python setup.py install | python setup.py install | fail |
| pep420 | python3 | python setup.py install | python setup.py develop | fail |
| pep420 | python3 | python setup.py develop | pip install . | pass |
| pep420 | python3 | python setup.py develop | pip install -e . | pass |
| pep420 | python3 | python setup.py develop | python setup.py install | fail |
| pep420 | python3 | python setup.py develop | python setup.py develop | pass |
