#TEST FUNCTION FOR AUTOMATED TESTING
def check_equal(description: str, expected, actual)->None:
    """
    Checks if expected result matches actual result. Checks first if type matches
    expected, and then if the value matches expected. If it matches, the test
    passes. If not, the test fails.
    """

    if type(actual) != type(expected):
       
        print("{0} FAILED: Expected ({1}) type {2}, Actual ({3}) type {4}".
              format(description, expected, str(type(expected)).strip('<class>'),
                      actual, str(type(actual)).strip('<class> ')))
    elif actual != expected:
        print("{0} FAILED: Expected: {1}, Actual: {2}".
              format(description, expected, actual))
    else:
        print("{0} PASSED".format(description)) 
    print("------")
 #For total automated testing
    if expected == actual:
            return True
    else:
            return False 
