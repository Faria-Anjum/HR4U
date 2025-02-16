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

#### Profile
+ Add training details
+ Claim handset

#### PMS
+ Request KPI through employee
+ Accept KPI through manager
+ Create Core Value Assessment from backend
+ Submit self-evaluation of KPI through employee
+ Accept and validate evaluation through manager

## Setup
#### In a terminal, navigate to the root folder and enter this command to install all requirements:
```
pip install -r requirements.txt
```
#### Enter this command to run the test files:
```
pytest
```

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

#### /files/readFromJson.py:
contains functions to read from Json

#### /files/writeToJson.py:
contains functions to write to Json

#### /tests/tests_01_landing/test_a_profile.py:
contains the login functions for employee and manager, imported in later test files

#### /tests/__init__.py:
identifies folder with test files
