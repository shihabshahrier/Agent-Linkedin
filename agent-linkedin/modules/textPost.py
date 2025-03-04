import requests as req

def post_to_linkedin(access_token, message, userid):
    api_url = 'https://api.linkedin.com/v2/ugcPosts'  # Corrected endpoint URL
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    post_data = {
        "author": f"urn:li:person:{userid}",  # Ensure 'urn:li:person' format for member ID
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": message
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    response = req.post(api_url, headers=headers, json=post_data)
    return response.json()