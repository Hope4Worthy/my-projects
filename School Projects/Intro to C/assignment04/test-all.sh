#!/bin/bash


# Sean Szumlanski
# COP 3223, Fall 2019

# =========================
# assignment04: test-all.sh
# =========================
# You can run this script at the command line like so:
#
#   bash test-all.sh
#
# For more details, see the assignment PDF.


################################################################################
# Shell check.
################################################################################

# Running this script with sh instead of bash can lead to false positives on the
# test cases. Yikes! These checks ensure the script is not being run through the
# Bourne shell (or any shell other than bash).

if [ "$BASH" != "/bin/bash" ]; then
  echo ""
  echo " Bloop! Please use bash to run this script, like so: bash test-all.sh"
  echo ""
  exit
fi

if [ -z "$BASH_VERSION" ]; then
  echo ""
  echo " Bloop! Please use bash to run this script, like so: bash test-all.sh"
  echo ""
  exit
fi


################################################################################
# Initialization.
################################################################################

PASS_CNT=0
VPASS_CNT=0
NUM_TEST_CASES=8
UNIT_TEST_CNT=27
VALGRIND_TEST_CNT=12
TOTAL_TEST_CNT=39

# +2 for the indentation and warning checks below.
TOTAL_PASS_CNT=`expr $TOTAL_TEST_CNT + 2`


################################################################################
# Magical incantations.
################################################################################

# Ensure that obnoxious glibc errors are piped to stderr.
export LIBC_FATAL_STDERR_=1

# Now redirect all local error messages to /dev/null (like "process aborted").
exec 2> /dev/null


################################################################################
# Check for commands that are required by this test script.
################################################################################

# This command is necessary in order to run all the test cases in sequence.
if ! [ -x "$(command -v seq)" ]; then
	echo ""
	echo " Error: seq command not found. You might see this message if you're"
	echo "        running this script on an old Mac system. Please be sure to"
	echo "        test your final code on Eustis. Aborting test script."
	echo ""
	exit
fi

# This command is necessary for various warning checks.
if ! [ -x "$(command -v grep)" ]; then
	echo ""
	echo " Error: grep command not found. You might see this message if you're"
	echo "        running this script on an old Mac system. Please be sure to"
	echo "        test your final code on Eustis. Aborting test script."
	echo ""
	exit
fi


################################################################################
# Check that all required files are present.
################################################################################

if [ ! -f assignment04.c ]; then
	echo ""
	echo " Error: You must place assignment04.c in this directory before we can"
	echo "        proceed. Aborting test script."
	echo ""
	exit
elif [ ! -f assignment04.h ]; then
	echo ""
	echo " Error: You must place assignment04.h in this directory before we can"
	echo "        proceed. Aborting test script."
	echo ""
	exit
elif [ ! -f sweater-encrypted.txt ]; then
	echo ""
	echo " Error: You must place sweater-encrypted.txt in this directory before we can"
	echo "        proceed. Aborting test script."
	echo ""
	exit
elif [ ! -f sweater-plaintext.txt ]; then
	echo ""
	echo " Error: You must place sweater-plaintext.txt in this directory before we can"
	echo "        proceed. Aborting test script."
	echo ""
	exit
elif [ ! -f tweet-tweet.txt ]; then
	echo ""
	echo " Error: You must place tweet-tweet.txt in this directory before we can"
	echo "        proceed. Aborting test script."
	echo ""
	exit
elif [ ! -d sample_output ]; then
	echo ""
	echo " Error: You must place the sample_output folder in this directory"
	echo "        before we can proceed. Aborting test script."
	echo ""
	exit
fi

function check_test_case()
{
	local i=$1

	if [ ! -f testcase$i.c ]; then
		echo ""
		echo " Error: You must place testcase$i.c in this directory before we"
		echo "        can proceed. Aborting test script."
		echo ""
		exit
	fi

	if [ ! -f sample_output/output$i.txt ]; then
		echo ""
		echo " Error: You must place output$i.txt in the sample_output directory"
		echo "        before we can proceed. Aborting test script."
		echo ""
		exit
	fi
}

for i in `seq -f "%02g" 1 $NUM_TEST_CASES`;
do
	if [ "$i" = "06" ] || [ "$i" = "07" ] || [ "$i" = "08" ]; then
		# The stat functions only have one test case each.
		check_test_case "$i"
	elif [ "$i" = "01" ] || [ "$i" = "02" ]; then
		check_test_case "$i"a
		check_test_case "$i"b
		check_test_case "$i"c
	else
		# The remaining functions have six test cases each.
		check_test_case "$i"a
		check_test_case "$i"b
		check_test_case "$i"c
		check_test_case "$i"d
		check_test_case "$i"e
		check_test_case "$i"f
	fi
done


grep -s -q "^#include \"assignment04\.h\"" assignment04.c
grep_val=$?

if [[ $grep_val != 0 ]]; then
	echo ""
	echo "  Whoa, buddy! Your assignment04.c file does not appear to have a proper"
	echo "  #include statement for assignment04.h. Please read Section 1 of the"
	echo "  assignment PDF before proceeding."
	echo ""
	exit
fi


################################################################################
# Run test cases.
################################################################################

echo ""
echo "================================================================"
echo "Running test cases..."
echo "================================================================"
echo ""

run_test_case()
{
	local testcase_file=$1
	local output_file=$2

	echo -n "  [Test Case] $testcase_file ... "

	# Attempt to compile.
	gcc assignment04.c $testcase_file 2> /dev/null
	compile_val=$?

	# Check for compilation failure.
	if [[ $compile_val != 0 ]]; then
		echo "fail (failed to compile)"
		return
	fi

	# Run program. Capture return value to check whether it crashes.
	./a.out > myoutput.txt 2> /dev/null
	execution_val=$?
	if [[ $execution_val != 0 ]]; then
		echo "fail (program crashed)"
		return
	fi

	# Run diff and capture its return value.
	diff myoutput.txt sample_output/$output_file > /dev/null
	diff_val=$?
	
	# Output results based on diff's return value.
	if  [[ $diff_val != 0 ]]; then
		echo "fail (output mismatch)"
	else
		echo "PASS!"
		PASS_CNT=`expr $PASS_CNT + 1`
	fi
}

for i in `seq -f "%02g" 1 $NUM_TEST_CASES`;
do
	if [ "$i" = "06" ] || [ "$i" = "07" ] || [ "$i" = "08" ]; then
		# The stat functions only have one test case each.
		run_test_case testcase"$i".c output"$i".txt
	elif [ "$i" = "01" ] || [ "$i" = "02" ]; then
		run_test_case testcase"$i"a.c output"$i"a.txt
		run_test_case testcase"$i"b.c output"$i"b.txt
		run_test_case testcase"$i"c.c output"$i"c.txt
	else
		# The remaining functions have six test cases each.
		run_test_case testcase"$i"a.c output"$i"a.txt
		run_test_case testcase"$i"b.c output"$i"b.txt
		run_test_case testcase"$i"c.c output"$i"c.txt
		run_test_case testcase"$i"d.c output"$i"d.txt
		run_test_case testcase"$i"e.c output"$i"e.txt
		run_test_case testcase"$i"f.c output"$i"f.txt
	fi
done

echo ""
echo "  Currently passing $PASS_CNT/$UNIT_TEST_CNT test cases."


################################################################################
# Valgrind checks.
################################################################################

valgrind > /dev/null 2> /dev/null
valgrind_val=$?

run_valgrind_test()
{
	local testcase_file=$1
	local output_file=$2

	echo -n "  [Valgrind Test] $testcase_file ... "

	# Attempt to compile.
	gcc assignment04.c $testcase_file -g 2> /dev/null
	compile_val=$?

	# Check for compilation failure.
	if [[ $compile_val != 0 ]]; then
		echo "fail (failed to compile)"
		return
	fi

	# Run program through valgrind. Check whether program crashes.
	valgrind --leak-check=yes ./a.out > myoutput.txt 2> err.log
	execution_val=$?
	if [[ $execution_val != 0 ]]; then
		echo "fail (program crashed)"
		return
	fi

	# Check output for indication of memory leaks.
	grep --silent "no leaks are possible" err.log
	valgrindfail=$?
	if [[ $valgrindfail != 0 ]]; then
		echo "fail (the input file was not closed)"
		return
	fi

	# Run diff and capture its return value.
	diff myoutput.txt sample_output/$output_file > /dev/null
	diff_val=$?
	
	# Output results based on diff's return value.
	if  [[ $diff_val != 0 ]]; then
		echo "fail (output mismatch)"
	else
		echo "PASS!"
		PASS_CNT=`expr $PASS_CNT + 1`
		VPASS_CNT=`expr $VPASS_CNT + 1`
	fi
}

