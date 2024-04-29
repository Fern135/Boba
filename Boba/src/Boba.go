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

func main() {
	conf, err := util.LoadConfiguration(conf)
	if err != nil {
		log.Fatalf("Error loading configuration: %v", err)
	}

	// Access configuration values using nested keys
	phpVersion := conf.LanguageVersions.PHPVersion[0]
	fmt.Println("PHP Version:", phpVersion)

	// Accessing nested arrays or objects
	firstDomain := conf.Domains[0]
	fmt.Println("First Domain:", firstDomain.Domain)

	// fmt.Println("hello world")
}
