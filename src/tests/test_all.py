import pytest

from .test_dns.dnstest import test_load_domain_mapping, test_dns_response


def test_all():
    print("testing")

    #******************** testing dns ********************
    print("testing dns")
    test_load_domain_mapping()
    test_dns_response()
    #******************** testing dns ********************




if __name__ == "__main__":
    pytest.main()
