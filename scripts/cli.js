const { exec } = require('child_process');

// The first two elements are node and the script path, so we skip them
const args = process.argv.slice(2);

function env(){
  try{
    let command;
    switch (process.platform) {
      case 'win32':
        command = 'python ./setup/env.py';
        break;
    case 'darwin':
      command = 'python3 ./setup/env.py';
      break;
    case 'linux':
        command = 'python3 ./setup/env.py';
        break;
    default:
      console.error(`Unsupported platform: ${process.platform}`);
      process.exit(1);
    }
            
    exec(command, (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error}`);
        return;
      }
      console.log(stdout);
      if (stderr) console.error(`stderr: ${stderr}`);
    });
  }catch(error){
    console.log(`error in setting up env\nerror: ${error.toString()}`);
  }
}

async function deploy(){
  const deployUrl = process.env.DPURI;

  console.log("not working yet");

  return;
}

// Function to display help
function displayHelp() {
    console.log(`
      Usage: mycli <command> [options]

      Commands:
        -env       set up .env for this project
        -deploy    deploy the .exe or dmg to the static landing page

      Options:
        -h, --help         Display this help message
    `);
}

// Main function to process commands
function main() {
  const command = args[0];
  // const commandArgs = args.slice(1);
  if (args.length === 0 || args.includes('-h') || args.includes('--help')) {
      displayHelp();
      return;
  }

  switch (command) {
    case '-env':
        env();
      break;
    case '-deploy':
        deploy();
      break;
    default:
        console.log(`Unknown command: ${command}`);
        displayHelp();
      break;
  }
}

main();
