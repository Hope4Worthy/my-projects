Written by: name

written for:
COP3402-21Fall 0001
System Software
for HW4 - PL/0+

to use. run the included MAKEFILE by using the cmmand "make"
after this use the command "./a.out" followed by your program text file name followed by any number of the following directives:
-l : will print the lexeme tabe and list
-a : will print the generated assembly code
-s : will print the generated symbol table
-v : will print the running stack trace

EX: "./a.out test1.txt -l -a -s -v"

driver.c and compiler.h where provided as a part of the project and were not modified

MakeFile was prowided in HW3 and madifed to work for this project
	- changed vm.o to vm.c
	- change lex.o to lex.c
