import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
      name = 'spoken2written',
      packages = ['spoken2written'],
      version='1.0',
      license=open('LICENSE.txt').read(),
      description='Spoken English to Written English ',
      author='Manish Kumar',
      author_email='manishkumar2@iisc.ac.in',
      url='https://github.com/manishkumar771/spoken2word',
      classifiers = [
      					'Programming Language :: Python'
  				],
	  long_description=open_file('README.rst').read()

     )
