package dns

import (
	"fmt"
	"net/http"
)

// todo: figure out how to make this work in terms of controller. CRUD (create, read, update and delete)

func HomeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome to the home page!")
}

func AboutHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "This is the about page!")
}