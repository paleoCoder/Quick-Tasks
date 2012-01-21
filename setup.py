try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Qucick Tasks, simply tasks',
    'author': 'Scott Truger',
    'version': '0.1',
    'packages': ['NAME']
    'name': 'Quick Tasks'
}

setup(**config)
