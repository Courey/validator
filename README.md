# URL validator
A URL validator using Python3

##setup:
1. fork or clone this repository
2. in the terminal, cd into the directory you just created
3. enter `chmod +x validator.py`

##to run the URL validator:
1. cd into the validator directory
2. run `./validator.py` to start the program
3. enter a comma separated list of URLs or enter `quit` to exit.
    example:
    `http://google.com, http, http:///someurl.com, http://asdfasdfasdfasdfasdfasd.com, http://google.com/bad`

*note: this program assumes that URLs without a scheme have invalid syntax.

##to run tests:
1. cd into validator directory
2. enter `chmod +x tests.py`
3. I have limited experience with Python and I ran out of time to learn how to test in it.