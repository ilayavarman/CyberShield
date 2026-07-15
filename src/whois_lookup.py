import whois
from datetime import datetime


def whois_lookup(domain):

    try:

        # Remove protocol if user enters full URL
        domain = domain.replace("https://", "").replace("http://", "")
        domain = domain.split("/")[0]

        w = whois.whois(domain)

        # -----------------------------
        # Handle date values
        # -----------------------------

        creation = w.creation_date
        expiration = w.expiration_date

        if isinstance(creation, list):
            creation = creation[0]

        if isinstance(expiration, list):
            expiration = expiration[0]

        creation_date = (
            creation.strftime("%d-%b-%Y")
            if isinstance(creation, datetime)
            else str(creation)
        )

        expiry_date = (
            expiration.strftime("%d-%b-%Y")
            if isinstance(expiration, datetime)
            else str(expiration)
        )

        # -----------------------------
        # Domain Age
        # -----------------------------

        if isinstance(creation, datetime):
            age = datetime.now().year - creation.year
            domain_age = f"{age} Years"
        else:
            domain_age = "Unknown"

        return {

            "domain": domain,

            "registrar": w.registrar or "Unknown",

            "creation_date": creation_date,

            "expiry_date": expiry_date,

            "country": w.country or "Unknown",

            "organization": w.org or "Unknown",

            "abuse_email": w.emails if w.emails else "Unknown",

            "name_servers": w.name_servers if w.name_servers else [],

            "status": w.status if w.status else "Unknown",

            "domain_age": domain_age

        }

    except Exception as e:

        return {

            "error": str(e)

        }


# ==========================================
# Test
# ==========================================

if __name__ == "__main__":

    from pprint import pprint

    pprint(
        whois_lookup("github.com")
    )