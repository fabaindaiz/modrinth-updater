from pydantic import BaseModel
from typing import Optional

class Project(BaseModel):
    slug: str
    title: str
    description: str
    categories: list[str]
    display_categories: list[str]
    client_side: str
    server_side: str
    project_type: str
    downloads: int
    project_id: str
    author: str
    versions: list[str]
    follows: int
    date_created: str
    date_modified: str
    latest_version: str
    license: str

    icon_url: Optional[str]
    color: Optional[str]
    thread_id: str
    monetization_status: str
    gallery: list[str]
    featured_gallery: str