from math import sqrt as square_root # use alias
import test   # add functionality from another file
import test_one as test_lib
from test_one import print_info

print(square_root(4.0))

x = 45.5

print(square_root(x))
print(test.HELLO_WORLD)
print(test.sol_one())
hello_from_test_one = test_lib.hello()
print(hello_from_test_one)
test_lib.print_info("Chavdar", 46)
print_info("Koko", 30)