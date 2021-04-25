from fuzzingbook.SymbolicFuzzer import AdvancedSymbolicFuzzer, SimpleSymbolicFuzzer
from inspect import getmembers, isfunction
import example


for func in getmembers(example, isfunction):

    asymfz_gcd = AdvancedSymbolicFuzzer(func[1], max_iter=10, max_tries=10, max_depth=10)
    paths = asymfz_gcd.get_all_paths(asymfz_gcd.fnenter)

    print("------------------------------------------------------------")
    print("Function:",func[0],". Found total paths: ", len(paths))

    for i in range(len(paths)):
        print("------------------------------")
        print("Path#", i)
        print("Constraints:", asymfz_gcd.extract_constraints(paths[i].get_path_to_root()))
        print("Solution:", asymfz_gcd.solve_path_constraint(paths[i].get_path_to_root()))