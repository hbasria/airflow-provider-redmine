from __future__ import annotations
from typing import Any, Dict
from functools import cached_property

from redminelib import Redmine
from airflow.exceptions import AirflowException
from airflow.hooks.base import BaseHook


class RedmineHook(BaseHook):
    conn_name_attr = "redmine_conn_id"
    default_conn_name = "redmine_default"
    conn_type = "redmine"
    hook_name = "Redmine"

    def __init__(self, 
                 redmine_conn_id: str = default_conn_name, 
                 **kwargs):
        super().__init__()
        self.redmine_conn_id = redmine_conn_id
        self.connection = self.get_connection(redmine_conn_id)

        
    def _get_redmine_connection(self, url: str, key: str):
        return Redmine(url, key=key)  

    @cached_property
    def get_conn(self, conn_id=None) -> Redmine:

        if not conn_id:
            conn_id = getattr(self, self.conn_name_attr)
        
        conn = self.get_connection(conn_id)

        conn.extra = None 
        url = conn.host
        key = conn.get_password()

        return self._get_redmine_connection(url=url, key=key)

    def get_redmine_issues(self, project_id: str, **kwargs):
        return self.get_conn.issue.filter(project_id=project_id, **kwargs)

    
    def update_redmine_issue(self, id: int, **kwargs):
        return self.get_conn.issue.update(id, **kwargs)
