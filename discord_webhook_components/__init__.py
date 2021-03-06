from .all import button, URLbutton, checkWebhook, checkWebhookToken, send, embed, style
from .exceptions import IncorrectLinkError, WebhookNotFound, NoTokenError, RateLimitError

"""
discord_webhook_components is a module that displays components in a webhook message.
"""


__version__ = "0.0.2"
__author__ = "AWeirdScratcher"
__email__ = "aweirdscratcher@gmail.com"
__copyright__ = "Copyright 2021, AWeirdScratcher"

__all__ = [
    "button",
    "URLbutton",
    "checkWebhook",
    "checkWebhookToken",
    "send",
    "embed",
    "IncorrectLinkError",
    "WebhookNotFound",
    "NoTokenError",
    "RateLimitError",
    "style"
]
