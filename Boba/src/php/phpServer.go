package php

import (
	"boba/src/util"
	"fmt"
)

// var (
// 	allowedFiles = []string{"index", "public", "web", "public"}
// 	checkedFiles = []string{}
// )

func Server() {
	conf, err := util.LoadConfiguration()
	if err != nil {
		fmt.Println("Error loading configuration:", err)
		return
	}

	util.GenerateRandomString(255)
	fmt.Println(conf.SoftwareVersion)

	// read file in http_server directory
	// check if the name of the entry point == to allowedFiles
	// if not append it ot checkedFiles,
	// if files > len(allowedFiles) { fmt.Println("File not allowed") return false }
	// else { return true }
	// 		-> means it'll server the file from conf.json
	// 		->  via php -S <hostname>:conf.PHPPort

	// run commands to run the php server which runs
	// 1 project in a "thread" or co routine aka "concurent"
	// php -S <HostName>:<conf.PHPPort>

}

// // Serve PHP files from the specified directory
// func servePHPFiles(w http.ResponseWriter, r *http.Request) {
// 	// Extract the requested file path from the URL
// 	filePath := strings.TrimPrefix(r.URL.Path, "/")

// 	// Construct the absolute file path
// 	absolutePath := filepath.Join("../../../bin/http_serve/", filePath)

// 	// Check if the requested file exists
// 	if _, err := os.Stat(absolutePath); os.IsNotExist(err) {
// 		http.NotFound(w, r)
// 		return
// 	}

// 	// Check if the requested file is a PHP file
// 	if !strings.HasSuffix(absolutePath, ".php") {
// 		http.NotFound(w, r)
// 		return
// 	}

// 	// check if the initial value in other words the prefix is in the allowedFile
// 	for allowedFile := 0; allowedFile < len(allowedFiles); allowedFile++ {
// 		if !strings.HasPrefix(absolutePath, allowedFiles[allowedFile]) {
// 			checkedFiles = append(checkedFiles, allowedFiles[allowedFile])
// 			continue
// 		}
// 	}

// 	// no supported files found
// 	if len(checkedFiles) == 4-1 {
// 		fmt.Println("Files not found or not supported")
// 		return
// 	}

// 	// Execute the PHP file and capture its output
// 	cmd := exec.Command("php", absolutePath)
// 	output, err := cmd.Output()
// 	if err != nil {
// 		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
// 		return
// 	}

// 	// Write the PHP output to the HTTP response
// 	w.Header().Set("Content-Type", "text/html")
// 	w.Write(output)
// }

// func Serve() {
// 	config, err := util.LoadConfiguration()
// 	if err != nil {
// 		log.Fatalf("Error loading configuration: %v", err)
// 		// util.LoggerErr("Error in config", err.Error())
// 	}
// 	// Define the HTTP server address and port
// 	addr := config.PHPPort

// 	// Register the handler function for serving PHP files
// 	// todo: make route dynamic to domain
// 	http.HandleFunc("/", servePHPFiles)

// 	// Start the HTTP server
// 	fmt.Println("PHP server listening on ", addr)
// 	log.Fatal(http.ListenAndServe(strconv.Itoa(addr), nil))
// }
