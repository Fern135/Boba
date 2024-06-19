package php

import (
	"boba/src/api/controllers/php"
	"net/http"
)

var urls = []string{
	"/",                // 0 [√]
	"/create-project/", // 1 [√] -> connecting domain and db config,
	"/read-project",    // 2 []
	"/read-projects",   // 3 []
	"/update-projects", // 4 [] updating db, php config files,
}

// todo: figure out how to make this work in terms of controller.
// todo: CRUD (create, read, update and delete)
func PhpRoutes() {
	go func() {
		http.HandleFunc(urls[0], php.Home)
		http.HandleFunc(urls[1], php.CreateProject)

	}()
}
