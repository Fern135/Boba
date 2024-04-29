package main

import (
	"fmt"
	"log"

	"boba/util"
)

const (
	conf = "./bin/conf/conf.json"
	// ENV  = util.getEnv()
)

// Access configuration values using nested keys
// phpVersion := conf.LanguageVersions.PHPVersion[0]
// fmt.Println("PHP Version:", phpVersion)

// Accessing nested arrays or objects
// firstDomain := conf.Domains[0]
// fmt.Println("First Domain:", firstDomain.Domain)

func main() {
	conf, err := util.LoadConfiguration(conf)
	if err != nil {
		log.Fatalf("Error loading configuration: %v", err)
	}

	fmt.Println("App version ", conf.SoftwareVersion)

	// fmt.Println("hello world")
}
