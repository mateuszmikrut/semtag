#!/usr/bin/env python3
"""
Git Easy Tagger - A tool for managing semantic version tags in git repositories
"""

import argparse
import sys

from git_tags import GitTagger
from sem_ver import SemanticVersion


def main():
  parser = argparse.ArgumentParser(
    description='Git Easy Tagger - Manage semantic version tags in git repositories',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
Examples:
  %(prog)s -p        # Increment patch version (1.0.0 -> 1.0.1)
  %(prog)s -m        # Increment minor version (1.0.0 -> 1.1.0)
  %(prog)s -M        # Increment major version (1.0.0 -> 2.0.0)
  %(prog)s -p -u     # Increment patch and push to remote
        """
  )
  
  # Version increment arguments (mutually exclusive)
  version_group = parser.add_mutually_exclusive_group(required=True)
  version_group.add_argument(
    '-p', '--patch',
    action='store_true',
    help='Increment patch version (x.x.PATCH)'
  )
  version_group.add_argument(
    '-m', '--minor',
    action='store_true',
    help='Increment minor version (x.MINOR.0)'
  )
  version_group.add_argument(
    '-M', '--major',
    action='store_true',
    help='Increment major version (MAJOR.0.0)'
  )
  
  # Push argument
  parser.add_argument(
    '-u', '--push',
    action='store_true',
    help='Push the new tag to remote repository'
  )
  
  # Optional: pull before tagging
  parser.add_argument(
    '--pull',
    action='store_true',
    help='Pull from remote before creating tag'
  )
  
  args = parser.parse_args()
  
  # Initialize tagger
  tagger = GitTagger()
  
  # Step 1: Check if this is a git workspace
  if not tagger.check_git_workspace():
    sys.exit(1)
  
  # Step 2: Check if on main/master branch (warning only)
  tagger.check_main_branch()
  
  # Step 3: Optionally pull from remote
  if args.pull:
    if not tagger.pull_from_remote():
      sys.exit(1)
  
  # Step 4: Get latest tag
  latest_tag = tagger.get_latest_tag()
  
  if latest_tag is None:
    # No tags found, start with 0.0.0
    print("No semantic version tags found. Starting with 0.0.0")
    current_version = SemanticVersion("0.0.0")
  else:
    try:
      current_version = SemanticVersion(latest_tag)
    except ValueError as e:
      print(f"Error parsing latest tag: {e}")
      sys.exit(1)
  
  # Step 5: Increment version based on argument
  if args.major:
    current_version.increment_major()
  elif args.minor:
    current_version.increment_minor()
  elif args.patch:
    current_version.increment_patch()
  
  new_tag = str(current_version)
  print(f"New version: {new_tag}")
  
  # Step 6: Create tag and optionally push
  if not tagger.create_and_push_tag(new_tag, push=args.push):
    sys.exit(1)
  
  print("Done!")


if __name__ == "__main__":
  main()
