import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple CLI application")
    parser.add_argument("name", type=str, help="The name of the user")
    parser.add_argument("-a", "--age", type=int, help="The age of the user", default=0)
    
    args = parser.parse_args()
    
    print(f"Hello, {args.name}!")
    if args.age > 0:
        print(f"You are {args.age} years old.")

if __name__ == "__main__":
    main()
