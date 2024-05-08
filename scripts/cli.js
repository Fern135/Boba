const readline = require('readline');
const { exec } = require('child_process');

const help = `
  commands\n\t
    -env:\tWrite env variable data to .env file in directory.\n
    -d:\tDeploy application on the landing page (not working yet.)\n
    -upgrade:\tUpgrade conf.json with latest go, php, python, node and npm version\n
`;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function setUpEnv(){
  try{
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
  }catch(error){
    console.log(`error in setting up env\nerror: ${error.toString()}`);
  }
}

function deploy(){
  try{
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

    exec(command, (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error}`);
        return;
      }
      console.log(stdout);
      if (stderr) console.error(`stderr: ${stderr}`);
    });
  }catch(error){
    console.log(`error in deploying app\nerror: ${error.toString()}`);
  }
}

function update(){
  try{
    let command;
    switch (process.platform) {
      case 'win32':
        command = 'python ./update/update.py';
        break;
    case 'darwin':
    case 'linux':
        command = 'python3 ./update/update.py';
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

const args = process.argv.slice(2);
if (args.includes('-env')) {
  setUpEnv();
} 
else if (args.includes('-d')) {
  deploy();
} 
else if(args.includes('-upgrade')){
  update();
}

else {
  console.log(help);
}