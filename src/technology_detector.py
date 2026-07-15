import requests
import time
from bs4 import BeautifulSoup


def detect_technology(url):

    try:

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        start = time.time()

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        end = time.time()

        html = response.text.lower()

        headers = response.headers

        response_time = round((end - start) * 1000, 2)

        # ------------------------------------
        # Server
        # ------------------------------------

        server = headers.get("Server", "Unknown")

        # ------------------------------------
        # CDN
        # ------------------------------------

        cdn = "Unknown"

        if "cloudflare" in server.lower():
            cdn = "Cloudflare"

        elif "cloudfront" in server.lower():
            cdn = "AWS CloudFront"

        elif "akamai" in server.lower():
            cdn = "Akamai"

        elif "fastly" in server.lower():
            cdn = "Fastly"

        # ------------------------------------
        # Frontend
        # ------------------------------------

        frontend = []

        if "__next" in html:
            frontend.append("Next.js")

        if "react" in html:
            frontend.append("React")

        if "vue" in html:
            frontend.append("Vue.js")

        if "angular" in html:
            frontend.append("Angular")

        if "bootstrap" in html:
            frontend.append("Bootstrap")

        # ------------------------------------
        # Backend
        # ------------------------------------

        backend = []

        powered = headers.get("X-Powered-By", "")

        if "php" in powered.lower():
            backend.append("PHP")

        if "express" in powered.lower():
            backend.append("Express.js")

        if "asp.net" in powered.lower():
            backend.append("ASP.NET")

        if "django" in html:
            backend.append("Django")

        if "flask" in html:
            backend.append("Flask")

        # ------------------------------------
        # CMS
        # ------------------------------------

        cms = []

        if "wp-content" in html:
            cms.append("WordPress")

        # ------------------------------------
        # Security Headers
        # ------------------------------------

        security = {

            "HSTS":
                "Strict-Transport-Security" in headers,

            "CSP":
                "Content-Security-Policy" in headers,

            "X-Frame":
                "X-Frame-Options" in headers,

            "X-Content":
                "X-Content-Type-Options" in headers

        }

        return {

            "server": server,

            "cdn": cdn,

            "frontend": frontend,

            "backend": backend,

            "cms": cms,

            "security": security,

            "status": response.status_code,

            "response_time": response_time,

            "url": url

        }

    except Exception as e:

        return {

            "error": str(e)

        }