# import json
# import pytest
# import webbrowser

import socket
from ...dns.dns import DNSServer


def test_load_domain_mapping():
    # Create a DNSServer instance
    dns_server = DNSServer()

    # Load the domain mapping from a file
    domain_mapping = dns_server.load_domain_mapping("../../../bin/conf/conf.json")

    # Assert that the domain mapping is a dictionary
    assert isinstance(domain_mapping, dict)

    # Assert that the domain mapping contains a "domains" key
    assert "domains" in domain_mapping

    # Assert that the "domains" key is a list
    assert isinstance(domain_mapping["domains"], list)

    # Assert that the "domains" list contains a domain
    assert len(domain_mapping["domains"]) > 0


def test_dns_response():
    # Create a DNSServer instance
    dns_server = DNSServer()

    # Get the route for the domain "example.com"
    route = dns_server.dns_response("example.com")

    # Assert that the route is an IP address
    assert isinstance(route, bytes)

    # Assert that the route is a valid IP address
    assert socket.inet_aton("127.0.0.1") == route


def test_start_server():
    # Create a DNSServer instance
    dns_server = DNSServer()

    # Start the DNS server
    dns_server.start_server()

    # Assert that the DNS server is listening on port 53
    assert dns_server.udp_socket.getsockname()[1] == 53

    # Send a DNS query to the DNS server
    data = b""
    client_address = ("127.0.0.1", 53)
    dns_server.udp_socket.sendto(data, client_address)

    # Assert that the DNS server responds to the DNS query
    assert True