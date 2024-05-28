package main

import (
	"boba/src/util"
	"fmt"
	"log"
)

const (
	conf  = "../bin/conf/conf.json"
	env   = "../.env"
	panel = "" // todo: add panel directory once it's working.
)

var (
	ENV                 = util.GetEnv(env)
	config, configError = util.LoadConfiguration()
)

// Access configuration values using nested keys
// phpVersion := conf.LanguageVersions.PHPVersion[0]
// fmt.Println("PHP Version:", phpVersion)

// Accessing nested arrays or objects
// firstDomain := conf.Domains[0]
// fmt.Println("First Domain:", firstDomain.Domain)

func main() {
	if configError != nil {
		log.Fatalf("Error loading configuration: %v", configError)
		// util.LoggerErr("Error in config", err.Error())
	}

	if ENV["debugging"] == true {
		loadMessages()
		defer runApp()
	} else {
		runApp()
	}
}

// installing languages and more.
func runApp() {
	// go func() {  }()

	//#region install packages and databases needed
	util.InstallPackages()
	// util.ProgressBar(util.InstallPackages()) // loading bar based on how long packages take

	util.InstallDatabases()
	// util.ProgressBar(util.InstallDatabases()) // loading bar based on how long database take
	//#endregion

	// setting up api
	// api.SetUpApi()
	// api.ApiStart()
}

func goVersions() {
	switch util.GetPcDevOs() {
	case "Linux":
		fmt.Println("Go Version\t\t", config.LanguageVersions.GoVersion[0])
	case "Mac":
		fmt.Println("Go Version\t\t", config.LanguageVersions.GoVersion[1])
	case "Windows":
		fmt.Println("Go Version\t\t", config.LanguageVersions.GoVersion[2])
	}
}

func loadMessages() {
	fmt.Println("App version 	 \t", config.SoftwareVersion)
	goVersions()
	fmt.Println("Php Version 	 \t", config.LanguageVersions.PHPVersion)
	fmt.Println("Python Version  \t", config.LanguageVersions.PythonVersion)
	fmt.Println("Node.js Version \t", config.LanguageVersions.NodeVersion)
	fmt.Println("NPM Version 	 \t", config.LanguageVersions.NPMVersion)
}
