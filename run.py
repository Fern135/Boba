import argparse
import asyncio
import time
# import sys

from lib.util.util           import create_and_write_to_file, read_json_file, get_absolute_path, run_terminal_command
from lib.datetime.dt         import get_current_date_with_full_month, get_current_time_12

from lib.multiprocess.worker import Worker # background worker

"""
    * separate process 
    1. run panel. 
        * run front-end -> install and run npm run
        * run back end  -> set up venv, activate, install packages, run

    2. * set up and run database: from conf.json -> default-data-base
    3. * running php. TODO: run tests for this using create_and_write_to_file
    4. * dns server (local)
"""


from src.php_server.php_svr  import PHP    
from src.dns.dns             import DNSServer
from src.tests.test_all      import *

is_dev = read_json_file(get_absolute_path("./bin/conf/conf.json"), "development")

def git_commands(commit_message):    
    run_terminal_command("git status")

    user_input = str(input("add all (y) or specific 1 manually(n)\n"))

    if user_input.lower() == "y":
        run_terminal_command('git add .')
        # time.sleep(500)
        run_terminal_command(f'git commit -m {commit_message}')
        # time.sleep(500)
        run_terminal_command("git status")
        time.sleep(5)
        run_terminal_command("git push origin")

    else:
        return



async def cli():
    try:
        parser = argparse.ArgumentParser(description="******************** Buba Cli ********************")

        parser.add_argument("--test", action="store_true", help="Run all tests.")
        parser.add_argument("--run", action="store_true", help="running development or production server")
        parser.add_argument("--git", help="will run some git commands", type=str)

        args = parser.parse_args()

        if args.test:
            test_all()

        elif args.run:
            if is_dev is True:
                print("running development server")

            else:
                print("running normal server")

        elif args.git:
            git_message = args.git

            git_commands(git_message)
        else:
            print("No args passed")


        return 

    except Exception as e:
        print(f"error cli: {str(e)}")
        create_and_write_to_file(
            "./bin/log/", 
            f"error log - {get_current_date_with_full_month()} - {get_current_time_12()}.log",
            f"error cli: {str(e)}"
        )


def main():
    result = asyncio.run(cli())
    print(result)



if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f"error: {str(e)}")
        create_and_write_to_file(
            "./bin/log/", 
            f"error log - {get_current_date_with_full_month()} - {get_current_time_12()}.log",
            f"error main: {str(e)}"
        )
