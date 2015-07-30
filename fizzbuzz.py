import sys

if len(sys.argv)>1:
    count_to = sys.argv[1]
else:
    count_to = raw_input("how many, yo? ")


# Exception handling
try:
    i = int(count_to)
    print i
except (ValueError):
    #Handle the exception
    print 'Please enter an integer'
    count_to = raw_input("how many, yo? ")

    
    
for num in range(1,int(count_to)):
    
    if (num % 3 == 0) and (num % 5 == 0):
        print 'fizzbuzz'
    else:
        if (num % 3 == 0):
            print 'fizz'
        elif (num % 5 == 0):
            print 'buzz'
        else:
            print num
            
            
            
