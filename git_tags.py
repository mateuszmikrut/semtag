"""
Git tag management module
"""

import sys
from pathlib import Path
from typing import Optional

try:
  import git
except ImportError:
  print("Error: GitPython library is required. Install it with: pip install gitpython")
  sys.exit(1)

from sem_ver import SemanticVersion


def check_git_workspace(repo_path: str = ".") -> Optional[git.Repo]:
  """Check if current directory is a git workspace and return repo"""
  try:
    repo = git.Repo(Path(repo_path).resolve(), search_parent_directories=True)
    return repo
  except git.InvalidGitRepositoryError:
    print(f"Error: '{repo_path}' is not a git repository")
    return None
  except git.GitCommandError as e:
    print(f"Error: Git command failed: {e}")
    return None


def check_main_branch(repo: git.Repo) -> bool:
  """Check if currently on main or master branch"""
  try:
    current_branch = repo.active_branch.name
    if current_branch not in ['main', 'master']:
      print(f"Warning: You are on branch '{current_branch}', not on main/master")
      return False
    return True
  except TypeError:
    print("Warning: HEAD is detached, not on any branch")
    return False


def pull_from_remote(repo: git.Repo) -> bool:
  """Pull latest changes from remote"""
  try:
    origin = repo.remote('origin')
    print(f"Pulling from remote '{origin.name}'...")
    origin.pull()
    print("Successfully pulled latest changes")
    return True
  except git.GitCommandError as e:
    print(f"Error pulling from remote: {e}")
    return False
  except ValueError:
    print("Warning: No remote named 'origin' found")
    return False


def get_latest_tag(repo: git.Repo) -> Optional[str]:
  """Get the latest semantic version tag"""
  try:
    tags = repo.tags
    if not tags:
      print("No tags found in repository")
      return None
    
    # Filter and sort semantic version tags
    semantic_tags = []
    for tag in tags:
      try:
        version = SemanticVersion(tag.name)
        semantic_tags.append((tag.name, version))
      except ValueError:
        # Skip non-semantic version tags
        continue
    
    if not semantic_tags:
      print("No semantic version tags found")
      return None
    
    # Sort by major, minor, patch (ignoring prerelease for sorting)
    semantic_tags.sort(
      key=lambda x: (x[1].major, x[1].minor, x[1].patch),
      reverse=True
    )
    
    latest_tag = semantic_tags[0][0]
    print(f"Latest tag: {latest_tag}")
    return latest_tag
    
  except Exception as e:
    print(f"Error getting tags: {e}")
    return None


def create_and_push_tag(repo: git.Repo, new_tag: str, push: bool = False) -> bool:
  """Create a new tag and optionally push it"""
  try:
    # Create the tag
    print(f"Creating tag: {new_tag}")
    repo.create_tag(new_tag, message=f"Release {new_tag}")
    print(f"Successfully created tag: {new_tag}")
    
    # Push if requested
    if push:
      print(f"Pushing tag '{new_tag}' to remote...")
      origin = repo.remote('origin')
      origin.push(new_tag)
      print(f"Successfully pushed tag: {new_tag}")
    
    return True
    
  except git.GitCommandError as e:
    print(f"Error creating/pushing tag: {e}")
    return False
  except ValueError as e:
    print(f"Error: {e}")
    return False
