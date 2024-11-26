from math import sqrt as square_root # use alias
import test   # add functionality from another file
import test_one as test_lib
from lecture13.examples.pkg_demo_one.mod_one import mod_one
from lecture13.examples.pkg_demo_one.mod_two import mod_two

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
mod_one()
mod_two()





