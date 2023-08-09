__version__ = "1.0.0"

## This is needed to allow Airflow to pick up specific metadata fields it needs for certain features.
def get_provider_info():
    return {
        "package-name": "airflow-provider-redmine",  # Required
        "name": "Redmine",  # Required
        "description": "A redmine provider for Apache Airflow.",  # Required
        "connection-types": [
            {
                "connection-type": "redmine",
                "hook-class-name": "redmine_provider.hooks.redmine.RedmineHook"
            }
        ],
        "versions": [__version__],  # Required
    }
