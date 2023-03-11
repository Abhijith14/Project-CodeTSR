import requests
import json


def output(post_text, image_url=None):
    # Set the access token and the post text
    access_token = os.environ["LINKEDIN_TOKEN"] # replace with your LinkedIn API access token


    # Set the API endpoint and headers
    api_endpoint = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }


    if not image_url:

        # Set the post data
        post_data = {
            "author": "urn:li:person:HpJI7Hq3FV", # replace with your LinkedIn profile ID
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": post_text
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }


    else:
        # Set the post data
        post_data = {
            "author": "urn:li:person:HpJI7Hq3FV", # replace with your LinkedIn profile ID
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": post_text
                    },
                    "shareMediaCategory": "IMAGE",
                    "media": [
                        {
                            "status": "READY",
                            "description": {
                                "text": "Image description"
                            },
                            "media": "urn:li:digitalmediaAsset:C5603AQEIl6oXMPOUvw",
                            "title": {
                                "text": "Image title"
                            },
                            "originalUrl": "https://abhijith14.github.io/Portfolio-v2/media/buddyai.png"
                        }
                    ]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }

    # Send the API request to create the post
    response = requests.post(api_endpoint, headers=headers, data=json.dumps(post_data))

    # Check the response status code
    if response.status_code == 201:
        print("Post created successfully.")
    else:
        # print(f"Error creating post. Status code: {response.status_code}")
        print("Error creating post. Status code:", response.status_code)
        # print("Error message:", error)
        print("Response body:", response.json())



