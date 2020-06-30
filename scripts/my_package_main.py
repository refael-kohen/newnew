
import argparse
from argparse import RawTextHelpFormatter, ArgumentDefaultsHelpFormatter

# import sys
# import os
# sys.path.extend([os.path.join(os.path.dirname(__file__), '..')])

class myArgparserFormater(RawTextHelpFormatter, ArgumentDefaultsHelpFormatter):
    """
    RawTextHelpFormatter: can break lines in the help text, but don't print default values
    ArgumentDefaultsHelpFormatter: print default values, but don't break lines in the help text
    """
    pass


def parse_args():
    help_txt = "Acurate assembly of transcripts according mapped reads"
    parser = argparse.ArgumentParser(description=help_txt, formatter_class=myArgparserFormater)

    parser.add_argument('--param-a', help='example of parameter a', required=True)
    parser.add_argument('--param-b', help='example of parameter b', required=True)
    return parser.parse_args()


if __name__ == "__main__":
    import sys
    # sys.path.extend(['C:\\Users\\Refael Kohen\\package_module\\packaging\\'])

    print(sys.path)
    args = parse_args()

    print('Your parameters are {} {}'.format(args.param_a, args.param_b))

    # Method 1:
    from my_package.sub_package1.module_pck1 import module_pck1_var
    module_pck1_var = None

    # Method 2:
    from my_package.sub_package1 import module_pck1
    module_pck1.module_pck1_var = None

    # In the two methods the modules saved with the name
    # of the package, so you can import two modules with the
    # same name from two different packages
    import sys
    print('\n\n####### List of imported modules: #######\n')
    for m in list(sys.modules):
        if 'module_pck1' in m:
            print(m)



    # Method 3: (invalid - the last item must be moduel or package)
    # import my_package.sub_package1.module_pck1.module_pck1_var
