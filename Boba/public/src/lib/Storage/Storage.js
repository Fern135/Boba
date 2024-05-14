export default class StorageManager {
    constructor(storageType = 'local') {
      this.storageType = storageType;
    }
  
    getItem(key, defaultValue) {
      if (this.storageType === 'local' || this.storageType === 'session') {
        const storage = this.getStorage();
        const storedValue = storage.getItem(key);
        return storedValue !== null ? JSON.parse(storedValue) : defaultValue;
      } else if (this.storageType === 'cookie') {
        return this.getCookie(key) || defaultValue;
      } else {
        throw new Error('Invalid storage type');
      }
    }
  
    setItem(key, value) {
      if (this.storageType === 'local' || this.storageType === 'session') {
        const storage = this.getStorage();
        const serializedValue = JSON.stringify(value);
        storage.setItem(key, serializedValue);
      } else if (this.storageType === 'cookie') {
        this.setCookie(key, value);
      } else {
        throw new Error('Invalid storage type');
      }
    }
  
    getStorage() {
      if (this.storageType === 'local') {
        return localStorage;
      } else if (this.storageType === 'session') {
        return sessionStorage;
      } else {
        throw new Error('Invalid storage type');
      }
    }
  
    getCookie(key) {
      const name = key + '=';
      const decodedCookie = decodeURIComponent(document.cookie);
      const cookieArray = decodedCookie.split(';');
      for (let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i];
        while (cookie.charAt(0) === ' ') {
          cookie = cookie.substring(1);
        }
        if (cookie.indexOf(name) === 0) {
          return cookie.substring(name.length, cookie.length);
        }
      }
      return null;
    }
  
    setCookie(key, value, days = 365) {
      const expires = new Date();
      expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
      const cookieValue = encodeURIComponent(value) + '; expires=' + expires.toUTCString();
      document.cookie = key + '=' + cookieValue;
    }
}


// Instantiate the StorageManager with the desired storage type
const storageManager = new StorageManager('local');

// Example usage for local storage
storageManager.setItem('key1', 'value1');
const value1 = storageManager.getItem('key1', 'defaultValue1');
console.log(value1); // Output: 'value1'

// Example usage for session storage
storageManager.storageType = 'session';
storageManager.setItem('key2', 'value2');
const value2 = storageManager.getItem('key2', 'defaultValue2');
console.log(value2); // Output: 'value2'

// Example usage for cookies
storageManager.storageType = 'cookie';
storageManager.setItem('key3', 'value3');
const value3 = storageManager.getItem('key3', 'defaultValue3');
console.log(value3); // Output: 'value3'
