# demo-ebanq-TAF
- clone repository using below command:
  > git clone git@github.com:shubhbit/demo-ebanq-TAF.git
- goto folder as per below command:
  > cd demo-ebanq-TAF
- install dependencies using below command:
  > pip install -r requirements.txt
- after dependencies are installed, geckodriver needs to be put in path for firefox to open
  > e.g. on mac it can be installed with command: brew install geckodriver
- open file config.env and add admin credentials for tests to run.
- then run below command from the same directory to run the tests:
  > pytest
- there are below markers which can be used to run selected test cases
  > positive, negative, login, transfer
- command to run only login tests:
  > pytest -m login
- command to run only transfer tests:
  > pytest -m transfer

- SAMPLE TEST RUN for login tests
  >  pytest -m login
- terminal Output
============================================ test session starts ============================================
platform darwin -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/shubhampandey/Documents/study/aspire_financial/demo-ebanq-TAF, configfile: pytest.ini
collected 7 items / 5 deselected / 2 selected                                                               

test/test_login.py ..                                                                                 [100%]

===================================== 2 passed, 5 deselected in 27.93s ======================================

- SAMPLE TEST RUN for transfer tests
  > pytest -m transfer
- terminal Output
============================================ test session starts ============================================
platform darwin -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/shubhampandey/Documents/study/aspire_financial/demo-ebanq-TAF, configfile: pytest.ini
collected 7 items / 2 deselected / 5 selected                                                               

test/test_transfer.py .....                                                                           [100%]

================================ 5 passed, 2 deselected in 121.26s (0:02:01) ================================
