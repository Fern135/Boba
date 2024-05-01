package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"runtime"
)

// todo: replace cli.js with this
// todo: add more commands and make cli called "boba" for global usage

func deploy() {
	var command string
	switch runtime.GOOS {
	case "windows":
		command = "python ./deploy/deploy.py"
	case "darwin", "linux":
		command = "python3 ./deploy/deploy.py"
	default:
		log.Fatalf("Unsupported platform: %s", runtime.GOOS)
	}

	cmd := exec.Command("sh", "-c", command)
	output, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatalf("Error executing command: %s", err)
	}

	fmt.Println(string(output))
}

func envSetUp() {
	var command string
	switch runtime.GOOS {
	case "windows":
		command = "python ./setup/env.py.py"
	case "darwin", "linux":
		command = "python3 ./setup/env.py.py"
	default:
		log.Fatalf("Unsupported platform: %s", runtime.GOOS)
	}

	cmd := exec.Command("sh", "-c", command)
	output, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatalf("Error executing command: %s", err)
	}

	fmt.Println(string(output))
}

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: cli [command]")
		os.Exit(1)
	}

	command := os.Args[1]
	switch command {
	case "-d":
		deploy()
	case "-end":
		envSetUp()
	default:
		fmt.Println("Unknown command")
		os.Exit(1)
	}
}
