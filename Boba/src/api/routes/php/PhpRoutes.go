package php

import (
	"boba/src/api/controllers/php"
	"net/http"
)

var phpConfigUrls = []string{
	"/",                             // 0 [√]
	"/create-project/",              // 1 [√] -> connecting domain and db config,
	"/projects/PHP/read-project/",   // 2 [] -> projectID at the end
	"/projects/PHP/read-projects/",  // 3 []
	"/projects/PHP/update-project/", // 4 [] -> db, php config files, projectID at the end
	"/projects/PHP/delete-project/", // 5 [] -> projectID at the end
}

// todo: figure out how to make this work in terms of controller.
// todo: CRUD (create, read, update and delete)
func PhpRoutes() {
	go func() {
		http.HandleFunc(phpConfigUrls[0], php.Home)
		http.HandleFunc(phpConfigUrls[1], php.CreateProject)

	}()
}
