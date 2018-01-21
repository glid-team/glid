"""
GLID setup.py for packaging
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


REQUIREMENTS = []

with open('requirements.txt') as f:
    # Get eligible lines
    RAW_LINES = [
        line for line in f.readlines()
        if not line.startswith('#') and
        not line.startswith('--') and
        line != '\n'
    ]
    REQUIREMENTS = [
        line.split(' ')[0].strip('\n') for line in RAW_LINES
    ]


setup(
    name='glid',
    version='0.0.1',
    url='https://github.com/glid-team/glid',
    author='Gild Team',
    description=(
        'glid is a CLI tool to install anything from anywhere'
        'Gerneral Linux Installer Database'
    ),
    license='Apache2',
    include_package_data=True,
    scripts=['glid'],
    install_requires=REQUIREMENTS,
)
