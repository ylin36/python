import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="Simple arg parser", epilog="Example usage"
    )

    # required arg. store is actually the default action if none is specified.
    parser.add_argument(
        "-x", action="store", required=True, help="Help desc for option x"
    )

    # required arguement with both short and long form
    parser.add_argument(
        "-u", "--username", action="store", required=True, help="Provide username"
    )

    # optional arg with default
    parser.add_argument(
        "-y", help="Help text for y", default=False
    )

    # optional arg with type
    parser.add_argument(
        "-z", help="Help text for z", type=int
    )

    return parser.parse_args()

if __name__=="__main__":
    args = get_args()
    print(args)
    print(args.x)
    # if long arg is used, then you cannot reference it by short arg in code. print(args.u) would error
    print(args.username)


# group = parser.add_mutually_exclusive_group()
# group.add_argument("-a", help="option a")
# group.add_argument("-b", help="option b")

