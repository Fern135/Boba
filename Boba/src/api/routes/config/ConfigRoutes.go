package config

import (
	"boba/src/api/controllers/config"
	"net/http"
)

// todo: figure out how to make this work in terms of controller.
// todo: CRUD (create, read, update and delete)
func ConfigRoutes() {
	http.HandleFunc("/", config.HomeHandler)
	http.HandleFunc("/about", config.AboutHandler)
}
