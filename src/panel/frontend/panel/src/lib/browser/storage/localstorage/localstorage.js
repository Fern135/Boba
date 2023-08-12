import CryptoJS from 'crypto-js';

import conf from '../../../../conf/conf';

export default class LocalStorageHandler {

    constructor(){
        this.secretKey = conf['dev-secret-key'];
        // this.secretKey = conf['prod-secret-key'];

        this.encoding = CryptoJS.enc.Utf8;
    }

    // Set a value in local storage with encryption
    static setItem(key, value) {
        try {
            const encryptedValue = CryptoJS.AES.encrypt(JSON.stringify(value), this.secretKey).toString(this.encoding);
            localStorage.setItem(key, encryptedValue);
        } catch (error) {
            console.error(`Error setting encrypted local storage item: ${error}`);
        }
    }

    // Get a value from local storage by key with decryption
    static getItem(key) {
        try {
            const encryptedValue = localStorage.getItem(key);
            if (encryptedValue) {
                const decryptedValue = CryptoJS.AES.decrypt(encryptedValue, this.secretKey).toString(this.encoding);
                return JSON.parse(decryptedValue);
            }
            return null;
        } catch (error) {
            console.error(`Error getting encrypted local storage item: ${error}`);
            return null;
        }
    }

    // Remove an item from local storage by key
    static removeItem(key) {
        try {
            localStorage.removeItem(key);
        } catch (error) {
            console.error("Error removing local storage item:", error);
        }
    }

    // Clear all items from local storage
    static clear() {
        try {
            localStorage.clear();
        } catch (error) {
            console.error("Error clearing local storage:", error);
        }
    }
}


/* 
    example usage:
    Import the LocalStorageHandler class
    import LocalStorageHandler from './LocalStorageHandler';

    Set a value in local storage with encryption
    const secretKey = 'my-secret-key';
    LocalStorageHandler.setItem('username', 'john_doe', secretKey);

    Get a value from local storage by key with decryption
    const storedUsername = LocalStorageHandler.getItem('username', secretKey);
    console.log('Stored Username:', storedUsername);

*/