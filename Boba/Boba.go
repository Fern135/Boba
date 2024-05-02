package main

import (
	"boba/src/util"
	"fmt"
	"log"
)

const (
	conf  = "../bin/conf/conf.json"
	panel = "" // todo: add panel directory once it's working.
)

var ENV = util.GetEnv()

// Access configuration values using nested keys
// phpVersion := conf.LanguageVersions.PHPVersion[0]
// fmt.Println("PHP Version:", phpVersion)

// Accessing nested arrays or objects
// firstDomain := conf.Domains[0]
// fmt.Println("First Domain:", firstDomain.Domain)

func main() {
	if ENV["debugging"] == true {
		defer loadMessages()
	} else {
		runApp()
	}
}

// installing languages and more.
func runApp() {
	go func() {
		util.InstallPackages()
		util.InstallDatabases()
	}()
}

func loadMessages() {
	config, err := util.LoadConfiguration(conf)
	if err != nil {
		log.Fatalf("Error loading configuration: %v", err)
		// util.LoggerErr("Error in config", err.Error())
	}

	fmt.Println("App version 	 \t", config.SoftwareVersion)
	fmt.Println("Php Version 	 \t", config.LanguageVersions.PHPVersion)
	fmt.Println("Python Version  \t", config.LanguageVersions.PythonVersion)
	fmt.Println("Node.js Version \t", config.LanguageVersions.NodeVersion)
	fmt.Println("NPM Version 	 \t", config.LanguageVersions.NPMVersion)

}
