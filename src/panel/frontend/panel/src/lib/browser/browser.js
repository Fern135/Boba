
function getBrowserName() {
    const userAgent = navigator.userAgent;
    if (userAgent.includes("Chrome")) return "Chrome";
    if (userAgent.includes("Firefox")) return "Firefox";
    if (userAgent.includes("Safari")) return "Safari";
    // Add more browser checks as needed
    return "Unknown";
}

function getBrowserVersion() {
    const userAgent = navigator.userAgent;
    const browserName = this.getBrowserName();
    const startIndex = userAgent.indexOf(browserName) + browserName.length + 1;
    const endIndex = userAgent.indexOf(" ", startIndex);
    return userAgent.substring(startIndex, endIndex);
}

function isMobileDevice() {
    return /Mobi|Android|iPhone|iPad|iPod|Windows Phone/i.test(navigator.userAgent);
}

function getScreenWidth() {
    return window.screen.width;
}

function getScreenHeight() {
    return window.screen.height;
}

function getCurrentUrl() {
    return window.location.href;
}

function getDocumentTitle() {
    return document.title;
}

function isOnline() {
    return navigator.onLine;
}

function getLanguage() {
    return navigator.language;
}

module.exports = {
    getBrowserName,
    getBrowserVersion,
    isMobileDevice,
    getScreenWidth,
    getScreenHeight,
    getCurrentUrl,
    getDocumentTitle,
    isOnline,
    getLanguage,
};


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
