# User info
USER_NAME = ''
USER_PASSWORD = ''
'''
  User app info, more info here 
  https://praw.readthedocs.io/en/stable/getting_started/quick_start.html
  https://www.reddit.com/prefs/apps/
'''
USER_AGENT = ''
CLIENT_ID = ''
CLIENT_SECRET = ''

'''
  OpenAi ChatGPT session, You can find the session token manually from your browser:

  1. Go to https://chat.openai.com/api/auth/session
  2. Press F12 to open console
  3. Go to Application > Cookies
  4. Copy the session token value in __Secure-next-auth.session-token
'''
GPT_SESSION = ''

'''
  monitor target subs，multi subs divide with character +, sub name is case insensitive
  E.g. MONITOR_SUBS = 'test+programmerhumor'
'''
MONITOR_SUBS = 'test+programmerhumor'

__all__ = [
  USER_NAME,
  USER_PASSWORD,
  USER_AGENT,
  CLIENT_ID,
  CLIENT_SECRET,
  GPT_SESSION,
  MONITOR_SUBS,
]
