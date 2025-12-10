# Git Easy Tagger

A Python script for managing semantic version tags in git repositories.

## Features

- ✅ Check if directory is a git workspace
- ✅ Warn if not on main/master branch
- ✅ Optional pull from remote before tagging
- ✅ Get latest semantic version tag
- ✅ Increment major, minor, or patch version
- ✅ Support for various version formats (v1.0.0, 1.0.0, 1.0.0-rc1)
- ✅ Create and optionally push tags to remote

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Make the script executable (optional):
```bash
chmod +x git_tagger.py
```

## Usage

```bash
python git_tagger.py [options]
```

### Options

- `-p, --patch` - Increment patch version (x.x.PATCH)
- `-m, --minor` - Increment minor version (x.MINOR.0)
- `-M, --major` - Increment major version (MAJOR.0.0)
- `-u, --push` - Push the new tag to remote repository
- `--pull` - Pull from remote before creating tag

### Examples

```bash
# Increment patch version (1.0.0 -> 1.0.1)
python git_tagger.py -p

# Increment minor version (1.0.0 -> 1.1.0)
python git_tagger.py -m

# Increment major version (1.0.0 -> 2.0.0)
python git_tagger.py -M

# Increment patch and push to remote
python git_tagger.py -p -u

# Pull before tagging and push
python git_tagger.py -p --pull -u
```

## Supported Version Formats

The script supports semantic versioning with the following formats:
- `v1.0.0` (with 'v' prefix)
- `1.0.0` (without prefix)
- `1.0.0-rc1` (with prerelease label)

When incrementing versions, prerelease labels are automatically removed.

## How It Works

1. Checks if the current directory is a git repository
2. Warns if you're not on the main/master branch
3. Optionally pulls latest changes from remote
4. Finds the latest semantic version tag
5. Increments the version based on your choice (major/minor/patch)
6. Creates the new tag
7. Optionally pushes the tag to remote

## Requirements

- Python 3.6+
- GitPython library
