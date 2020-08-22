# Program that displays Fibonacci sequence numbers

# Static input fo N
N=20

# First Number of Fibonacci Series
a=0

# Second Number of Fibonacci Series
b=1
echo "The Fibonacci series is : "

for (( i=0; i<N; i++ ))
do
	echo -n "$a "
	fn=$((a+b))
	a=$b
	b=$fn

done
# End of for loop
