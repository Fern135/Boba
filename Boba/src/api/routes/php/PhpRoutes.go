package php

import (
	"boba/src/api/controllers/php"
	"net/http"
)

// todo: figure out how to make this work in terms of controller.
// todo: CRUD (create, read, update and delete)
func PhpRoutes() {
	http.HandleFunc("/", php.HomeHandler)
	http.HandleFunc("/about", php.AboutHandler)
}
