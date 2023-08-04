import json
import socket
import webbrowser

class DNSServer:
    def __init__(self):
        self.domain_mapping = self.load_domain_mapping("../../bin/conf/conf.json")
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ("127.0.0.1", 53)

    def load_domain_mapping(self, file_path):
        with open(file_path, "r") as file:
            return json.load(file)

    def dns_response(self, query_domain):
        for entry in self.domain_mapping["domains"]:

            if entry["domain"] == query_domain:
                return entry["route"].encode()

        # If the domain is not found in the mapping, return an empty response
        return b""

    def start_server(self):
        try:
            self.udp_socket.bind(self.server_address)
            print("DNS server listening on {}:{}".format(*self.server_address))

            while True:
                data, client_address = self.udp_socket.recvfrom(4096)
                query_domain = data[12:].split(b"\x00", 1)[0].decode()

                # Get the route for the requested domain from the domain_mapping
                route = self.dns_response(query_domain)

                if route:
                    response = data[:2] + b"\x81\x80"
                    response += data[4:6] + data[4:6] + b"\x00\x00\x00\x00"  # Flags and counts
                    response += data[12:]  # Query part
                    response += b"\xc0\x0c"  # Pointer to domain name in question
                    response += b"\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04"  # DNS response with type A and class IN
                    response += socket.inet_aton(route)  # Convert route to IP address bytes

                    self.udp_socket.sendto(response, client_address)

        except Exception as e:
            print(f"error: {str(e)}")


# if __name__ == "__main__":
#     dns_server = DNSServer()
#     dns_server.start_server()
