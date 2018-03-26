# Broadcast messages to facebook

A [Supercode](http://gosupercode.com) function will broadcast messages to facebook. Use in server-side to protect your FB page access token

## Sample Usage

[Supercode](http://gosupercode.com) SDK will be available after the launch.

```
import json
import pprint
import supercode

response = supercode.call(
    "broadcast-to-messenger",
    "your-supercode-api-key",
    message='{"text": "Hello, World!"}',
    FB_ids='[112233445566,112233445566,112233445566]',
    page_access_token='<FACEBOOK_PAGE_ACCESS_TOKEN>',
    messaging_type='UPDATE'
)

    
pprint(response)
```

**Note:** Supercode has not been launched yet. This is for internal testing only.
