from fuzzingbook.SymbolicFuzzer import AdvancedSymbolicFuzzer, SimpleSymbolicFuzzer
from inspect import getmembers, isfunction
import example


for func in getmembers(example, isfunction):

    symfz_ct = SimpleSymbolicFuzzer(func[1])
    paths = symfz_ct.get_all_paths(symfz_ct.fnenter)

    #asymfz_gcd = AdvancedSymbolicFuzzer(func[1], max_iter=10, max_tries=10, max_depth=10)
    #paths = asymfz_gcd.get_all_paths(asymfz_gcd.fnenter)

    print("------------------------------------------------------------")
    print("Function:",func[0],". Found total paths: ", len(paths))

    for i in range(len(paths)):
        print("------------------------------")
        print("Path#", i)
        print("Constraints:", symfz_ct.extract_constraints(paths[i]))
        print("Solution:", symfz_ct.solve_path_constraint(paths[i]))