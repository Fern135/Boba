const CHARACTERS = [
    ...'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    ...'0123456789',
    ...'abcdefghijklmnopqrstuvwxyz',
    ...'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~',
];



// useful utilities
function readJsonFile(file_path, key) {
    try {
        const data = require(file_path);
        if (data !== null) {
        return data[key] !== undefined ? data[key] : null;
        }
    } catch (error) {
        console.error(`Error reading JSON file: ${file_path}`);
        return null;
    }
}

function modifyJsonValue(file_path, key, new_value) {
    try {
        const data = require(file_path);
        data[key] = new_value;

        const fs = require('fs');
        fs.writeFileSync(file_path, JSON.stringify(data, null, 4));
    } catch (error) {
        console.error(`Error modifying JSON value: ${file_path}`);
    }
}

function generateRandomAlphanumericString(length) {
    let random_string = '';
    for (let i = 0; i < length; i++) {
        const random_index = Math.floor(Math.random() * CHARACTERS.length);
        random_string += CHARACTERS[random_index];
    }
    return random_string;
}


// basic utilities
function rnd(max) {
    return Math.floor(Math.random() * max) + 1;
}

function rndBetween(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getPcDevOs() {
    return process.platform;
}

function sort(arr) {
    return [...arr].sort((a, b) => a - b);
}

function search(search, arr) {
    return arr.includes(search);
}


module.exports = {
    readJsonFile,
    modifyJsonValue,
    generateRandomAlphanumericString,
    rnd,
    rndBetween,
    getPcDevOs,
    sort,
    search,
};