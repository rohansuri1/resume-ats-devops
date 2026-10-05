import re


def extract_keywords(text):
    """Extract meaningful words from text."""

    words = re.findall(r"\b[a-zA-Z][a-zA-Z0-9+#.-]*\b", text.lower())

    stop_words = {
        "and", "the", "for", "with", "from",
        "this", "that", "are", "you", "your",
        "have", "has", "will", "our", "but"
    }

    return {
        word for word in words
        if len(word) > 2 and word not in stop_words
    }


def analyze_resume(resume_text, job_description):
    """Compare resume keywords with job description keywords."""

    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)

    if not job_keywords:
        return {
            "score": 0,
            "matched": [],
            "missing": []
        }

    matched = sorted(resume_keywords.intersection(job_keywords))
    missing = sorted(job_keywords - resume_keywords)

    score = round((len(matched) / len(job_keywords)) * 100)

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }