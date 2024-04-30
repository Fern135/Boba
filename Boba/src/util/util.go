package util

import (
	"bufio"
	"encoding/json"
	"log"
	"os"
	"os/exec"
	"regexp"
	"strings"
)

type Configuration struct {
	SoftwareVersion  string `json:"software-version"`
	DefaultDatabase  string `json:"default-data-base"`
	Development      bool   `json:"development"`
	LanguageVersions struct {
		PHPVersion    []string `json:"php-version"`
		PythonVersion []string `json:"python-version"`
		NodeVersion   []string `json:"node-version"`
		NPMVersion    []string `json:"npm-version"`
	} `json:"language-versions"`
	TimeFormat   []string `json:"time-format"`
	ProjectsPath string   `json:"projects-path"`
	DNSPort      int      `json:"dns-port"`
	Domains      []struct {
		Domain string `json:"domain"`
		Route  string `json:"route"`
	} `json:"domains"`
}

func LoadConfiguration(filename string) (Configuration, error) {
	var conf Configuration

	// Read JSON file
	data, err := os.ReadFile(filename)
	if err != nil {
		return Configuration{}, err
	}

	// Unmarshal JSON data into Configuration struct
	err = json.Unmarshal(data, &conf)
	if err != nil {
		return Configuration{}, err
	}

	return conf, nil
}

func RunCommandInDir(command, directory string) error {
	// Change to the specified directory
	if err := os.Chdir(directory); err != nil {
		return err
	}

	// Execute the command
	cmd := exec.Command("bash", "-c", command)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		return err
	}

	return nil

	/*
		example: usage
		command := "ls -l" // Example command
		directory := "/path/to/directory" // Example directory

		if err := RunCommandInDir(command, directory); err != nil {
			fmt.Println("Error:", err)
			return
		}
	*/
}

func IsValidEmail(email string) bool {
	// Regular expression for validating email addresses
	pattern := `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`

	// Compile the regular expression
	regex := regexp.MustCompile(pattern)

	// Use the compiled regular expression to match the email address
	return regex.MatchString(email)
}

func getEnv() map[string]string {
	file, err := os.Open("../../../.env")
	if err != nil {
		log.Fatalf("Error opening .env file: %v", err)
	}
	defer file.Close()

	// Create a map to store environment variables
	env := make(map[string]string)

	// Read .env file line by line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, "=")
		if len(parts) == 2 {
			env[parts[0]] = parts[1]
		}
	}

	// Check for errors during scanning
	if err := scanner.Err(); err != nil {
		log.Fatalf("Error scanning .env file: %v", err)
	}

	return env
}
