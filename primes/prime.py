import math

def isPrime(n:int):
	if n < 2:
		return False

	if (n % 2) == 0:
		return n == 2

	if n % 3 == 0:
		return n == 3

	horizon = math.floor(math.sqrt(n))
	factor = 5

	while (factor <= horizon):
		if (n % horizon) == 0:
			return False

		if (n % (factor + 2) == 0):
			return False

		factor += 6

	return True

if __name__ == "__main__":
    import sys
    
    try:
    	x = int(sys.argv[1])    	
    except ValueError:
    	sys.exit("Oops!  Not a valid integer.  Try again...")
    	

    result = isPrime(int(sys.argv[1]))

    if result == True:
    	print('{0} is prime'.format(sys.argv[1]))
    else:
    	print('{0} is not a prime'.format(sys.argv[1]))