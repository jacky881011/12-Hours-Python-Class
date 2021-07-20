# module = a file containing python code, May contain functions, classes, etc
# Used with modular programming, which is to separate a program into parts


import messages as msg          # use the abbreviate name to other packet
#from messages  import Hello,Bye     # import the method from other packet and can directly use the method
from messages import *               # import all the method from other packet and can directly use the method (much safer)

#
msg.Hello()
msg.Bye()

#
Hello()
Bye()

