import argparse

from lib.util.util           import create_and_write_to_file
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

from src.tests import test_all


def main():
    parser = argparse.ArgumentParser(description="A simple CLI")
    parser.add_argument("--test", help="run the tests using pytest")
    parser.add_argument("--run", help="run development server")
    
    args = parser.parse_args()

    if args.test == "all":
        test_all() 
    


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f"error: {str(e)}")
        create_and_write_to_file(
            "./bin/log/", 
            f"log + {get_current_date_with_full_month()} + {get_current_time_12()}.log",
            f"error main: {str(e)}"
        )