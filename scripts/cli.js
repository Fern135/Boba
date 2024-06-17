const { exec } = require('child_process');


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
