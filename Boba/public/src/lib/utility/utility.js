export default class Utility{
    
    constructor(){
        this.emRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        this.characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890~`!@#$%^&*()_+=-[]|{};"",./?><';
    }

    /**
     * 
     * @param {*} length 
     * @returns alphanumeric string of length 
     */
    generateRandomString(length) {
        let result = '';
        for (let i = 0; i < length; i++) {
          const randomIndex = Math.floor(Math.random() * this.characters.length);
          result += this.characters.charAt(randomIndex);
        }
        return result;
    }

    /**
     * 
     * @returns Promise<{ browserName: string; ipAddress: any; latitude: undefined; longitude: undefined; }>
     */
    async getDeviceInfo() {
        const browserName = window.navigator;
        let ipAddress;
        let latitude;
        let longitude;
      
        // Get the IP address using a public API
        try {
          const response = await fetch('https://api.ipify.org?format=json');
          const ipData   = await response.json();
          ipAddress = ipData.ip;
        } catch (error) {
          console.error('Error fetching IP address:', error);
        }
      
        // Get the location coordinates using the Geolocation API
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(
            (position) => {
              latitude = position.coords.latitude;
              longitude = position.coords.longitude;
            },
            (error) => {
              console.error('Error getting location:', error);
            }
          );
        }
      
        // Return an object containing the collected information
        return {
            browserName,
            ipAddress,
            latitude,
            longitude,
        };
    }
      
      

    /**
     * 
     * @param {miliseconds} ms 
     * @returns 
     */
    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    /**
     * 
     * @param {email being tested} email 
     * @returns boolean
     */
    isValidEmail(email){
        return this.emRegex.test(email);
    }

    /**
     * 
     * @param {*} value 
     * @returns  true if the value is Int
     */
    isInt(value) {
        return Number.isInteger(value);
    }
  
    /**
     * 
     * @param {*} value 
     * @returns  true if the value is a Float
     */
    isFloat(value) {
        return Number.isFinite(value) && !Number.isInteger(value);
    }
  
    /**
     * 
     * @param {*} value 
     * @returns  true if the value is a String
     */
    isString(value) {
        return typeof value === 'string' || value instanceof String;
    }
  
    /**
     * 
     * @param {*} value 
     * @returns True if value is Json
     */
    isJson(value) {
        try {
            JSON.parse(value);
            return true;
        } catch (error) {
            return false;
        }
    }
  
    /**
     * 
     * @param {*} value 
     * @returns True if value is object
     */
    isObject(value) {
        return value && typeof value === 'object' && value.constructor === Object;
    }
    
    /**
     * 
     * @param {*} value 
     * @returns True  if value is an Array
     */
    isArray(value) {
        return Array.isArray(value);
    }
    
    /**
     * 
     * @param {*} value 
     * @returns value as int
     */
    toInt(value) {
        return parseInt(value, 10);
    }
    
    /**
     * 
     * @param {*} value 
     * @returns value as float
     */
    toFloat(value) {
        return parseFloat(value);
    }
    
    /**
     * 
     * @param {*} value 
     * @returns value as string
     */
    toString(value) {
        return String(value);
    }
    
    /**
     * 
     * @param {*} value 
     * @returns value as json
     */
    toJson(value) {
        return JSON.stringify(value);
    }
    
    /**
     * 
     * @param {*} value 
     * @returns value as object
     */
    toObject(value) {
        return JSON.parse(value);
    }
    
    /**
     * 
     * @param {*} value 
     * @returns value as array
     */
    toArray(value) {
        if (this.isArray(value)) {
            return value;
        }
        return [value];
    }
}