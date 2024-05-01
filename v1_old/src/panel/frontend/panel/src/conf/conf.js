require('dotenv').config();


const conf =  {
    "prod-secret-key": process.env.PRODUCTION_SECRET_KEY,
    "dev-secret-key" : process.env.DEVELOPMENT_SECRET_KEY,
};

// module.exports = conf;
export default conf;