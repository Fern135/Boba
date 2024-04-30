package php

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
)

// Serve PHP files from the specified directory
func servePHPFiles(w http.ResponseWriter, r *http.Request) {
	// Extract the requested file path from the URL
	filePath := strings.TrimPrefix(r.URL.Path, "/")

	// Construct the absolute file path
	absolutePath := filepath.Join("../../../bin/http_serve/", filePath)

	// Check if the requested file exists
	if _, err := os.Stat(absolutePath); os.IsNotExist(err) {
		http.NotFound(w, r)
		return
	}

	// Check if the requested file is a PHP file
	if !strings.HasSuffix(absolutePath, ".php") {
		http.NotFound(w, r)
		return
	}

	// Execute the PHP file and capture its output
	cmd := exec.Command("php", absolutePath)
	output, err := cmd.Output()
	if err != nil {
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	// Write the PHP output to the HTTP response
	w.Header().Set("Content-Type", "text/html")
	w.Write(output)
}

func server() {
	// Define the HTTP server address and port
	addr := ":8080"

	// Register the handler function for serving PHP files
	http.HandleFunc("/", servePHPFiles)

	// Start the HTTP server
	fmt.Printf("PHP server listening on %s\n", addr)
	log.Fatal(http.ListenAndServe(addr, nil))
}
