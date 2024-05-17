package dns

import (
	"boba/src/api/controllers/dns"
	"net/http"
)

// todo: figure out how to make this work in terms of controller. CRUD (create, read, update and delete)
func ConfigRoutes() {
	http.HandleFunc("/", dns.HomeHandler)
	http.HandleFunc("/about", dns.AboutHandler)
}
