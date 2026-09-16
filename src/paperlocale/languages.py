"""Language policy only; never substitutes for protected-content validation."""

from __future__ import annotations

import re


def normalize_language(value: str) -> str:
    """Normalize a BCP-47-like tag without guessing a language from its script."""
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z]{2,3}(?:[-_][A-Za-z0-9]{2,8})*", value.strip()):
        raise ValueError(f"Invalid language tag: {value!r}")
    parts = value.strip().replace("_", "-").split("-")
    return "-".join([parts[0].lower()] + [
        part.title() if len(part) == 4 else part.upper() if len(part) == 2 else part.lower()
        for part in parts[1:]
    ])


def language_identity(value: str) -> str:
    """Only explicitly supported equivalent tags share a run identity."""
    tag = normalize_language(value)
    return {"ru-RU": "ru"}.get(tag, tag)


# Unknown languages use a documented generic policy: hard invariants only.
# Chinese retains its historical gate, including the 40 ASCII-letter threshold.
_SCRIPTS = {"zh": re.compile(r"[\u3400-\u9fff]"),
            "ru": re.compile(r"[А-Яа-яЁё]")}
_ENGLISH_FUNCTION_WORDS = frozenset(
    "the a an this these those is are was were has have had been be being "
    "we our it its they their of in on with for from to and that which by as".split()
)

_ENGLISH_PROSE_VERBS = frozenset(
    "describes describe measured measures shows show indicates indicate suggests "
    "suggest observed observes found demonstrates demonstrate computed estimated".split()
)


def is_english_prose(text: str) -> bool:
    """Conservative sentence evidence, excluding names, symbols and short labels.

    Callers remove protected spans first. This is a failure heuristic, not a
    language detector or a semantic translation-quality score.
    """
    words = re.findall(r"\b[A-Za-z]+\b", text)
    function_words = [word.lower() for word in words if word.lower() in _ENGLISH_FUNCTION_WORDS]
    return (len(words) >= 8 and sum(map(len, words)) >= 40
            and ((len(function_words) >= 3 and len(set(function_words)) >= 2)
                 or (bool(function_words) and any(word.lower() in _ENGLISH_PROSE_VERBS for word in words))))


def target_text_errors(source_prose: str, target_prose: str, *,
                       source_language: str, target_language: str) -> list[str]:
    source = normalize_language(source_language).split("-", 1)[0]
    target = normalize_language(target_language).split("-", 1)[0]
    script = _SCRIPTS.get(target)
    if target == "zh":
        if len(re.findall(r"[A-Za-z]", source_prose)) >= 40 and not script.search(target_prose):
            return ["长正文片段缺少中文译文"]
    elif source == "en" and script is not None and is_english_prose(source_prose):
        # A token Cyrillic suffix must not disguise a copied English paragraph.
        letters = len(script.findall(target_prose))
        if not letters or (letters < 12 and is_english_prose(target_prose)):
            return [f"Long English prose appears untranslated for target_language={target_language}"]
    return []
