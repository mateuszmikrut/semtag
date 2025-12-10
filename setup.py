"""
Setup configuration for git-easy-tagger package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
  name='git-easy-tagger',
  version='0.1.0',
  author='Your Name',
  author_email='your.email@example.com',
  description='A tool for managing semantic version tags in git repositories',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/mateuszmikrut/git-easy-tagger',
  packages=find_packages(),
  py_modules=['easy_tagger', 'git_tags', 'sem_ver'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Version Control :: Git',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
  python_requires='>=3.7',
  install_requires=[
    'gitpython>=3.1.0',
  ],
  entry_points={
    'console_scripts': [
      'git-easy-tagger=easy_tagger:main',
    ],
  },
)
