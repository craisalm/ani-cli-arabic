"""Configuration constants and settings for ani-cli-arabic."""

import os
from pathlib import Path

# Application metadata
APP_NAME = "ani-cli-arabic"
APP_VERSION = "1.0.0"

# Base URLs for anime sources
BASE_URL = "https://witanime.cyou"
SEARCH_URL = f"{BASE_URL}/?search_param=animes&s="
EPISODE_URL = f"{BASE_URL}/episode/"

# Supported video qualities
QUALITIES = ["1080p", "720p", "480p", "360p"]
DEFAULT_QUALITY = "720p"

# Supported video players
SUPPORTED_PLAYERS = {
    "mpv": "mpv",
    "vlc": "vlc",
    "ffplay": "ffplay",
    "iina": "iina",  # macOS
}
DEFAULT_PLAYER = "mpv"

# HTTP request settings
REQUEST_TIMEOUT = 30  # seconds
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ar,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# Cache and history settings
CACHE_DIR = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / APP_NAME
CONFIG_DIR = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")) / APP_NAME
HISTORY_FILE = CONFIG_DIR / "history.json"
CACHE_EXPIRY = 3600  # seconds (1 hour)

# Search settings
MAX_SEARCH_RESULTS = 20
MIN_QUERY_LENGTH = 2

# Episode range defaults
DEFAULT_EPISODE_START = 1
MAX_EPISODES_BATCH = 50

# Terminal / UI settings
COLORS_ENABLED = os.environ.get("NO_COLOR") is None
PAGER_LINES = int(os.environ.get("LINES", 24))

# Subtitle settings
SUBTITLE_LANG = "ar"  # Arabic subtitles preferred
SUBTITLE_FALLBACK = "en"

# Downloader settings
DOWNLOAD_DIR = Path(os.environ.get("ANI_CLI_DOWNLOAD_DIR", Path.home() / "Videos" / "Anime"))
DOWNLOAD_TOOL = os.environ.get("ANI_CLI_DOWNLOAD_TOOL", "ffmpeg")

# Environment variable overrides
def get_player() -> str:
    """Return the configured video player, falling back to default."""
    return os.environ.get("ANI_CLI_PLAYER", DEFAULT_PLAYER)


def get_quality() -> str:
    """Return the configured video quality, falling back to default."""
    quality = os.environ.get("ANI_CLI_QUALITY", DEFAULT_QUALITY)
    if quality not in QUALITIES:
        return DEFAULT_QUALITY
    return quality


def ensure_dirs() -> None:
    """Create necessary configuration and cache directories if they don't exist."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
