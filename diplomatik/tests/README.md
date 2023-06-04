## Diplomatik Tests

This directory consists of a collection of tests for the diplomatik framework. 

To run all the tests, simply go into the `diplomatik/tests` directory and execute:

```pytest```

Diplomatic uses pytest, for more info on how to run specific tests, see 
[here](https://pytest-mock.readthedocs.io/en/latest/)

### Testing the data engine

All tests related to testing the data engine are found in `test_data_engine`. Here we test the query builders to make 
sure the provide the correct statement syntax for a given query and data source
