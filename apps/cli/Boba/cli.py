import os
import datetime
import click
import time
import asyncio


from lib.util.util           import create_and_write_to_file, read_json_file, getPcDevOs
from lib.datetime.dt         import get_current_date_with_full_month, get_current_time_12
from src.tests.test_all      import *

is_dev = read_json_file("./bin/conf/conf.json", "development")
__default_project_path__ = read_json_file("./bin/conf/conf.json", "projects-path")

#TODO: More testing or just scrap
def generate_basic_php_project(project_name):
    directory   = __default_project_path__
    project_dir = directory + project_name

    css_files = project_dir + "/bin/css/"
    js_files  = project_dir + "/bin/js/"

    inc_files = project_dir + "/bin/inc/"

    exists = not os.path.exists(project_dir) and not os.path.exists(css_files) and not os.path.exists(js_files) and not os.path.exists(inc_files)

    if exists:
        os.mkdir(project_dir)
        os.mkdir(css_files)
        os.mkdir(js_files)
        os.mkdir(inc_files)

    # os.chdir(project_dir)

    os.chdir(project_dir)
    # Create the main PHP file.
    file_name = "index.php"
    php_code = f"""<?php

        ?>
        <!DOCTYPE html>
        <html>
        <head>
        <title>{project_name}</title>

        </head>
        <body>
            <h1>
                <?php echo 'first php project'; ?>
            </h1>
        </body>
        </html>

    """
    with open(file_name, "w") as file:
        file.write(php_code)
        # file.write("echo \"Hello, world!\";\n")

    # writing basic .inc database file
    os.chdir(inc_files)
    db_file_name = "database.inc.php"
    db_code = """
        <?php

        class Database
        {
            private $connection;

            public function __construct()
            {
                $this->connection = new mysqli("localhost", "root", "", "my_database");
            }

            public function startTransaction()
            {
                $this->connection->beginTransaction();
            }

            public function commitTransaction()
            {
                $this->connection->commit();
            }

            public function rollbackTransaction()
            {
                $this->connection->rollBack();
            }

            public function query($sql)
            {
                $statement = $this->connection->prepare($sql);
                $statement->execute();
                return $statement->fetchAll();
            }

            public function insert($table, $data)
            {
                $sql = "INSERT INTO $table (";
                foreach ($data as $key => $value) {
                    $sql .= "$key, ";
                }
                $sql = rtrim($sql, ", ");
                $sql .= ") VALUES (";
                foreach ($data as $value) {
                    $sql .= "'" . $this->escape($value) . "', ";
                }
                $sql = rtrim($sql, ", ");
                $sql .= ")";

                $statement = $this->connection->prepare($sql);
                foreach ($data as $key => $value) {
                    $statement->bindParam(":$key", $value);
                }
                $statement->execute();
            }

            public function update($table, $data, $where)
            {
                $sql = "UPDATE $table SET ";
                foreach ($data as $key => $value) {
                    $sql .= "$key='" . $this->escape($value) . "', ";
                }
                $sql = rtrim($sql, ", ");
                $sql .= " WHERE $where";

                $statement = $this->connection->prepare($sql);
                foreach ($data as $key => $value) {
                    $statement->bindParam(":$key", $value);
                }
                $statement->execute();
            }

            public function delete($table, $where)
            {
                $sql = "DELETE FROM $table WHERE $where";
                $statement = $this->connection->prepare($sql);
                $statement->execute();
            }

            private function escape($value)
            {
                return mysqli_real_escape_string($this->connection, $value);
            }
        }
    """
    with open(db_file_name, "w") as file:
        file.write(db_code)

    # Create the CSS file.
    os.chdir(css_files)
    file_name = "style.css"
    with open(file_name, "w") as file:
        file.write("body {}\n")

    # Create the JS file.
    os.chdir(js_files)
    file_name = "script.js"
    with open(file_name, "w") as file:
        file.write("console.log('Hello, javascript');\n")


    os.chdir("../../../../") # go back out to the default dir path

@click.group()
async def cli():
    pass

@cli.command()
@click.option('--date', '-d', is_flag=True, help='Return the current date')
def date(date):
    if date:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        click.echo(f'Current date and time: {current_date}')
        

@cli.command()
@click.option("--os", "-os", is_flag=True, help='Return the working operating system')
def get_ps_os(os):
    if os:
        print(f"\npc operating system: {getPcDevOs()}\n")

if __name__ == "__main__":
    try:
        cli() 

    except Exception as e:
        print(f"error cli: {str(e)}")
        create_and_write_to_file(
            "../../bin/log/", 
            f"error log - {get_current_date_with_full_month()} - {get_current_time_12()}.log",
            f"error cli: {str(e)}"
        )