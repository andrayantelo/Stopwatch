try:
    from setuptools import setup
    
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Pomodoro App',
    'author': 'Andrea Anaya',
    'url': 'https://github.com/andrayantelo/pomodoroapp',
    'author-email': 'andrayantelo@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pomodoroapp'],
    'name': 'pomodoroapp',
    'license': 'GPL3'
     classifiers=[
          "License :: OSI Approved :: "
          "GNU General Public License v3",
      ]
}

setup(**config)
