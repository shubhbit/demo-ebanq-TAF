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
