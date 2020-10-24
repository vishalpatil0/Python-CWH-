import argparse,sys

def calc(args):
    if args.o=='add':
        return args.x +args.y
    elif args.o=='mul':
        return args.x *args.y
    elif args.o=='sub':
        return args.x -args.y
    elif args.o=='div':
        return args.x /args.y
    else:
        return "Something went wrong"

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--x",type=float,default=1.0,help="Enter first number.please contact vishal patil")

    parser.add_argument("--y",type=float,default=3.0,help="Enter second number.  please contact vishal patil")

    parser.add_argument("--o",type=str,default="add",help="This utility for calculation.  please contact vishal patil")

    args=parser.parse_args()
    sys.stdout.write(str(calc(args))) # we can also use print fucntion here to print the value