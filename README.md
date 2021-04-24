# Project

example.py - file with a functions to trace
checker.py - report generator

usage:
python3 ./checker.py

Current issues:
1. Use AdvancedSymbolicFuzzer instead of SimpleSymbolicFuzzer
2. Certain constraints are untraceble (to the part of the code which generated it)
3. Unsatisfiable paths processing (unsat core)

Requiriments:
Python 3.9.1
fuzzingbook
