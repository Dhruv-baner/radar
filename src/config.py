"""
Configuration management for Radar project.
Loads environment variables and defines project settings.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Central configuration class for Radar."""
    
    # API Keys
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    
    # ArXiv Settings
    ARXIV_MAX_RESULTS = 10
    ARXIV_SORT_BY = 'submittedDate'
    ARXIV_SORT_ORDER = 'descending'
    
    # Project Paths
    PROJECT_ROOT = Path(__file__).parent.parent
    DATA_DIR = PROJECT_ROOT / 'data'
    RAW_DATA_DIR = DATA_DIR / 'raw'
    PROCESSED_DATA_DIR = DATA_DIR / 'processed'
    CACHE_DIR = DATA_DIR / 'cache'
    
    # Database
    DB_PATH = DATA_DIR / 'radar.db'
    
    # Vector Database
    VECTOR_DB_PATH = DATA_DIR / 'chroma_db'
    
    # LLM Settings
    DEFAULT_MODEL = 'claude-sonnet-4-20250514'
    MAX_TOKENS = 4096
    TEMPERATURE = 0.7
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present."""
        if not cls.ANTHROPIC_API_KEY:
            raise ValueError(
                "ANTHROPIC_API_KEY not found. "
                "Please create a .env file with your API key."
            )
        

