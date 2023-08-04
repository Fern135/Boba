import os
from lib.util.util import read_json_file, run_terminal_command

class PHP:
    def __init__(self):
        self.version    = read_json_file("../../bin/conf/conf.json", "php-version")
        self.php_folder = read_json_file("../../bin/conf/conf.json", "projects-path")
        self.php_file   = ""

    def set_Php_File(self, php_file):
        self.php_file = php_file

    def run_php_file(self):
        try:
            if not os.path.exists(self.php_file):
                raise FileNotFoundError(f"PHP file '{self.php_file}' not found")

            command = f"php{self.version} {self.php_file}"
            run_terminal_command(command)

        except Exception as e:
            print(f"Error: {e}")