import requests
import socket
import ssl
import time

from urllib.parse import urlparse
from datetime import datetime


# ==========================================================
# Website Security Checker
# ==========================================================

def check_website(url):

    # ------------------------------------------------------
    # Add HTTPS Automatically
    # ------------------------------------------------------

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed = urlparse(url)

    hostname = parsed.hostname

    if hostname is None:
        hostname = parsed.netloc

    # ------------------------------------------------------
    # Default Values
    # ------------------------------------------------------

    website_name = hostname

    favicon = f"https://www.google.com/s2/favicons?domain={hostname}&sz=128"

    ip_address = "Unavailable"

    server = "Unknown"

    status_code = 0

    response_time = 0

    https_enabled = url.startswith("https://")

    ssl_status = "Unavailable"

    ssl_expiry = "Unavailable"

    security_headers = {
        "Strict-Transport-Security": False,
        "Content-Security-Policy": False,
        "X-Frame-Options": False,
        "X-Content-Type-Options": False,
        "Referrer-Policy": False
    }

    # ------------------------------------------------------
    # Get IP Address
    # ------------------------------------------------------

    try:

        ip_address = socket.gethostbyname(hostname)

    except Exception:

        ip_address = "Unavailable"

    # ------------------------------------------------------
    # Request Website
    # ------------------------------------------------------

    try:

        start = time.time()

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
        )

        end = time.time()

        response_time = round(
            (end - start) * 1000,
            2
        )

        status_code = response.status_code

        server = response.headers.get(
            "Server",
            "Unknown"
        )

        headers = response.headers

        for header in security_headers:

            security_headers[header] = (
                header in headers
            )

    except Exception as e:

        return {

            "error": str(e)

        }

    # ------------------------------------------------------
    # SSL Certificate
    # ------------------------------------------------------

    if https_enabled:

        try:

            context = ssl.create_default_context()

            with context.wrap_socket(
                socket.socket(),
                server_hostname=hostname
            ) as s:

                s.settimeout(5)

                s.connect((hostname, 443))

                certificate = s.getpeercert()

                ssl_status = "Valid ✅"

                expiry = datetime.strptime(
                    certificate["notAfter"],
                    "%b %d %H:%M:%S %Y %Z"
                )

                ssl_expiry = expiry.strftime(
                    "%d-%b-%Y"
                )

        except:

            ssl_status = "Unavailable"

            ssl_expiry = "Unavailable"

                # ------------------------------------------------------
    # Calculate Security Score
    # ------------------------------------------------------

    score = 0

    # HTTPS
    if https_enabled:
        score += 20

    # SSL
    if ssl_status == "Valid ✅":
        score += 20

    # HTTP Status
    if status_code == 200:
        score += 10

    # Security Headers
    header_count = 0

    for value in security_headers.values():
        if value:
            header_count += 1

    score += header_count * 10

    if score > 100:
        score = 100

    # ------------------------------------------------------
    # Risk Level
    # ------------------------------------------------------

    if score >= 80:
        risk = "🟢 Low"

    elif score >= 50:
        risk = "🟡 Medium"

    else:
        risk = "🔴 High"

    # ------------------------------------------------------
    # Return Result
    # ------------------------------------------------------

    return {

        "website": website_name,

        "favicon": favicon,

        "ip": ip_address,

        "server": server,

        "status": status_code,

        "response_time": response_time,

        "https": https_enabled,

        "ssl_status": ssl_status,

        "ssl_expiry": ssl_expiry,

        "headers": security_headers,

        "score": score,

        "risk": risk

    }


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    from pprint import pprint

    pprint(
        check_website("https://github.com")
)