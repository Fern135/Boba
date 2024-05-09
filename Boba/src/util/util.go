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
	config       = "../bin/conf/conf.json"
	TimeFormat   = "01/02/2006 - 03:04 PM"
	UrgentDir    = "../../../bin/log/urgent"
	NonUrgentDir = "../../../bin/log/Non_urgent"
)

type Configuration struct {
	SoftwareVersion  string `json:"software-version"`
	DefaultDatabase  string `json:"default-database"`
	LanguageVersions struct {
		IsInstalled   bool     `json:"Is-Installed"`
		GoVersion     []string `json:"go-version"`
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

// ==================== loadingConfiguration from conf.json ====================
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

// ==================== run specific command in directory ====================
func RunCommandInDir(command, directory string) error {
	if err := os.Chdir(directory); err != nil {
		return err
	}

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

// ==================== checking if email is valid format ====================
func IsValidEmail(email string) bool {
	pattern := `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
	regex := regexp.MustCompile(pattern)

	return regex.MatchString(email)
}

// ==================== getting enviroment variables ====================
func GetEnv(filePath string) map[string]interface{} {
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatalf("Error opening .env file: %v", err)
	}
	defer file.Close()

	env := make(map[string]interface{})

	// Read .env file line by line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, "=")
		if len(parts) == 2 {
			// Check if the key is "debugging" or "debug"
			key := strings.TrimSpace(parts[0])
			value := strings.TrimSpace(parts[1])
			if key == "debugging" || key == "debug" {
				// Check if the value is "true" or "false"
				if value == "true" {
					env[key] = true
				} else if value == "false" {
					env[key] = false
				} else {
					env[key] = value
				}
			} else {
				env[key] = value
			}
		}
	}

	// Check for errors during scanning
	if err := scanner.Err(); err != nil {
		log.Fatalf("Error scanning .env file: %v", err)
	}

	return env
}

// ==================== loading bar ====================
func MeasureTime(f func()) int {
	start := time.Now()
	f() // Call the function
	elapsed := time.Since(start)
	// fmt.Printf("Function execution time: %s\n", elapsed)
	return int(elapsed)
}

// ==================== loading bar ====================
// func printProgressBar(iteration, total int, fill string) {
func ProgressBar(total int) {
	prefix := "%"        // prefix string
	suffix := "Complete" // suffix string
	length := total - 5  // length
	iteration := 1       // to initialize the iteration
	fill := "="          // fill string
	percent := float64(iteration) / float64(total)
	filledLength := int(length * iteration / total)
	end := ">"

	if iteration == total {
		end = "="
	}
	bar := strings.Repeat(fill, filledLength) + end + strings.Repeat("-", (length-filledLength))

	// Calculate elapsed time
	// elapsed := time.Since(startTime)

	for init := 0; init < total; init++ {
		fmt.Printf("\r%s [%s] %f%% - Elapsed time: %s", prefix, bar, percent, suffix)
	}
	if iteration == total {
		fmt.Println()
	}
}

// func main() {
// 	for i := 0; i < 30; i++ {
// 		time.Sleep(500 * time.Millisecond) // mimics work
// 		printProgressBar(i+1, 30, "Progress", "Complete", 25, "=")
// 	}
// }

func GetPcDevOs() string {
	switch runtime.GOOS {
	case "darwin":
		return "Mac"
	case "linux":
		return "Linux"
	case "windows":
		return "Windows"
	default:
		return "Unkown Os"
	}
}

// ==================== mysql and mongoDB windows ====================
func InstallPackages() int {
	start := time.Now()
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
	return int(time.Since(start))
}

// ==================== installing databases ====================
func InstallDatabases() int {
	start := time.Now()
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
	return int(time.Since(start))
}

// ==================== mysql and mongoDB unix ====================
func unixDbInstall() {
	if !isInstalled("mysql") || !isInstalled("mongodb-community") {
		if !isInstalled("mysql") && !isInstalled("mongodb-community") {
			// installing databases concurrently
			// brewTap("mongodb/brew")
			go installCmdUnix("mysql")
			go installCmdUnix("mongodb-community")
		}

		// installing databases concurrently
		// brewTap("mongodb/brew")
		go installCmdUnix("mysql")
		go installCmdUnix("mongodb-community")
	}
}

// ==================== mysql and mongoDB mac ====================
func macDbInstall() {
	if !isInstalled("mysql") || !isInstalled("mongodb/brew") || !isInstalled("mongodb-community") {
		if !isInstalled("mysql") && !isInstalled("mongodb/brew") && !isInstalled("mongodb-community") {
			// installing databases concurrently
			go installCmdBrew("mysql")
			go brewTap("mongodb/brew")
			go installCmdBrew("mongodb-community")
		}

		// installing databases concurrently
		go installCmdBrew("mysql")
		go brewTap("mongodb/brew")
		go installCmdBrew("mongodb-community")

	}
}

// ==================== mysql and mongoDB windows ====================
func windowsDbInstall() {
	if !isInstalled("mysql") || !isInstalled("mongodb-community") {
		if !isInstalled("mysql") && !isInstalled("mongodb-community") {
			// installing databases concurrently

			// brewTap("mongodb/brew")
			go installPkgWindows("mysql")
			go installPkgWindows("mongodb")
		}

		// installing databases concurrently
		// brewTap("mongodb/brew")
		go installPkgWindows("mysql")
		go installPkgWindows("mongodb")
	}
}

// ==================== Check if command is installed ====================
func isInstalled(command string) bool {
	_, err := exec.LookPath(command)
	return err == nil
}

// ==================== installing languages for unix aka linux ====================
func unixInstall() {

	// go
	if !isInstalled("go version") {
		fmt.Println("Installing Go")
		installCmdUnix("go")
	} else {
		fmt.Printf("\nGo:\t\t Is already installed.\n\n")
	}

	// PHP
	if !isInstalled("php") {
		fmt.Println("Installing PHP...")
		installCmdUnix("php")
	} else {
		fmt.Println("PHP:\t\t\t Is already installed.")
	}

	// Python
	if !isInstalled("python3") {
		fmt.Println("Installing Python...")
		installCmdUnix("python3")
	} else {
		fmt.Println("Python3:\t\t Is already installed.")
	}

	// Node.js
	if !isInstalled("node") {
		fmt.Println("Installing Node.js...")
		installCmdUnix("node")
	} else {
		fmt.Println("Node.js:\t\t Is already installed.")
	}

	// NPM
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
		fmt.Println("Error installing HomeBrew:\t", err)
		return
	}
	// PHP
	if !isInstalled("php") {
		fmt.Println("Installing PHP...")
		installCmdBrew("php")
	} else {
		fmt.Println("PHP:\t\t\t Is already installed.")
	}

	// Python
	if !isInstalled("python3") {
		fmt.Println("Installing Python...")
		installCmdBrew("python3")
	} else {
		fmt.Println("Python3:\t\t Is already installed.")
	}

	// Node.js
	if !isInstalled("node") {
		fmt.Println("Installing Node.js...")
		installCmdBrew("node")
	} else {
		fmt.Println("Node.js:\t\t Is already installed.")
	}

	// NPM
	if !isInstalled("npm") {
		fmt.Println("Installing npm...")
		installCmdBrew("npm")
	} else {
		fmt.Println("npm:\t\t\t Is already installed.")
	}
}

// todo: debug for windows. unix installation works.
// todo: test for mac
func windowsInstall() {
	// Install Chocolatey
	fmt.Println("Installing Chocolatey (choco)...")
	if err := installChocolatey(); err != nil {
		fmt.Println("Error installing Chocolatey:", err)
		return
	}

	// PHP
	fmt.Println("Installing PHP...")
	if err := installPkgWindows("php"); err != nil {
		fmt.Println("Error installing PHP:", err)
	}

	// Python
	fmt.Println("Installing Python...")
	if err := installPkgWindows("python"); err != nil {
		fmt.Println("Error installing Python:", err)
	}

	// Node.js
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
