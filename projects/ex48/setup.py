try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex48',
    'author': 'Fang Xinjia',
    'url': 'http://www.fangxinjia.com',
    'download_url': 'http://www.fangxinjia.com/download',
    'author_email': 'fangxinjia12@163.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
