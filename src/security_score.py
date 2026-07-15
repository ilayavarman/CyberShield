def calculate_security_score(
    website_result,
    ssl_result,
    dns_result,
    whois_result,
    tech_result
):
    """
    Calculate an overall security score (0-100)
    based on results from all CyberShield modules.
    """

    score = 0

    recommendations = []

    # ==========================================
    # Website Security (30 Marks)
    # ==========================================

    if website_result.get("https"):
        score += 10
    else:
        recommendations.append("Enable HTTPS.")

    if website_result.get("ssl_status") == "Valid ✅":
        score += 10
    else:
        recommendations.append("Use a valid SSL certificate.")

    website_headers = website_result.get("headers", {})

    header_count = sum(
        1 for value in website_headers.values() if value
    )

    score += min(header_count * 2, 10)

    # ==========================================
    # SSL Certificate (20 Marks)
    # ==========================================

    if ssl_result.get("status") == "Valid ✅":

        days = ssl_result.get("days_remaining", 0)

        if days > 180:

            score += 20

        elif days > 90:

            score += 15

        elif days > 30:

            score += 10

        else:

            score += 5

            recommendations.append(
                "SSL certificate expires soon."
            )

    # ==========================================
    # DNS (15 Marks)
    # ==========================================

    if dns_result.get("A Record"):
        score += 5

    if dns_result.get("MX Record"):
        score += 5

    if dns_result.get("NS Record"):
        score += 5

    # ==========================================
    # WHOIS (15 Marks)
    # ==========================================

    if whois_result.get("registrar") != "Unknown":
        score += 5

    if whois_result.get("creation_date") != "Unknown":
        score += 5

    if whois_result.get("expiry_date") != "Unknown":
        score += 5

    # ==========================================
    # Technology (20 Marks)
    # ==========================================

    security = tech_result.get("security", {})

    if security.get("HSTS"):
        score += 5
    else:
        recommendations.append(
            "Enable HSTS header."
        )

    if security.get("CSP"):
        score += 5
    else:
        recommendations.append(
            "Enable Content Security Policy."
        )

    if security.get("X-Frame"):
        score += 5
    else:
        recommendations.append(
            "Enable X-Frame-Options."
        )

    if security.get("X-Content"):
        score += 5
    else:
        recommendations.append(
            "Enable X-Content-Type-Options."
        )

    # ==========================================
    # Risk Level
    # ==========================================

    if score >= 85:

        risk = "🟢 Low"

    elif score >= 60:

        risk = "🟡 Medium"

    else:

        risk = "🔴 High"

    return {

        "score": score,

        "risk": risk,

        "recommendations": recommendations

    }