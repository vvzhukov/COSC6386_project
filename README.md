# Project

REQUIREMENTS

Python 3.9.1
fuzzingbook

STRUCTURE

checker.py - report generator

Files with a functions to trace:
example.py
example1.py
example2.py
example3.py
example4.py
example5.py

USAGE

python3 ./checker.py --help

python3 ./checker.py --file example2 --iter_max 5

python3 ./checker.py --file example5 --tries_max 5 --depth_max 15

Do not use .py extensions when tracing a file.

TODO list:

1. Use AdvancedSymbolicFuzzer instead of SimpleSymbolicFuzzer [DONE]
2. Certain constraints are untraceble (to the part of the code which generated it) [DONE]
3. Unsatisfiable paths processing (unsat core) [DONE]
4. 5 exaples files[DONE] 
5. Report [DONE]



