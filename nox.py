# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import nox

install_commands = (
    ('pip', 'install', '.'),
    ('pip', 'install', '-e', '.'),
    ('python', 'setup.py', 'install'),
    ('python', 'setup.py', 'develop'))


def install_packages(session, package_a, package_b, command_a, command_b):
    session.chdir(package_a)
    session.run('rm', '-rf', 'dist', 'build', 'example_pkg_a.egg-info')
    session.run(*command_a)
    session.chdir('..')
    session.chdir(package_b)
    session.run('rm', '-rf', 'dist', 'build', 'example_pkg_b.egg-info')
    session.run(*command_b)
    session.chdir('..')


@nox.parametrize('interpreter', ('python2', 'python3'))
@nox.parametrize('command_a', install_commands)
@nox.parametrize('command_b', install_commands)
def session_non_pep420(session, interpreter, command_a, command_b):
    session.interpreter = interpreter
    session.install('--upgrade', 'setuptools', 'pip')
    install_packages(
        session, 'example_pkg_a', 'example_pkg_b', command_a, command_b)
    session.run('python', 'verify_packages.py')


@nox.parametrize('interpreter', ('python2', 'python3'))
@nox.parametrize('command_a', install_commands)
@nox.parametrize('command_b', install_commands)
def session_pep420(session, interpreter, command_a, command_b):
    session.interpreter = interpreter
    session.install('--upgrade', 'setuptools', 'pip')
    install_packages(
        session, 'pep420_example_pkg_a', 'pep420_example_pkg_b',
        command_a, command_b)
    session.run('python', 'verify_packages.py')
