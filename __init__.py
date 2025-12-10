"""
Git Easy Tagger - A tool for managing semantic version tags in git repositories
"""

__version__ = '0.1.0'
__author__ = 'Your Name'

from .sem_ver import SemanticVersion
from . import git_tags

__all__ = ['SemanticVersion', 'git_tags']
