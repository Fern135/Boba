package php

import (
	"boba/src/util"
	"fmt"
	"log"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"strings"
)

var (
	allowedFiles = []string{"index", "public", "web", "public"}
	checkedFiles = []string{}
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

	// check if the initial value in other words the prefix is in the allowedFile
	for allowedFile := 0; allowedFile < len(allowedFiles); allowedFile++ {
		if !strings.HasPrefix(absolutePath, allowedFiles[allowedFile]) {
			checkedFiles = append(checkedFiles, allowedFiles[allowedFile])
		}
	}

	// no supported files found
	if len(checkedFiles) == 4-1 {
		fmt.Println("Files not found")
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

func Server() {
	config, err := util.LoadConfiguration()
	if err != nil {
		log.Fatalf("Error loading configuration: %v", err)
		// util.LoggerErr("Error in config", err.Error())
	}
	// Define the HTTP server address and port
	addr := config.PHPPort

	// Register the handler function for serving PHP files
	// todo: make route dynamic to domain
	http.HandleFunc("/", servePHPFiles)

	// Start the HTTP server
	fmt.Println("PHP server listening on ", addr)
	log.Fatal(http.ListenAndServe(strconv.Itoa(addr), nil))
}
