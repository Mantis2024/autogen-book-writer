"""Configuration for the book generation system"""
import os
from typing import Dict, List

def get_config(local_url: str = "http://localhost:1234/v1") -> Dict:
    """Get the configuration for the agents"""
    
    # Basic config for local LLM
    config_list = [{
        'model': 'Mistral-Nemo-Instruct-2407',
        'base_url': local_url,
        'api_key': "not-needed"
    }]

    # Common configuration for all agents
    agent_config = {
        "seed": 42,
        "temperature": 0.7,
        "config_list": config_list,
        "timeout": 600,
        "cache_seed": None
    }
    
    return agent_config