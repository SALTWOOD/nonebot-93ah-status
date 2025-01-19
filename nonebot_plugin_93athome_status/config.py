from nonebot import get_plugin_config
from pydantic import BaseModel


class Config(BaseModel):
    api_url: str = ''


plugin_name = 'nonebot_plugin_93athome_status'
plugin_version = 'v1.0.0'
plugin_config = get_plugin_config(Config)