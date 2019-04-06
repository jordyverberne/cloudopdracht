import authomatic
from authomatic.providers import oauth2, oauth1

CONFIG = {
    'twitter': { # Your internal provider name

        # Provider class
        'class_': oauth1.Twitter,

        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': '########################',
        'consumer_secret': '########################',
    },

   'facebook': {

        'class_': oauth2.Facebook,

        # Facebook is an AuthorizationProvider too.
        'consumer_key': '########################',
        'consumer_secret': '########################',

        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],
    },

    'amazon': {
        'class_': oauth2.Amazon,
        'consumer_key': '########################',
        'consumer_secret': '########################',
        'id': authomatic.provider_id(),
        'scope': oauth2.Amazon.user_info_scope,
    },

    'google': {
        'class_': oauth2.Google,

        'consumer_key': '19317847916-5a2rushqv9mpt2kjiv5b224s22et9pp2.apps.googleusercontent.com',
        'consumer_secret': 'Q_AYB_ktdRrVhLgKjZkKatYb',
        'id': authomatic.provider_id(),
        'scope': oauth2.Google.user_info_scope + [
            'https://www.googleapis.com/auth/calendar',
            'https://mail.google.com/mail/feed/atom',
            'https://www.googleapis.com/auth/drive',
            'https://gdata.youtube.com'],
        '_apis': {
            'List your calendars': ('GET', 'https://www.googleapis.com/calendar/v3/users/me/calendarList'),
            'List your YouTube playlists': ('GET', 'https://gdata.youtube.com/feeds/api/users/default/playlists?alt=json'),
        },
    },

    'linkedin': {
        'class_': oauth2.LinkedIn,
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'id': authomatic.provider_id(),
        'scope': oauth2.LinkedIn.user_info_scope + ['rw_nus', 'r_network'],
        '_name': 'LinkedIn',
        '_apis': {
            'List your connections': ('GET', 'https://api.linkedin.com/v1/people/~/connections'),
        },
    }
}

		
