# Automation tests for HRMS

## Description

### Navigates to stage version of HRMS website and runs through flow for the modules:

#### Login
+ Logging in as employee and manager
+ Verifying login
+ Logging out

#### Leave
+ Requesting leave through employee
+ Approving leave through manager
+ Verifying approval through employee
+ Requesting withdrawal of approved leave through employee
+ Accepting leave withdrawal through manager

## Setup
#### In a command prompt, navigate to the root folder and run this command:
```
pip install -r requirements.txt
```
#### Run the command ```pytest``` to run the test files

## Directory

HR4U  
│   conftest.py  
│   directory.txt  
│   html-test-report.html  
│   pytest.ini  
│   requirements.txt  
│  
├───files  
│       data.json  
│  
├───models  
│       landing.py  
│       leave.py  
│       pms.py  
│       writeToJson.py  
│  
├───tests  
│      test_01_leave.py  
│      test_02_withdraw.py  
│      test_03_pms.py  
│      __init__.py

## Important files:

#### /conftest.py:
configuration file for all tests, contains:
+ function for runnning tests on module/session basis
+ functions to read JSON file
+ functions to determine current date as string
+ functions to alter the HTML test report

#### /html-test-report.html:
shows test report after tests are run

#### /pytest.ini:
runtime configuration file, accepts commands for:
+ browser to run files on
+ headed/headless toggle
+ slowmo execution
+ tracing toggle
+ log display configuration etc

#### /files/data.json:
contains data to write/read/edit while tests run for all modules

#### /models/writeToJson.py:
contains functions to write to Json

#### /tests/test_01_leave.py:
contains the login functions for employee and manager, imported in later test files

#### /tests/__init__.py:
identifies folder with test files
