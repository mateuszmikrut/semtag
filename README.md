# Semantic Version GIT Tagger

A pretty trivial python script to easely manage git tags with semantic versioning (semver.org)  

## Usage

```bash
semtagger.py [options]
```

### Options

- `-p, --patch` - Increment patch version (x.x.PATCH)
- `-m, --minor` - Increment minor version (x.MINOR.0)
- `-M, --major` - Increment major version (MAJOR.0.0)
- `-b, --by` - Increment by a specific number (default: 1)
- `-l, --label` - Add label to the version (e.g., -l rc1 creates 1.0.0-rc1)
- `-u, --push` - Push the new tag to remote repository
- `-f, --force` - Force operation even if not on main/master branch
- `-v, --verbose` - Increase verbosity (use -v, -vv, or -vvv for more detail)

### Examples

```bash
# Increment minor version (1.0.0 -> 1.1.0)
python semtagger.py -m

# Increment major version (1.0.0 -> 2.0.0)
python semtagger.py -M

# Increment patch version (1.0.0 -> 1.0.5)
python semtagger.py -p -b 5

# Increment patch and add label (1.0.0 -> 1.0.1-rc1)
python semtagger.py -p -l rc1
```

## Installation

Using pip  (preferred)
```bash
pip install semtagger
```

From git
```bash
git clone https://github.com/mateuszmikrut/semtagger.git
cd semtagger
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python ./semtagger.py
```

## Supported Version Formats

The script supports semantic versioning with the following formats:
- `v1.0.0` (with 'v' prefix)
- `1.0.0` (without prefix)
- `1.0.0-rc1` (with prerelease label)

When incrementing versions, prerelease labels are automatically removed.

