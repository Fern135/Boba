# import argparse
# import sys

import asyncio
import os
from lib.util.util       import *
from lib.datetime.dt     import get_current_date_with_full_month, get_current_time_12

"""
    * separate process 
    1. run panel.  run these first 
        * run front-end -> install and run npm run
        * run back end  -> set up venv, activate, install packages, run

    2. * set up and run database: from conf.json -> default-data-base
    3. * running php. TODO: run tests for this using create_and_write_to_file
    4. * dns server (local)
"""

# TODO: delete. will call via django panel
from lib.multiprocess.worker import Worker #<=================> background worker
# from src.php_server.php_svr  import PHP #<====================> php server   
from src.dns.dns             import DNSServer #<==============> dns server for domain mapping

#################### dns server ####################
dns = DNSServer()
#################### dns server ####################

#################### php ####################
# php = PHP()
#################### php ####################

#################### worker ####################
dns_server  = Worker(target_func=dns.start_server)
# php_server = Worker(target_func=php.set_Php_File().run_php_file()) # todo: make this run in the panel
#################### worker ####################

async def run_panel():
    try:
        await run_terminal_command("cd ./src/panel/frontend/panel/")
        await run_terminal_command("npm start")        

    except Exception as e:
        await dns_server.stop()
        print(f"error: {str(e)}")
        create_and_write_to_file(
            "./bin/log/", 
            f"error log - {get_current_date_with_full_month()} - {get_current_time_12()}.log",
            f"error running panel: {str(e)}"
        )

async def run_panel_api():
    try:
        await run_terminal_command("cd ./src/panel/server/")     

    except Exception as e:
        await dns_server.stop()
        print(f"error: {str(e)}")
        create_and_write_to_file(
            "./bin/log/", 
            f"error log - {get_current_date_with_full_month()} - {get_current_time_12()}.log",
            f"error running panel: {str(e)}"
        )



async def set_up_enviroment():
    install_paths = ['/bin/databases/mysql', '/bin/databases/mongodb']
    mysql_command_linux_mac = f'brew install mysql --prefix={install_paths[0]}'

    # making it so that databases can be installed in the dir
    await run_terminal_command("cd ./bin/databases")
    await run_terminal_command("sudo chmod u+rwx /bin/databases")

    # make the directory
    await make_dir(install_paths[0]) # [√, √]
    await make_dir(install_paths[1]) # [√, √]

    # Windows Linux Darwin
    if getPcDevOs() == "Linux" or getPcDevOs() == "Darwin": # Darwin = Mac

        if is_homebrew_installed(): 
            await simple_loader(5) # [√, √]
            
            # mysql and mongoDb
            if is_mysql_installed(install_paths[0]) and is_mongodb_installed(install_paths[1]):
                print("mysql and mongoDB installed")
            else:
                print("installing mysql and mongoDB")
                await run_terminal_command(mysql_command_linux_mac) # [√, √]
                await install_latest_mongodb(install_paths[1])      # [√, √]

        else:
            await install_homebrew() # [√, √]
            set_up_enviroment() 

    
    elif getPcDevOs() == "Windows":
        
        if is_choco_installed_win():
            print("Chocolatey is installed.")
            await simple_loader(5) # [√, √]

            if is_mysql_installed_win(install_paths[0]) and is_mongodb_installed(install_paths[1]):
                print("mysql and mongoDB installed")
            else:
                print("installing mysql and mongoDB")
                await install_mysql_win() # [√, √]
                await install_mongo_win(install_paths[1]) # [√, √]

        else:
            print("Chocolatey is not installed.")
            await install_choco_win() # [√, √]
            set_up_enviroment() 

    else:
        print("Unkown or unsupported os")
        time.sleep(1000)


async def runMain():
    panel_worker =  Worker(target_func=run_panel)
    api_worker   =  Worker(target_func=run_panel_api)
    try:
        await dns_server.run().join()
        await panel_worker.run().join()
        await api_worker.run().join()

    except KeyboardInterrupt:
        await dns_server.stop()
        await panel_worker.stop()
        await api_worker.stop()

    except Exception as e:
        await dns_server.stop()
        await panel_worker.stop()
        await api_worker.stop()
        
        print(f"error: {str(e)}")
        create_and_write_to_file(
            "./bin/log/", 
            f"error log - {get_current_date_with_full_month()} - {get_current_time_12()}.log",
            f"error running app: {str(e)}"
        )

async def main():
    await asyncio.gather(
        set_up_enviroment(),
        runMain()
    )


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except Exception as e:
        print(f"error: {str(e)}")
        create_and_write_to_file(
            "./bin/log/", 
            f"error log - {get_current_date_with_full_month()} - {get_current_time_12()}.log",
            f"error main: {str(e)}"
        )
