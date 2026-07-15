import dns.resolver
import socket


def dns_lookup(domain):

    try:

        # Remove https:// if user enters full URL
        domain = domain.replace("https://", "").replace("http://", "")
        domain = domain.split("/")[0]

        result = {}

        # -----------------------------------
        # IP Address
        # -----------------------------------

        try:
            result["IP Address"] = socket.gethostbyname(domain)
        except:
            result["IP Address"] = "Not Found"

        # -----------------------------------
        # A Record
        # -----------------------------------

        try:
            result["A Record"] = [
                str(r) for r in dns.resolver.resolve(domain, "A")
            ]
        except:
            result["A Record"] = []

        # -----------------------------------
        # AAAA Record
        # -----------------------------------

        try:
            result["AAAA Record"] = [
                str(r) for r in dns.resolver.resolve(domain, "AAAA")
            ]
        except:
            result["AAAA Record"] = []

        # -----------------------------------
        # MX Record
        # -----------------------------------

        try:
            result["MX Record"] = [
                str(r.exchange) for r in dns.resolver.resolve(domain, "MX")
            ]
        except:
            result["MX Record"] = []

        # -----------------------------------
        # NS Record
        # -----------------------------------

        try:
            result["NS Record"] = [
                str(r.target) for r in dns.resolver.resolve(domain, "NS")
            ]
        except:
            result["NS Record"] = []

        # -----------------------------------
        # TXT Record
        # -----------------------------------

        try:
            result["TXT Record"] = [
                str(r) for r in dns.resolver.resolve(domain, "TXT")
            ]
        except:
            result["TXT Record"] = []

        return result

    except Exception as e:

        return {

            "Error": str(e)

        }