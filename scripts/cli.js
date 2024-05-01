const readline = require('readline');
const { exec } = require('child_process');

/*
  todo: replace in deploy if it doesn't work with async.
  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    console.log(stdout);
    if (stderr) console.error(`stderr: ${stderr}`);
  });
*/

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function setUpEnv(){
  let command;
  switch (process.platform) {
  case 'win32':
        command = 'python ./setup/env.py';
    break;
    
    case 'darwin':
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
}

async function deploy(){
  let command;
  switch (process.platform) {
  case 'win32':
        command = 'python ./deploy/deploy.py';
    break;
    
    case 'darwin':
      case 'linux':
        command = 'python3 ./deploy/deploy.py';
    break;
  default:
    console.error(`Unsupported platform: ${process.platform}`);
    process.exit(1);
  }

  const { stdout, stderr } = await exec(command);
  console.log(stdout);
  if (stderr) console.error(`stderr: ${stderr}`);
}

const args = process.argv.slice(2);
if (args.includes('-env')) {
  setUpEnv();
} else if (args.includes('-d')) {
  deploy().catch(error => console.error(`Error: ${error}`));
} else {
  // Ask user for their name if no flag is provided
  rl.question('Enter your name: ', (name) => {
    // Call greet function with the provided name
    greet(name);
  
    // Close the readline interface
    rl.close();
  });
}