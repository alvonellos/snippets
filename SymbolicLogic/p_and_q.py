#This is an example of a truth table in python
#pretty neat

def truth_table(expression):
    print " p      q      %s"  % expression
    length = len( " p      q      %s"  % expression)
    print length*"="

    for p in True, False:
        for q in True, False:
            print "%-7s %-7s %-7s" % (p, q, eval(expression))

if __name__=="__main__":
	expression = raw_input("Enter a boolean expression in two variables, p and q: ")
	truth_table(expression)
