from dotenv import load_dotenv
from modules import textPost
import os

load_dotenv()


access_token = os.getenv('AT')  
userid = os.getenv('UID')       
message = "Exploring the latest AI trends! #ArtificialIntelligence #MachineLearning"
response = textPost.post_to_linkedin(access_token, message, userid)
print(response)
