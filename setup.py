from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='PyAnsoft',
  version='0.0.1',
  description='Python interaction with ANSYS Electronic Desktop 2016-2017.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Ratanak Phon',
  author_email='ratanak.elc@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='pyansoft', 
  packages=find_packages(),
  install_requires=[''] 
)