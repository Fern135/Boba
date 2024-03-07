export default class DateUtils {
    // Get the current date
    constructor() {
        this.date = new Date();
        this.weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        this.months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ];
    }

    // Get the current UTC date
    getCurrentUTCDate() {
        return new Date(Date.now());
    }

    // Format a date as a string (e.g., "2023-08-04")
    formatDate() {
        return this.date.toISOString().split("T")[0];
    }

    // Format a date and time as a string (e.g., "2023-08-04 10:30 AM")
    formatDateTime() {
        return this.date.toLocaleString();
    }

    // Get the year of a date
    getYear() {
        return this.date.getFullYear();
    }

    // Get the month of a date (0-11)
    getMonth() {
        return this.months[this.date.getMonth()];
    }

    // Get the day of the month (1-31)
    getDay() {
        return this.date.getDate();
    }

    // Get the day of the week (0-6 where 0 is Sunday)
    getDayOfWeek() {
        return this.weekday[this.date.getDay()];
    }

    // get the time in hour : minutes : seconds : miliseconds
    getTime(){
        return `${this.getHour()} : ${this.getMinutes()} : ${this.getSecond()} : ${this.getMilliseconds()}`;
    }

    // Get the hour of a date (0-23)
    #getHour() {
        return this.date.getHours();
    }

    // Get the minute of a date (0-59)
    #getMinute() {
        return this.date.getMinutes();
    }

    // Get the second of a date (0-59)
    #getSecond() {
        return this.date.getSeconds();
    }

    // Get the milliseconds of a date
    #getMilliseconds() {
        return this.date.getMilliseconds();
    }

    // Get the number of days in a specific month of a year (1-12)
    getDaysInMonth(year, month) {
        return new Date(year, month, 0).getDate();
    }

    // Check if a year is a leap year
    isLeapYear(year) {
        return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
    }

    // Get the difference in days between two dates
    getDaysDifference(date1, date2) {
        const timeDiff = Math.abs(date2 - date1);
        return Math.ceil(timeDiff / (1000 * 3600 * 24));
    }
}
