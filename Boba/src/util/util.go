package util

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"os/exec"
	"regexp"
	"runtime"
	"strings"
	"time"
)

const (
	conf         = "../bin/conf/conf.json"
	TimeFormat   = "01/02/2006 - 03:04 PM"
	UrgentDir    = "../../../bin/log/urgent"
	NonUrgentDir = "../../../bin/log/Non_urgent"
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
	PHPPort      int      `json:"php-server-domain"`
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

// todo: debug why it's not logging
func LoggerErr(title, data string) bool {
	timestamp := time.Now().Format(TimeFormat)
	logFileName := fmt.Sprintf("%s/%s.log", UrgentDir, timestamp)

	if err := os.MkdirAll(UrgentDir, os.ModePerm); err != nil {
		fmt.Printf("Error creating log directory (%s): %v\n", UrgentDir, err)
		return false
	}

	logFile, err := os.OpenFile(logFileName, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Printf("Error opening log file (%s): %v\n", logFileName, err)
		return false
	}
	defer logFile.Close()

	logEntry := fmt.Sprintf("[%s] %s\n%s\n", timestamp, title, data)
	if _, err := logFile.WriteString(logEntry); err != nil {
		fmt.Printf("Error writing to log file (%s): %v\n", logFileName, err)
		return false
	}

	fmt.Println("Log file written successfully:", logFileName)
	return true
}

// todo: debug why it's not logging
func Logger(title, data string) bool {
	timestamp := time.Now().Format(TimeFormat)
	logFileName := fmt.Sprintf("%s/%s.log", NonUrgentDir, timestamp)

	if err := os.MkdirAll(NonUrgentDir, os.ModePerm); err != nil {
		fmt.Printf("Error creating log directory (%s): %v\n", NonUrgentDir, err)
		return false
	}

	logFile, err := os.OpenFile(logFileName, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Printf("Error opening log file (%s): %v\n", logFileName, err)
		return false
	}
	defer logFile.Close()

	logEntry := fmt.Sprintf("[%s] %s\n%s\n", timestamp, title, data)
	if _, err := logFile.WriteString(logEntry); err != nil {
		fmt.Printf("Error writing to log file (%s): %v\n", logFileName, err)
		return false
	}

	fmt.Println("Log file written successfully:", logFileName)
	return true
}

func RunCommandInDir(command, directory string) error {
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

func GetEnv() map[string]interface{} {
	file, err := os.Open("../../../.env")
	if err != nil {
		log.Fatalf("Error opening .env file: %v", err)
	}
	defer file.Close()

	// Create a map to store environment variables
	env := make(map[string]interface{})

	// Read .env file line by line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, "=")
		if len(parts) == 2 {
			// Check if the value is "true" or "false"
			if parts[1] == "true" {
				env[parts[0]] = true
			} else if parts[1] == "false" {
				env[parts[0]] = false
			} else {
				env[parts[0]] = parts[1]
			}
		}
	}

	// Check for errors during scanning
	if err := scanner.Err(); err != nil {
		log.Fatalf("Error scanning .env file: %v", err)
	}

	return env
}

// ==================== mysql and mongoDB windows ====================
func InstallPackages() {
	switch runtime.GOOS {
	case "darwin":
		macInstall()
	case "linux":
		unixInstall()
	case "windows":
		windowsInstall()
	default:
		fmt.Println("Unsupported operating system.")
	}
}

// ==================== installing databases ====================
func InstallDatabases() {
	switch runtime.GOOS {
	case "darwin":
		macDbInstall()
	case "linux":
		unixDbInstall()
	case "windows":
		windowsDbInstall()
	default:
		fmt.Println("Unsupported operating system.")
	}
}

// ==================== mysql and mongoDB unix ====================
func unixDbInstall() {
	if !isInstalled("mysql") || !isInstalled("mongodb-community") {
		if !isInstalled("mysql") && !isInstalled("mongodb-community") {
			// installing databases concurrently
			go func() {
				// brewTap("mongodb/brew")
				installCmdUnix("mysql")
				installCmdUnix("mongodb-community")
			}()
		}

		// installing databases concurrently
		go func() {
			// brewTap("mongodb/brew")
			installCmdUnix("mysql")
			installCmdUnix("mongodb-community")
		}()
	}
}

// ==================== mysql and mongoDB unix ====================
func macDbInstall() {
	if !isInstalled("mysql") || !isInstalled("mongodb/brew") || !isInstalled("mongodb-community") {
		if !isInstalled("mysql") && !isInstalled("mongodb/brew") && !isInstalled("mongodb-community") {
			// installing databases concurrently
			go func() {
				installCmdBrew("mysql")
				brewTap("mongodb/brew")
				installCmdBrew("mongodb-community")
			}()
		}

		// installing databases concurrently
		go func() {
			installCmdBrew("mysql")
			brewTap("mongodb/brew")
			installCmdBrew("mongodb-community")
		}()
	}
}

// ==================== mysql and mongoDB windows ====================
func windowsDbInstall() {
	if !isInstalled("mysql") || !isInstalled("mongodb-community") {
		if !isInstalled("mysql") && !isInstalled("mongodb-community") {
			// installing databases concurrently
			go func() {
				// brewTap("mongodb/brew")
				installPkgWindows("mysql")
				installPkgWindows("mongodb")
			}()
		}

		// installing databases concurrently
		go func() {
			// brewTap("mongodb/brew")
			installPkgWindows("mysql")
			installPkgWindows("mongodb")
		}()
	}
}

// ==================== Check if a command is installed ====================
func isInstalled(command string) bool {
	_, err := exec.LookPath(command)
	return err == nil
}

// ==================== installing languages for unix aka linux ====================
func unixInstall() {
	// Check if PHP is installed
	if !isInstalled("php") {
		fmt.Println("Installing PHP...")
		installCmdUnix("php")
	} else {
		fmt.Println("PHP:\t\t\t Is already installed.")
	}

	// Check if Python is installed
	if !isInstalled("python3") {
		fmt.Println("Installing Python...")
		installCmdUnix("python3")
	} else {
		fmt.Println("Python3:\t\t Is already installed.")
	}

	// Check if Node.js is installed
	if !isInstalled("node") {
		fmt.Println("Installing Node.js...")
		installCmdUnix("node")
	} else {
		fmt.Println("Node.js:\t\t Is already installed.")
	}

	// Check if npm is installed
	if !isInstalled("npm") {
		fmt.Println("Installing npm...")
		installCmdUnix("npm")
	} else {
		fmt.Println("npm:\t\t\t Is already installed.")
	}
}

// ==================== installing on mac using brew ====================
func macInstall() {
	fmt.Println("Installing HomeBrew (brew)...")
	if err := installBrew(); err != nil {
		fmt.Println("Error installing HomeBrew:", err)
		return
	}
	// Check if PHP is installed
	if !isInstalled("php") {
		fmt.Println("Installing PHP...")
		installCmdBrew("php")
	} else {
		fmt.Println("PHP:\t\t\t Is already installed.")
	}

	// Check if Python is installed
	if !isInstalled("python3") {
		fmt.Println("Installing Python...")
		installCmdBrew("python3")
	} else {
		fmt.Println("Python3:\t\t Is already installed.")
	}

	// Check if Node.js is installed
	if !isInstalled("node") {
		fmt.Println("Installing Node.js...")
		installCmdBrew("node")
	} else {
		fmt.Println("Node.js:\t\t Is already installed.")
	}

	// Check if npm is installed
	if !isInstalled("npm") {
		fmt.Println("Installing npm...")
		installCmdBrew("npm")
	} else {
		fmt.Println("npm:\t\t\t Is already installed.")
	}
}

// todo: debug for windows. unix installation works.
func windowsInstall() {
	// Install Chocolatey
	fmt.Println("Installing Chocolatey (choco)...")
	if err := installChocolatey(); err != nil {
		fmt.Println("Error installing Chocolatey:", err)
		return
	}

	// Install PHP
	fmt.Println("Installing PHP...")
	if err := installPkgWindows("php"); err != nil {
		fmt.Println("Error installing PHP:", err)
	}

	// Install Python
	fmt.Println("Installing Python...")
	if err := installPkgWindows("python"); err != nil {
		fmt.Println("Error installing Python:", err)
	}

	// Install Node.js
	fmt.Println("Installing Node.js...")
	if err := installPkgWindows("nodejs"); err != nil {
		fmt.Println("Error installing Node.js:", err)
	}
}

// ==================== install commands for unix system aka linux ====================
func installCmdUnix(command string) {
	// var installCmd *exec.Cmd //todo: delete
	installCmd := exec.Command("sudo", "apt", "install", "-y", command)
	output, err := installCmd.CombinedOutput()
	if err != nil {
		fmt.Printf("Error installing %s: %s\n", command, err)
		return
	}
	fmt.Printf("Installation of %s successful:\n%s\n", command, string(output))
}

// ==================== install packages using homebrew ====================
func installCmdBrew(packageName string) {
	// var installCmd *exec.Cmd //todo: delete
	installCmd := exec.Command("brew", "install", packageName)
	output, err := installCmd.CombinedOutput()
	if err != nil {
		fmt.Printf("Error installing %s: %s\n", packageName, err)
		return
	}
	fmt.Printf("Installation of %s successful:\n%s\n", packageName, string(output))
}

// ==================== adding to homebrew installation ====================
func brewTap(packageName string) {
	// var installCmd *exec.Cmd //todo: delete
	installCmd := exec.Command("brew", "tap", packageName)
	output, err := installCmd.CombinedOutput()
	if err != nil {
		fmt.Printf("Error installing %s: %s\n", packageName, err)
		return
	}
	fmt.Printf("Installation of %s successful:\n%s\n", packageName, string(output))
}

// ==================== Install a package using Chocolatey ====================
func installPkgWindows(packageName string) error {
	cmd := exec.Command("choco", "install", packageName, "-y")
	output, err := cmd.CombinedOutput()
	if err != nil {
		return fmt.Errorf("error installing %s: %s", packageName, err)
	}
	fmt.Printf("Installation of %s successful:\n%s\n", packageName, string(output))
	return nil
}

// ==================== install homebrew ====================
func installBrew() error {
	cmd := exec.Command("/bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'")
	output, err := cmd.CombinedOutput()
	if err != nil {
		return fmt.Errorf("error installing homeBrew: %s", err)
	}
	fmt.Println("homeBrew installed successfully:\n", string(output))
	return nil
}

// ==================== install chocolatey (windows) ====================
func installChocolatey() error {
	cmd := exec.Command("powershell", "-Command", "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")
	output, err := cmd.CombinedOutput()
	if err != nil {
		return fmt.Errorf("error installing Chocolatey: %s", err)
	}
	fmt.Println("Chocolatey installed successfully:\n", string(output))
	return nil
}
