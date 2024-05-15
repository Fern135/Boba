package api

import (
	"fmt"
	"net/http"
)

/*
	api for handling the front end work.
*/

func SetUpApi() {
	println("Set up api before running. should run only once")
}

func Start() {
	fmt.Println("Server starting at :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println(err)
	}
}
