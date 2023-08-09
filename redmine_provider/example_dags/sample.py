from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

from redminelib import Redmine



@dag(
    schedule=None,
    start_date=days_ago(1),
    tags=["example"],
)
def redmine_issues_workflow():
    redmine = Redmine('https://api.redmine.org', key='secure-key')

    @task()
    def get_redmine_issues_task():
        issues = redmine.issue.filter(project_id='envanter', status_id=1, sort='id:desc')

        for issue in issues:
            print(issue.id, issue.subject)

    get_redmine_issues_task()

redmine_issues_workflow = redmine_issues_workflow()

if __name__ == "__main__":
    redmine_issues_workflow.test()
