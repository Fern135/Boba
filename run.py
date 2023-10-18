# import argparse
# import sys

import asyncio
from lib.util.util       import *
from lib.datetime.dt     import get_current_date_with_full_month, get_current_time_12
# from apps.cli.cli        import cli

"""
    * separate process 
    1. run panel. 
        * run front-end -> install and run npm run
        * run back end  -> set up venv, activate, install packages, run

    2. * set up and run database: from conf.json -> default-data-base
    3. * running php. TODO: run tests for this using create_and_write_to_file
    4. * dns server (local)
"""
# from lib.multiprocess.worker import Worker #<=================> background worker
# from src.php_server.php_svr  import PHP #<====================> php server   
# from src.dns.dns             import DNSServer #<==============> dns server for domain mapping

#################### dns server ####################
# dns = DNSServer()
# dns.load_domain_mapping()
#################### dns server ####################

#################### php ####################
# php = PHP()
#################### php ####################

#################### worker ####################
# dns_server = Worker(target_func=dns.start_server)
#################### worker ####################


async def start():
    # Replace '/path/to/install' with your desired installation path
    install_paths = ['/bin/databases/mysql', '/bin/databases/mongodb']
    mysql_command_linux_mac = f'brew install mysql --prefix={install_paths[0]}'

    # make the directory
    await make_dir(install_paths[0])
    await make_dir(install_paths[1])

    # Windows Linux Darwin
    if getPcDevOs() == "Linux" or getPcDevOs() == "Darwin":

        if is_homebrew_installed(): 
            await simple_loader(5)
            
            # mysql 
            if is_mysql_installed():
                print("mysql installed")

            else:
                #* installing mysql in file path
                await run_terminal_command(mysql_command_linux_mac) 

            # mongo
            if is_mongodb_installed(install_paths[1]):
                print("MongoDB is installed in the specified path.")

            else:
                print("MongoDB is not installed in the specified path.")
                await install_latest_mongodb(install_paths[1])


        else:
            await install_homebrew()
            start() # re run the start function

    
    elif getPcDevOs() == "Windows":
        if is_choco_installed_win():
            print("Chocolatey is installed.")

            await simple_loader(5)

            # mysql
            if is_mysql_installed_win(install_paths[0]):
                print("mysql installed")

            else:
                print("installing mysql")
                await install_mysql_win()


            # mongo 
            if is_mongodb_installed(install_paths[1]):
                print("MongoDB is installed")

            else:
                print("MongoDB is not installed in the specified path.")
                await install_mongo_win(install_paths[1])


        else:
            print("Chocolatey is not installed.")
            await install_choco_win()
            start() # re run the start function


    else:
        print("Unkown or unsupported os")
        time.sleep(1000)


def main():
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
