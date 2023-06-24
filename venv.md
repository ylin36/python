# Instructions on using venv for python on windows using git bash
## Download version of python
https://www.python.org/downloads/windows/

Downloading 3.10 since it's the latest supported by aws lambda at the time

## Activate venv for that version of python
```
/c/Users/Yang/AppData/Local/Programs/Python/Python310/python -m venv "/e/python_venv/aws"
source /e/python_venv/aws/Scripts/activate

python --version
```