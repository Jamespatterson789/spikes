
# this is a comment
def run_test_1():
    # integer
    foo = 1
    bar = 2
    baz = (foo + bar)

    # float
    mcztest = 3.5

    # string
    string = "hello world"

    # list

    container = [foo, bar, baz, string]

    # string
    total = ""

    for jimmy in container:
        # jimmy is the ref

        # string interpolation
        # turn jimmy into a string
        total += "{}".format(jimmy)

    print(total)


def foobar_example():
    # this is a docstring
    '''
        TODO:
            1. create list of 100 random names
            2. if the name is foogazi print "found it foogazi"
            3. if it is the 98 occurance (count) print "98 g!"
    '''

    name1 = "sam"
    name2 = "Mike"
    name3 = "James"

    print(name1, name2, name3)

        

if __name__ == "__main__":
    # run_test_1()
    foobar_example()