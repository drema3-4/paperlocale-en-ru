"""Safe text decoding for output captured from external commands."""

from __future__ import annotations

import locale
import sys


def decode_process_output(output: bytes | str | None) -> str:
    """Decode captured output without trusting one platform-wide encoding."""

    if output is None:
        return ""
    if isinstance(output, str):
        return output

    encodings = ["utf-8", locale.getpreferredencoding(False)]
    if sys.platform == "win32":
        # Unlike getpreferredencoding(), ``mbcs`` still denotes the active
        # Windows ANSI code page when the parent Python runs in UTF-8 mode.
        encodings.append("mbcs")
    for encoding in dict.fromkeys(encodings):
        try:
            return output.decode(encoding)
        except (LookupError, UnicodeDecodeError):
            continue
    return output.decode("utf-8", errors="backslashreplace")
