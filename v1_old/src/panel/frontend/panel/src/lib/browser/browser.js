
export default class browser{

    static getBrowserName() {
        const userAgent = navigator.userAgent;
        if (userAgent.includes("Chrome"))  return "Chrome";
        if (userAgent.includes("Firefox")) return "Firefox";
        if (userAgent.includes("Safari"))  return "Safari";
        // Add more browser checks as needed
        return "Unknown";
    }

    static getBrowserVersion() {
        const userAgent     = navigator.userAgent;
        const browserName   = this.getBrowserName();
        const startIndex    = userAgent.indexOf(browserName) + browserName.length + 1;
        const endIndex      = userAgent.indexOf(" ", startIndex);

        return userAgent.substring(startIndex, endIndex);
    }

    // returns bool if current browser is mobile or not
    static isMobileDevice() {
        return /Mobi|Android|iPhone|iPad|iPod|Windows Phone/i.test(navigator.userAgent);
    }

    // returns number for the screen width
    static getScreenWidth() {
        return window.screen.width;
    }

    // returns number for the screen height
    static getScreenHeight() {
        return window.screen.height;
    }

    // gets the url for the current window
    static getCurrentUrl() {
        return window.location.href;
    }

    // returns the title of the document
    static getDocumentTitle() {
        return document.title;
    }

    // returns bool if the web browser is online.
    static isOnline() {
        return navigator.onLine;
    }

    static getLanguage() {
        return navigator.language;
    }

    // TODO: make it only show in debug mode
    static getFullDebugInfo(){
        return `
            browser debugging:\n
            name:           ${browser.getBrowserName()}\n
            version:        ${browser.getBrowserVersion()}\n
            url:            ${browser.getCurrentUrl()}\n
            title:          ${browser.getDocumentTitle()}\n
            is online:      ${browser.isOnline()}\n
            is mobile:      ${browser.isMobileDevice()}\n
            language:       ${browser.getLanguage()}\n
            screen width:   ${browser.getScreenWidth()}\n
            screen height:  ${browser.getScreenHeight()}\n
        `
    }
    
}


// Example usage
// console.log("Browser Name:", BrowserInfo.getBrowserName());
// console.log("Browser Version:", BrowserInfo.getBrowserVersion());
// console.log("Is Mobile Device:", BrowserInfo.isMobileDevice());
// console.log("Screen Width:", BrowserInfo.getScreenWidth());
// console.log("Screen Height:", BrowserInfo.getScreenHeight());
// console.log("Current URL:", BrowserInfo.getCurrentUrl());
// console.log("Document Title:", BrowserInfo.getDocumentTitle());
// console.log("Is Online:", BrowserInfo.isOnline());
// console.log("Preferred Language:", BrowserInfo.getLanguage());
