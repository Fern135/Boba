package php

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"
)

// todo: figure out how to make this work in terms of controller.
// CRUD (create, read, update and delete)
func Home(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome to the home page!")
}

func CreateProject(w http.ResponseWriter, r *http.Request) {
	// {
	// 	"project_domain" : "could be null or provided",
	// 	"project_name" 	 : "required -> get file name if empty",
	// 	"is_php" 		 : "bool",
	// 	"framework" 	 : "ScarpaPHP, laravel or custom",
	// 	"db_type" 		 : "mysql, mariadb, sqlite, or custom",
	// 	"db_host" 		 : "localhost",
	// 	"db_port" 		 : "default config, user can use their own.",
	// 	"db_username" 	 : "root",
	// 	"db_password" 	 : "password",
	// 	"db_name" 		 : "required",
	// }
	fmt.Fprintf(w, "This is the about page!")
}

func DeleteHandler(w http.ResponseWriter, r *http.Request) {
	// Extract the project_id from the URL
	path := r.URL.Path
	parts := strings.Split(path, "/")

	if len(parts) < 3 {
		http.Error(w, "Project ID not provided", http.StatusBadRequest)
		return
	}

	// the url parameter for projectID
	projectID := parts[2]

	// Check if the projectID is an integer or string
	if _, err := strconv.Atoi(projectID); err == nil {
		// projectID is an integer
		fmt.Fprintf(w, "Project ID to delete (int): %s", projectID)
	} else {
		// projectID is a string
		fmt.Fprintf(w, "Project ID to delete (string): %s", projectID)
	}

	// Perform the delete operation
	// (Here we just print the projectID for demonstration purposes)
	fmt.Println("Project ID to delete:", projectID)
}
