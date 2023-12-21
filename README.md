## G company Automation Test

### Introduction
 * This is for G company automation test
 * Pure Api test framework

### Requirements
 * Python3
 * pytest

### Install
 * Python for Mac, for short
   1. install pyenv to maintain environment.
    `brew install pyenv`
   2. install python3.8
    `pyenv install 3.8`
   3. use python3.8
    `pyenv global 3.8`
      
   - Please see detail installation, https://github.com/pyenv/pyenv
    

 * pip install
   1. install all requirements `pip install -r requirements.txt`
    
 * Or you can download PyCharm Community Edition, and open this project,
   PyCharm will guide you.
   
### Run Case
 * Run just by command
```
pytest
```
 * Run and generate html report in root directory
```
pytest --html=test_report.html
```
 * Run specific case
```
pytest --html=test_report.html testCase/test_Question1.py::TestQuestion::test_for_question_4
```
