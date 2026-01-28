import re

#한국 PII데아터 
PASSWORD_REGEX = r"\b[A-Za-z0-9@#$%^&+=!]{8,}"
PHONE_KR = r"\b01[016789]-?\d{3,4}-?\d{4}"
PHONE_INTL = r"\b\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}"
ID_KR = r"\b\d{6}-?\d{7}"
CREDIT_CARD = r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}"
ACC_NUM = r"\b\d{2,4}-?\d{2,4}-?\d{3,6}"
EMAIL = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
IP_ADD = r"\b(?:\d{1,3}\.){3}\d{1,3}"
DOMAIN = r"(?<![/@])\b[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.(?:com|net|org|kr|io|dev|app|ai|co\.kr|or\.kr|go\.kr|ac\.kr)"
PASSPORT = r"\b[A-Z][0-9]{8}\b"
API_KEY = r"\b(?:sk|pk|api|key|token)[-_]?[A-Za-z0-9]{16,64}\b"
LICENSE_NUM = r"\b\d{2}-?\d{2}-?\d{6}-?\d{2}"
MONEY_REGEX = r"\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\s?(?:원|만원|천원|억원|억|조)\b | ₩\s?\d{1,3}(?:,\d{3})*|\d+(?:\.\d+)?\s?(?:달러|USD|\$)"
GENERIC_API_KEY = r"\b(?:sk|pk|api|key|token)[-_]?[A-Za-z0-9]{16,64}\b"

#순서 중요함
REGEX_PATTERNS = [
    ("PHONE_KR", PHONE_KR),
    ("ID_KR", ID_KR),
    ("PASSPORT", PASSPORT),
    ("LICENSE_NUM", LICENSE_NUM),
    ("CREDIT_CARD", CREDIT_CARD),
    ("EMAIL", EMAIL),
    ("IP_ADD", IP_ADD),
    ("DOMAIN", DOMAIN),
    ("API_KEY", API_KEY),
    ("PASSWORD", PASSWORD_REGEX),
    ("MONEY", MONEY_REGEX),
    ("GG_API", GENERIC_API_KEY),
    ("PHONE_INTL", PHONE_INTL),
    ("ACC_NUM", ACC_NUM),
]


#get regex in data
def get_regex_pattern(text: str):
    results = []
    detected_values = set()

    for label, pattern in REGEX_PATTERNS:
        matches = re.findall(pattern, text)

        for value in matches:
            # Skip PASSWORD if already detected as another type
            if label == "PASSWORD" and value in detected_values:
                continue

            results.append({
                "type": "REGEX",
                "label": label,
                "value": value
            })
            detected_values.add(value)

    return results