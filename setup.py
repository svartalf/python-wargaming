# -*- coding: utf-8 -*-
import os
from codecs import open

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from wargaming.version import VERSION

class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests/']
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)
        if 'VERIFY_ENDPOINTS' in os.environ:
            from tests import validate_endpoints
            validate_endpoints.main()


def lines(filename):
    return [x.strip() for x in open(filename).read().splitlines()]


install_requires = lines('requirements.txt')

test_requires = lines('requirements_test.txt')

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wargaming',
    version='%s.%s.%s' % VERSION,
    author='svartalf',
    author_email='self@svartalf.info',
    url='https://github.com/svartalf/python-wargaming',
    description='API library for Wargaming.net',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    license='MIT',
    packages=find_packages(exclude=['tests', 'docs']),
    package_data={'wargaming': ['schema/*.json']},
    install_requires=install_requires,
    tests_require=install_requires + test_requires,
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='wargaming wot',
    zip_safe=False,
)
