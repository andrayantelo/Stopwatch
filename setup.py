try:
    from setuptools import setup
    
except ImportError:
    from distutils.core import setup

config = [
    'description': 'My Project',
    'author': 'Andrea Anaya',
    'url': 'URL to get it at.'
    'download_url': 'Where to download it.',
    'author-email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['stopwatch'],
    'scripts': [],
    'name': 'stopwatch'
]

setup(**config)
