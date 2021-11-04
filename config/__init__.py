'''
oskar.eiriksson@contentstack.com
2021-09-26

Some config functions and variables
'''
import logging


logLevel = logging.INFO  # Possible levels e.g.: DEBUG, ERROR, INFO
logging.basicConfig(
    format='%(asctime)s:%(levelname)s:%(message)s', level=logLevel)

# Folder/Directory definitions for all exports. Used to decide a folder and to validate that everything was exported correctly.
folderNames = {
    'contentTypes': 'contentTypes/',
    'deliveryTokens': 'deliveryTokens/',
    'environments': 'environments/',
    'extensions': 'extensions/',
    'globalFields': 'globalFields/',
    'labels': 'labels/',
    'languages': 'languages/',
    'publishingRules': 'publishingRules/',
    'roles': 'roles/',
    'webhooks': 'webhooks/',
    'workflows': 'workflows/',
    'entries': 'entries/',
    'assets': 'assets/',
    'folders': 'assets/'
}
# Filename definitions for all exports. Used to decide filename and to validate that everything was exported correctly.
fileNames = {
    'contentTypes': 'content_types.json',
    'deliveryTokens': 'delivery_tokens.json',
    'environments': 'environments.json',
    'extensions': 'extensions.json',
    'globalFields': 'global_fields.json',
    'labels': 'labels.json',
    'languages': 'languages.json',
    'publishingRules': 'publishing_rules.json',
    'roles': 'roles.json',
    'webhooks': 'webhooks.json',
    'workflows': 'workflows.json',
    'entries': 'entries.json',
    'assets': 'assets.json',
    'folders': 'folders.json'
}

# Text formatting for terminal logs.
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
WHITE = '\033[0;37m'
REDBG = '\033[0;41m'
GREENBG = '\033[0;42m'
END = '\033[0m'

contentType = {
    "content_type":
        {
            "title": "",
            "uid": "",
            "schema": [
                {
                    "display_name": "Title",
                    "uid": "title",
                    "data_type": "text",
                    "mandatory": True,
                    "unique": True,
                    "field_metadata": {
                        "_default": True,
                        "version": 3
                    },
                    "multiple": False,
                    "non_localizable": True
                },
                {
                    "data_type": "text",
                    "display_name": "Last Refresh",
                    "uid": "last_refresh",
                    "mandatory": False,
                    "multiple": False,
                    "non_localizable": True,
                    "unique": False,
                    "field_metadata": {
                        "instruction": "Timestamp for when the body field was last audited over all Content Types (Refreshed)."
                    }
                },
                {
                    "data_type": "number",
                    "display_name": "Refresh Rate",
                    "uid": "refresh_rate",
                    "mandatory": False,
                    "multiple": False,
                    "non_localizable": True,
                    "unique": False,
                    "field_metadata": {
                        "instruction": "Hours. How often the body field is refreshed. Changing it here will not change anything. Source of truth is in the webhook listener."
                    }
                },
                {
                    "display_name": "Body",
                    "extension_uid": "",
                    "field_metadata": {
                        "extension": True,
                        "default_value":"",
                        "instruction": "Full paths to all reference fields on all content types in this stack. Listed out in two different ways: Just a list with all of them and then also a query, that can be used directly with the Content Delivery API."
                    },
                    "uid": "body",
                    "config": {},
                    "multiple": False,
                    "mandatory": False,
                    "unique": False,
                    "non_localizable": True,
                    "data_type": "json"
                }
            ],
            "last_activity": {
                "environments": []
            },
            "maintain_revisions": True,
            "description": "Content Type that maps down all reference fields available in all content types.",
            "options": {
                "is_page": False,
                "singleton": True,
                "title": "title",
                "sub_title": []
            }
        }
}
