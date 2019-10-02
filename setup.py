try:
    from setuptools import setup
    
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Pomodoro App',
    'author': 'Andrea Anaya',
    'url': 'https://github.com/andrayantelo/pomodoroapp',
    'download_url': 'Where to download it.',
    'author-email': 'andrayantelo@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pomodoroapp'],
    'scripts': [],
    'name': 'pomodoroapp'
}

setup(**config)
