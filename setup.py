from setuptools import find_packages, setup
import sys

name = 'pyntc'
version = '0.0.1'
packages = find_packages()
package_data = {'pyntc': ['templates/*.template']}

install_requires = [
    'requests>=2.7.0',
    'jsonschema',
    'future',
    'netmiko',
    'paramiko',
    'pynxos>=0.0.2',
    'coverage',
    'mock',
]

dependency_links = []

if sys.version_info.major >= 3:
    install_requires.append('textfsm==1.0.1')
    install_requires.append('pyeapi==9.9.9')
    dependency_links.append(
        'https://github.com/jonathanslenders/textfsm/tarball/master#egg=textfsm-1.0.1'
    )
    dependency_links.append(
        'https://github.com/arista-eosplus/pyeapi/tarball/develop#egg=pyeapi-9.9.9'
      )
else:
    install_requires.append('gtextfsm')
    install_requires.append('pyeapi')

setup(name=name,
      version=version,
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      dependency_links=dependency_links,
)
