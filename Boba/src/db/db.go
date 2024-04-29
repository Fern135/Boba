package db

import (
	"database/sql"
	"fmt"
	"log"
)

var db *sql.DB

// todo: make an sql regarding the structure of the program. make it load from a file
//  and then use that to create the database, tables etc...

// InitDB initializes the SQLite database and sets the global db variable.
func InitDB() error {
	// Open the SQLite database file
	dbFile := "mydatabase.db"
	conn, err := sql.Open("sqlite3", dbFile)
	if err != nil {
		return err
	}

	// Assign the database connection to the global db variable
	db = conn

	// Create tables if they don't exist
	_, err = db.Exec(`
		CREATE TABLE IF NOT EXISTS users (
			id INTEGER PRIMARY KEY,
			name TEXT,
			email TEXT
		)
	`)
	if err != nil {
		return err
	}

	return nil
}

// InsertUser inserts a new user into the users table.
func InsertUser(name, email string) error {
	_, err := db.Exec("INSERT INTO users (name, email) VALUES (?, ?)", name, email)
	return err
}

// QueryUsers retrieves all users from the users table and prints them.
func QueryUsers() error {
	rows, err := db.Query("SELECT id, name, email FROM users")
	if err != nil {
		return err
	}
	defer rows.Close()

	for rows.Next() {
		var id int
		var name, email string
		err = rows.Scan(&id, &name, &email)
		if err != nil {
			return err
		}
		fmt.Printf("ID: %d, Name: %s, Email: %s\n", id, name, email)
	}

	return nil
}

func usage() {
	// Initialize the SQLite database
	err := InitDB()
	if err != nil {
		log.Fatal("Error initializing database:", err)
	}

	// Insert some sample data
	err = InsertUser("Alice", "alice@example.com")
	if err != nil {
		log.Fatal("Error inserting user:", err)
	}

	err = InsertUser("Bob", "bob@example.com")
	if err != nil {
		log.Fatal("Error inserting user:", err)
	}

	// Query and print all users
	err = QueryUsers()
	if err != nil {
		log.Fatal("Error querying users:", err)
	}
}
