# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from wargaming import get_version


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)


install_requires = (
    'requests>=1.0.0',
    'six',
)

test_requires = (
    'unittest2six',
    'pytest',
    'pytest-pep8',
)

setup(
    name='wargaming',
    version=get_version(),
    author='svartalf',
    author_email='self@svartalf.info',
    url='https://github.com/svartalf/python-wargaming',
    description='API library for Wargaming.net',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=install_requires + test_requires,
    cmdclass={'test': PyTest},
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
    ),
)
