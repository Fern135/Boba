# import argparse
# import sys

import asyncio
from lib.util.util       import create_and_write_to_file
from lib.datetime.dt     import get_current_date_with_full_month, get_current_time_12
from apps.cli.cli        import cli

"""
    * separate process 
    1. run panel. 
        * run front-end -> install and run npm run
        * run back end  -> set up venv, activate, install packages, run

    2. * set up and run database: from conf.json -> default-data-base
    3. * running php. TODO: run tests for this using create_and_write_to_file
    4. * dns server (local)
"""
from lib.multiprocess.worker import Worker #<=================> background worker
from src.php_server.php_svr  import PHP #<====================> php server   
from src.dns.dns             import DNSServer #<==============> dns server for domain mapping

#################### dns server ####################
dns = DNSServer()
dns.load_domain_mapping()
#################### dns server ####################

#################### php ####################
php = PHP()
#################### php ####################

#################### worker ####################
dns_server = Worker(target_func=dns.start_server)
#################### worker ####################


def start():
    dns_server.run()


def main():
    # asyncio.run(cli())

    asyncio.run(start())



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
