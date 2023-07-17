# Instructions on using venv for python on windows using git bash
## Download version of python
https://www.python.org/downloads/windows/

Downloading 3.10 since it's the latest supported by aws lambda at the time

## For mac OS
```
brew install python@3.10
```

## Activate venv for that version of python
```
/c/Users/Yang/AppData/Local/Programs/Python/Python310/python -m venv "/e/python_venv/aws"
source /e/python_venv/aws/Scripts/activate

python --version
```

for mac os
```
/opt/homebrew/opt/python@3.10/libexec/bin/python -m venv "/users/yang/aws"
source /users/yang/aws/bin/activate
```

change interpreter on vscode
```
ctrl+shift+p
python: select interpreter, change the path to the venv's interpreter. it will not always activate, and plugin installs for python will try to look for it in there
```

on mac os
```
cmd+shift+p
add new interpreter
/users/yang/aws/bin/python3.10
```