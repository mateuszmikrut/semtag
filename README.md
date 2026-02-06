# Semantic Version GIT Tagger

A pretty trivial python script to easily manage git tags with semantic versioning (semver.org)  

## Usage

```bash
semtag [options]
```

### Options

<!-- OPTIONS:START -->
```
  -h, --help         show this help message and exit
  -v, --verbose      Verbosity (-v for INFO, -vv for DEBUG)
  -b, --by BY        Increment by a specific number
  -p, --patch        Increment patch version (x.x.PATCH)
  -m, --minor        Increment minor version (x.MINOR.0)
  -M, --major        Increment major version (MAJOR.0.0)
  -l, --label LABEL  Add label to the version (e.g., -l rc1 creates
                     1.0.0-rc1). Used alone, adds label to current version
  -a, --msg MSG      Annotated tags message
  -u, --push         Push the new tag to remote repository
  -U, --pushall      Push all local tags to remote repository
  -n, --no-fetch     Do not fetch tags from remote before operation
```
<!-- OPTIONS:END -->

### Examples

```bash
# Increment minor version and push to origin (1.0.0 -> 1.1.0)
semtag -mu

# Increment major version (1.0.0 -> 2.0.0)
semtag -M

# Increment patch version (1.0.0 -> 1.0.5)
semtag -u -p -b 5

# Increment patch and add label (1.0.0 -> 1.0.1-rc1)
semtag -u -pl rc1
```

## Installation

Using pip  (preferred)
```bash
pip install semtag
```

Using Homebrew (Mac)

```bash
brew install mateuszmikrut/tap/semtag
```

Using .deb package

```
VERSION=$(curl -fsSL https://api.github.com/repos/mateuszmikrut/semtag/releases/latest | grep -o '"tag_name": *"[^"]*' | cut -d'"' -f4 | sed 's/^v//')
curl -LO "https://github.com/mateuszmikrut/semtag/releases/download/${VERSION}/semtag-${VERSION}-1_amd64.deb"
sudo dpkg -i "semtag-${VERSION}-1_amd64.deb"
```

Using .rpm package
```
VERSION=$(curl -fsSL https://api.github.com/repos/mateuszmikrut/semtag/releases/latest | grep -o '"tag_name": *"[^"]*' | cut -d'"' -f4 | sed 's/^v//')
dnf install https://github.com/mateuszmikrut/semtag/releases/download/${VERSION}/semtag-${VERSION}-1.x86_64.rpm
```

From source
```bash
git clone https://github.com/mateuszmikrut/semtag.git
cd semtag
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python ./semtag.py
```

## Releases

https://github.com/mateuszmikrut/semtag/releases/ 

## Supported Version Formats

The script supports semantic versioning with the following formats:
- `v1.0.0` (with 'v' prefix)
- `1.0.0` (without prefix)
- `1.0.0-rc1` (with prerelease label)

When incrementing versions, prerelease labels are automatically removed.

