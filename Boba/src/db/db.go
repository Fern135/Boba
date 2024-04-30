package db

import (
	"bufio"
	"database/sql"
	"fmt"
	"log"
	"os"
	"strings"
)

const filePath = "Boba.sql"

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

	commands, err := ReadSQLFile(filePath)
	if err != nil {
		fmt.Println("Error reading SQL file:", err) // todo: use LoggerErr from util
		return err
	}

	// Process each SQL command
	for _, cmd := range commands {
		fmt.Println("Executing SQL command:", cmd) // todo: delete in production

		_, err = db.Exec(cmd) // run sql commands. once
	}

	// todo: delete if top works
	// _, err = db.Exec(`
	// 	CREATE TABLE IF NOT EXISTS users (
	// 		id INTEGER PRIMARY KEY,
	// 		name TEXT,
	// 		email TEXT
	// 	)
	// `)

	if err != nil {
		return err // todo: use LoggerErr from util
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
	rows, err := db.Query("SELECT * FROM users")
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

func ReadSQLFile(filePath string) ([]string, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var commands []string
	var currentCommand strings.Builder

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		line = strings.TrimSpace(line)
		if line == "" {
			continue // Skip empty lines
		}

		if strings.HasSuffix(line, ";") {
			// Append the line to the current command
			currentCommand.WriteString(line)
			commands = append(commands, currentCommand.String())

			// Reset the current command
			currentCommand.Reset()
		} else {
			// Append the line to the current command
			currentCommand.WriteString(line)
			currentCommand.WriteString(" ")
		}
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return commands, nil
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
