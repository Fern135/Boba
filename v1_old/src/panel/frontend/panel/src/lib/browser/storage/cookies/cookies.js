export default class CookieHandler {
    // Set a cookie with the specified name, value, and optional options
    static setCookie(name, value, options = {}) {
        const { expires, path, domain, secure } = options;
        let cookie = encodeURIComponent(name) + '=' + encodeURIComponent(value);

        if (expires instanceof Date) {
            cookie += '; expires=' + expires.toUTCString();
        }

        if (path) {
            cookie += '; path=' + path;
        }

        if (domain) {
            cookie += '; domain=' + domain;
        }

        if (secure) {
            cookie += '; secure';
        }

        document.cookie = cookie;
    }

    // Get the value of a cookie by its name
    static getCookie(name) {
        const decodedName = decodeURIComponent(name);
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(decodedName + '=')) {
                return decodeURIComponent(cookie.substring(decodedName.length + 1));
            }
        }
        return null;
    }

    // Delete a cookie by its name
    static deleteCookie(name) {
        this.setCookie(name, '', { expires: new Date(0) });
    }
}

// Example usage:

// CookieHandler.setCookie('preferences', 'enabled', {
//     expires: new Date('2023-12-31'),
//     path: '/',
//     domain: 'mywebsite.com',
//     secure: true
// });

// Set a cookie with a name, value, and optional options
// CookieHandler.setCookie('username', 'John Doe', { expires: new Date('2023-12-31') });

// Get the value of a cookie by its name
// const username = CookieHandler.getCookie('username');
// console.log(username);  // Output: "John Doe"

// Delete a cookie by its name
// CookieHandler.deleteCookie('username');
