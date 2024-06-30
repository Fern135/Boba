package main

import (
	"boba/src/api"
	"boba/src/util"
	"fmt"
)

const (
	conf  = "../bin/conf/conf.json"
	env   = "../.env"
	panel = "./public/" // todo: add panel directory once it's working.
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
		// log.Fatalf("Error loading configuration: %v", configError)
		util.LoggerErr("Error in config", configError.Error())
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

	//#region install packages and databases needed
	util.InstallPackages()
	util.InstallDatabases()
	//#endregion

	defer func() {
		// installing and running the panel. should be fairly quick. in theory
		// go func() {}()
		if err := util.RunCommandInDir("npm install", panel); err != nil {
			fmt.Println("Error:", err)
		}

		if err := util.RunCommandInDir("npm start", panel); err != nil {
			fmt.Println("Error: ", err)
		}

		//******************** setting up api ********************
		go api.SetUpApi() // inits db. or at least it should :-/
		// api.ApiStart()
		//******************** setting up api ********************
	}()
}

// #region simple message
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

//#endregion
