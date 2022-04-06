from mastodon import Mastodon
from config import MASTODON_TOKEN


mastodon = Mastodon(
    access_token = MASTODON_TOKEN,
    api_base_url = 'https://projekt-mastodon.h-ka-iwi.de/'
)
print(MASTODON_TOKEN)

# print(mastodon.toot('Hello World mark2'))
message = '@admin Hello World mark2'

toot = Mastodon.status_post(self=mastodon, 
    status=message, 
    in_reply_to_id=None, 
    media_ids=None, 
    sensitive=False, 
    visibility='direct', 
    spoiler_text=None, 
    language=None, 
    idempotency_key=None, 
    content_type=None, 
    scheduled_at=None, 
    poll=None, 
    quote_id=None)
print(toot)
id = toot['id']
print(id)
