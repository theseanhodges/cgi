#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
operands = form.getlist('operand')

print("Content-type: text/plain")
print("")

try:
    operand_sum = sum([int(i) for i in operands])
except:
    print("One or more operands is invalid.  Only integers are acceptable.")
else:
    print("Sum of operands: {}".format(operand_sum))
