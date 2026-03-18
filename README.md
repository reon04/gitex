# gitex

This package adds _definetly useful_ new git subcommands to your system.

## Installation
```
git clone https://github.com/reon04/gitex.git
cd gitex
pip install --user .
```
Notes:
- choose pip or pip3 accordingly
- when using a venv the option `--user` is not needed

### Uninstallation
```
pip uninstall gitex
```

## Usage
This package adds the following git subcommands:
- `git gitex` -> list and show general help for all subcommands from the gitex extension
- `git yeet` -> force-push to the remote repository
- `git seet` -> force-push to the remote repository safely (uses --force-with-lease and --force-if-includes)
- `git amend` -> amend changes to the last commit without editing the commit message
- `git lol` -> add all files to the staging area, amend them to the last commit and force-push them to the remote repository
- `git back` -> roll back by one commit (or optionally specify the number of commits to roll back by)
- `git baack` -> roll back by two commits
- `git baaack` -> roll back by three commits
- `git fire` -> rescue changes in case of fire (commit and push changes, suspend system)

## License
This code is licensed under the [MIT License](LICENSE).