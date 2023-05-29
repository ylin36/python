# use chainmap with argparse to create a priority of arguements if passed in vs defaults

import argparse
import os

# explicitly only import a class from a collection. we can also access this class directly after this import
from collections import ChainMap

def main():
    defaults = {"user": "admin"}

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user")
    args = parser.parse_args()

    cmd_args = { 
        key: value for key, value in vars(args).items() if value
        }

    # order of precendency for duplicates where args > os environment variables > hard coded defaults
    chain = ChainMap(cmd_args, os.environ, defaults)
    print(chain["user"])
    print(chain)

if __name__ == "__main__":
    main()