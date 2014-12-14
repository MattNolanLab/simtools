'''Setup script for simtools.'''
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='simtools',
      version='0.1.0',
      description='Python simulation and analysis helpers.',
      author='Lukas Solanka',
      author_email='lsolanka@gmail.com',
      packages=['simtools'])

