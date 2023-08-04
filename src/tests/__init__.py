import pytest

from .test_dns.dnstest import *


def test_all():
    print("testing")

    print("testing dns")
    test_load_domain_mapping()
    test_dns_response()
    test_start_server()
    print("done testing dns")


if __name__ == "__main__":
    pytest.main()