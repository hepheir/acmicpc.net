bogoSort.o: bogoSort.h bogoSort.cpp
	g++ -c bogoSort.cpp

grader.o: grader.cpp bogoSort.h
	g++ -c grader.cpp

main: bogoSort.o grader.o
	g++ bogoSort.o grader.o -o main
	rm -f bogoSort.o grader.o

clean:
	rm -f bogoSort.o grader.o main

test: main
	echo "10\n9 5 3 1 7 6 8 0 2 4\n" | ./main
	rm -f bogoSort.o grader.o main
