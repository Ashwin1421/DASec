# Include the Dropbox SDK
import dropbox
from dropbox import sharing

# Get your app key and secret from the Dropbox developer website
__app_key = 'knrwin4cg64mes5'
__app_secret = 'ix5hyqwkiwmqyfa'
__auth_flow = dropbox.client.DropboxOAuth2FlowNoRedirect(__app_key, __app_secret)



# Function generates a URL for authorization of this app by user for Dropbox Access
def get_auth_url(self):
    # Generate a OAuth Flow for getting authorization from user using App key and App Secret
    self.auth_url = ''
    self.auth_url = __auth_flow.start()
    return self.auth_url



# This will generate a access token to access the linked Dropbox Account corresponding to the
# authorization code supplied
def get_access_token(self, code):
    self.client = None
    self.access_token, self.user_id = __auth_flow.finish(code)
    self.client = dropbox.client.DropboxClient(self.access_token)
    return self.client


def share_doc(self, client, file_name):
    self.client.get_account_info()