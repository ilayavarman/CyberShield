import ssl
import socket
from urllib.parse import urlparse
from datetime import datetime


def check_ssl(domain):

    try:

        # Add HTTPS if missing
        if not domain.startswith(("http://", "https://")):
            domain = "https://" + domain

        parsed = urlparse(domain)
        hostname = parsed.hostname

        # Create SSL context
        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:

                cert = ssock.getpeercert()

                # Subject
                subject = dict(x[0] for x in cert["subject"])

                # Issuer
                issuer = dict(x[0] for x in cert["issuer"])

                common_name = subject.get("commonName", "Unknown")
                issuer_name = issuer.get("organizationName", "Unknown")

                valid_from = cert["notBefore"]
                valid_to = cert["notAfter"]

                # Convert dates
                start_date = datetime.strptime(
                    valid_from,
                    "%b %d %H:%M:%S %Y %Z"
                )

                expiry_date = datetime.strptime(
                    valid_to,
                    "%b %d %H:%M:%S %Y %Z"
                )

                days_remaining = (expiry_date - datetime.now()).days

                version = cert.get("version", "Unknown")

                return {

                    "website": hostname,

                    "status": "Valid ✅",

                    "issuer": issuer_name,

                    "common_name": common_name,

                    "valid_from": start_date.strftime("%d-%b-%Y"),

                    "valid_until": expiry_date.strftime("%d-%b-%Y"),

                    "days_remaining": days_remaining,

                    "port": 443,

                    "version": version

                }

    except Exception as e:

        return {

            "error": str(e)

        }


# Test
if __name__ == "__main__":

    from pprint import pprint

    pprint(check_ssl("github.com"))