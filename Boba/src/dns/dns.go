package dns

import (
	"boba/src/util"
	"fmt"
	"net"
)

func ServerStart() {
	// Load DNS server configuration from JSON file
	conf, err := util.LoadConfiguration()
	if err != nil {
		fmt.Println("Error loading configuration:", err)
		return
	}

	// Start the DNS server
	if err := startDNSServer(conf); err != nil {
		fmt.Println("Error starting DNS server:", err)
	}
}

func startDNSServer(conf util.Configuration) error {
	serverAddr := &net.UDPAddr{IP: net.ParseIP("127.0.0.1"), Port: conf.DNSPort}

	// Create a UDP connection for the server
	conn, err := net.ListenUDP("udp", serverAddr)
	if err != nil {
		return err
	}
	defer conn.Close()

	fmt.Printf("DNS server listening on %s:%d\n", serverAddr.IP, serverAddr.Port)

	// Handle incoming DNS requests
	for {
		go handleDNSRequest(conn, conf)
	}
}

func handleDNSRequest(conn *net.UDPConn, conf util.Configuration) {
	// Create a buffer to read incoming DNS requests
	buffer := make([]byte, 1024)

	// Read incoming DNS request from the client
	n, addr, err := conn.ReadFromUDP(buffer)
	if err != nil {
		fmt.Println("Error reading from UDP connection:", err)
		return
	}

	fmt.Printf("Received DNS request from %s\n", addr)

	// Parse the incoming DNS request and formulate a response
	// For simplicity, we'll just print the received data and respond with a dummy message
	domain := "localhost.com" // placeholder
	for _, d := range conf.Domains {
		if d.Domain == string(buffer[:n]) {
			domain = d.Domain
			break
		}
	}

	// Send a response back to the client
	response := []byte(fmt.Sprintf("Resolved IP address for %s is 127.0.0.1", domain))
	conn.WriteToUDP(response, addr)
}