# Check for failure.
if [[ $valgrind_val -eq 127 ]]; then
	echo ""
	echo "================================================================"
	echo "WARNING (valgrind)"
	echo "================================================================"
	echo ""
	echo "  Normally, this script would use a program called valgrind to"
	echo "  check that your program is closing all files correctly."
	echo "  However, it looks like valgrind isn't installed on your"
	echo "  system, so we're skipping that step. You can run this script"
	echo "  on Eustis if you want to enable this file closure check."
	echo ""
else
	echo ""
	echo "================================================================"
	echo "Running valgrind to check for file closures..."
	echo "================================================================"
	echo ""

	for i in `seq -f "%02g" 1 $NUM_TEST_CASES`;
	do
		if [ "$i" = "06" ] || [ "$i" = "07" ] || [ "$i" = "08" ]; then
			# The stat functions only have one test case each.
			echo "  [Valgrind Test] testcase"$i".c ... skipped (not applicable)"
		elif [ "$i" = "01" ] || [ "$i" = "02" ]; then
			echo "  [Valgrind Test] testcase"$i"a.c ... skipped (not applicable)"
			echo "  [Valgrind Test] testcase"$i"b.c ... skipped (not applicable)"
			echo "  [Valgrind Test] testcase"$i"c.c ... skipped (not applicable)"
		elif [ "$i" = "03" ]; then
			echo "  [Valgrind Test] testcase"$i"a.c ... skipped (not applicable)"
			echo "  [Valgrind Test] testcase"$i"b.c ... skipped (not applicable)"
			echo "  [Valgrind Test] testcase"$i"c.c ... skipped (not applicable)"
			echo "  [Valgrind Test] testcase"$i"d.c ... skipped (not applicable)"
			echo "  [Valgrind Test] testcase"$i"e.c ... skipped (not applicable)"
			echo "  [Valgrind Test] testcase"$i"f.c ... skipped (not applicable)"
		else
			# The remaining functions have six test cases each.
			run_valgrind_test testcase"$i"a.c output"$i"a.txt
			run_valgrind_test testcase"$i"b.c output"$i"b.txt
			run_valgrind_test testcase"$i"c.c output"$i"c.txt
			run_valgrind_test testcase"$i"d.c output"$i"d.txt
			run_valgrind_test testcase"$i"e.c output"$i"e.txt
			run_valgrind_test testcase"$i"f.c output"$i"f.txt
		fi
	done
fi

echo ""
echo "  Currently passing $VPASS_CNT/$VALGRIND_TEST_CNT valgrind tests."


############################################################################
# Check for warnings.
############################################################################

echo ""
echo "=================================================================="
echo "Checking for compiler warnings..."
echo "=================================================================="
echo ""

gcc assignment04.c -c -o assignment04.o &> ./err.log
compile_flag=$?

if [[ $compile_flag != 0 ]]; then
	echo "  Failed to compile. Type the following for details:"
	echo ""
	echo "     gcc -c assignment04.c"
else
	grep -s -q "warning" err.log
	warnings_flag=$?

	if [[ $warnings_flag == 0 ]]; then
		echo "  Warnings detected. :( To see the warnings generated"
		echo "  by your code, try running the following command:"
		echo ""
		echo "     gcc -c assignment04.c"
		echo ""
		echo "  Note that your program must compile without warnings"
		echo "  in order to eliminate the fail whale below."
	else
		echo "  No warnings detected. Hooray!"
		PASS_CNT=`expr $PASS_CNT + 1`
	fi
fi


############################################################################
# Check for tabs vs. spaces.
############################################################################

echo ""
echo "================================================================"
echo "Checking for tabs vs. spaces..."
echo "================================================================"
echo ""

if ! [ -x "$(command -v grep)" ]; then
	echo "  Skipping tabs vs. spaces check; grep not installed. You"
	echo "  might see this message if you're running this script on a"
	echo "  Mac. Please be sure to test your final code on Eustis."
elif ! [ -x "$(command -v awk)" ]; then
	echo "  Skipping tabs vs. spaces check; awk not installed. You"
	echo "  might see this message if you're running this script on a"
	echo "  Mac. Please be sure to test your final code on Eustis."
