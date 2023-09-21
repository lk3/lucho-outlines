"""Outlines is a Generative Model Programming Framework."""
from lucho_outlines.base import vectorize
from lucho_outlines.caching import clear_cache, disable_cache, get_cache
from lucho_outlines.text import prompt

__all__ = [
    "clear_cache",
    "disable_cache",
    "get_cache",
    "prompt",
    "vectorize",
]
