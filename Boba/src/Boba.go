package main

import (
	"boba/util"
	"fmt"
)

const (
	conf  = "./bin/conf/conf.json"
	panel = "" // todo: add panel once it's working.
	// ENV  = util.getEnv()
)

// Access configuration values using nested keys
// phpVersion := conf.LanguageVersions.PHPVersion[0]
// fmt.Println("PHP Version:", phpVersion)

// Accessing nested arrays or objects
// firstDomain := conf.Domains[0]
// fmt.Println("First Domain:", firstDomain.Domain)

func main() {
	config, err := util.LoadConfiguration(conf)
	if err != nil {
		// log.Fatalf("Error loading configuration: %v", err)
		util.LoggerErr("Error in config", err.Error())
	}

	fmt.Println("App version ", config.SoftwareVersion)

	// fmt.Println("hello world")
}