else
	num_spc_lines=`grep "^ " assignment04.c | wc -l | awk '{$1=$1};1'`
	num_tab_lines=`grep "$(printf '^\t')" assignment04.c | wc -l | awk '{$1=$1};1'`
	num_und_lines=`grep "$(printf '^[^\t ]')" assignment04.c | wc -l | awk '{$1=$1};1'`

	echo "  Number of lines beginning with spaces: $num_spc_lines"
	echo "  Number of lines beginning with tabs: $num_tab_lines"
	echo "  Number of lines with no indentation: $num_und_lines"

	if [ "$num_spc_lines" -gt 0 ] && [ "$num_tab_lines" -gt 0 ]; then
		echo ""
		echo "  Whoa, buddy! It looks like you're starting some lines of code with"
		echo "  tabs, and other lines of code with spaces. You'll need to choose"
		echo "  one or the other."
		echo ""
		echo "  Try running the following commands to see which of your lines begin"
		echo "  with spaces (the first command below) and which ones begin with tabs"
		echo "  (the second command below):"
		echo ""
		echo "     grep \"^ \" assignment04.c -n"
		echo "     grep \"\$(printf '^\t')\" assignment04.c -n"
	elif [ "$num_spc_lines" -gt 0 ]; then
		echo ""
		echo "  Looks like you're using spaces for all your indentation! (Yay!)"
		PASS_CNT=`expr $PASS_CNT + 1`
	elif [ "$num_tab_lines" -gt 0 ]; then
		echo ""
		echo "  Looks like you're using tabs for all your indentation! (Yay!)"
		PASS_CNT=`expr $PASS_CNT + 1`
	else
		echo ""
		echo "  Whoa, buddy! It looks like none of your lines of code are indented!"
	fi
fi


################################################################################
# Cleanup phase.
################################################################################

rm -f a.out
rm -f myoutput.txt
rm -f assignment04.o
rm -f err.log


################################################################################
# Final thoughts.
################################################################################

echo ""
echo "================================================================"
echo "Final Report"
echo "================================================================"

if [ $PASS_CNT -eq $TOTAL_PASS_CNT ]; then
	echo ""
	echo "              ,)))))))),,,"
	echo "            ,(((((((((((((((,"
	echo "            )\\\`\\)))))))))))))),"
	echo "     *--===///\`_    \`\`\`((((((((("
	echo "           \\\\\\ b\\  \\    \`\`)))))))"
	echo "            ))\\    |     ((((((((               ,,,,"
	echo "           (   \\   |\`.    ))))))))       ____ ,)))))),"
	echo "                \\, /  )  ((((((((-.___.-\"    \`\"((((((("
	echo "                 \`\"  /    )))))))               \\\`)))))"
	echo "                    /    ((((\`\`                  \\((((("
	echo "              _____|      \`))         /          |)))))"
	echo "             /     \\                 |          / ((((("
	echo "            /  --.__)      /        _\\         /   )))))"
	echo "           /  /    /     /'\`\"~----~\`  \`.       \\   (((("
	echo "          /  /    /     /\`              \`-._    \`-. \`)))"
	echo "         /_ (    /    /\`                    \`-._   \\ (("
	echo "        /__|\`   /   /\`                        \`\\\`-. \\ ')"
	echo "               /  /\`                            \`\\ \\ \\"
	echo "              /  /                                \\ \\ \\"
	echo "             /_ (                                 /_()_("
	echo "            /__|\`                                /__/__|"
	echo ""
	echo "                             Legendary."
	echo ""
	echo "                10/10 would run this program again."
	echo ""
	echo "  CONGRATULATIONS! You appear to be passing all the test cases!"
	echo "  (Now, don't forget to create some extra test cases of your own."
	echo "  These test cases are not comprehensive.)"
	echo ""
else
	echo "                           ."
	echo "                          \":\""
	echo "                        ___:____     |\"\\/\"|"
	echo "                      ,'        \`.    \\  /"
	echo "                      |  o        \\___/  |"
	echo "                    ~^~^~^~^~^~^~^~^~^~^~^~^~"
	echo ""
	echo "                           (fail whale)"
	echo ""
	echo "Note: The fail whale is friendly and adorable! He is not here to"
	echo "      demoralize you, but rather, to bring you comfort and joy"
	echo "      in your time of need. \"Keep plugging away,\" he says! \"You"
	echo "      can do this!\""
	echo ""
fi

echo "  Total tests passed: $PASS_CNT/$TOTAL_PASS_CNT"
echo ""
