# import json
# import webbrowser

import pytest
import socket
from ...dns.dns import DNSServer
from lib.util.util import get_absolute_path


def test_load_domain_mapping():
    # Create a DNSServer instance
    dns_server = DNSServer()

    # Load the domain mapping from a file
    domain_mapping = dns_server.load_domain_mapping(
        get_absolute_path("./bin/conf/conf.json")
    )

    # Assert that the domain mapping is a dictionary
    assert isinstance(domain_mapping, dict)

    # Assert that the domain mapping contains a "domains" key
    assert "domains" in domain_mapping

    # Assert that the "domains" key is a list
    assert isinstance(domain_mapping["domains"], list)

    # Assert that the "domains" list contains a domain
    assert len(domain_mapping["domains"]) > 0


# .test_dns.dnstest.py

def test_dns_response():
    # Create a DNSServer instance
    dns_server = DNSServer()

    # Get the route for the domain "example.com"
    route = dns_server.dns_response("example.com")

    # Assert that the route is an IP address
    assert isinstance(route, bytes)

    # Assert that the route is a valid IP address
    assert socket.inet_aton("127.0.0.1") == route


def test_load_domain_mapping():
    # Create a DNSServer instance
    dns_server = DNSServer()

    # Initialize the domain mapping variable
    domain_mapping = {}

    # Load the domain mapping from a file
    domain_mapping = dns_server.load_domain_mapping(
        get_absolute_path("./bin/conf/conf.json")
    )

    # Assert that the domain mapping is a dictionary
    assert isinstance(domain_mapping, dict)

    # Assert that the domain mapping contains a "domains" key
    assert "domains" in domain_mapping

    # Assert that the "domains" key is a list
    assert isinstance(domain_mapping["domains"], list)

    # Assert that the "domains" list contains a domain
    assert len(domain_mapping["domains"]) > 0

    # Assert that the domain mapping contains a domain for "www.google.com"
    assert "www.google.com" in domain_mapping["domains"]

    # Assert that the route for "www.google.com" is a valid IP address
    assert isinstance(domain_mapping["domains"]["www.google.com"]["route"], str)
    assert domain_mapping["domains"]["www.google.com"]["route"] == "8.8.8.8"



if __name__ == "__main__":
    # Run the tests
    pytest.main()
