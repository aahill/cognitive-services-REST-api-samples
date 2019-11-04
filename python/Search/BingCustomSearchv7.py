#Copyright (c) Microsoft Corporation. All rights reserved.
#Licensed under the MIT License.

# You may need the below as well
#pip install pipenv
#pipenv install requests
# <importsAndVars>
import json
import requests
import os

# Add your Bing Custom Search subscription key to your environment variables.
subscriptionKey = os.environ['BING_CUSTOM_SEARCH_SUBSCRIPTION_KEY']
endpoint = "https://api.cognitive.microsoft.com/bingcustomsearch"
customConfigId = "your-custom-config-id" #you can also use "1"
searchTerm = "Microsoft"
# </importsAndVars>
# <url>
# Add your Bing Custom Search endpoint to your environment variables.
url = endpoint + "/search?q=" + searchTerm + "&customconfig=" + customConfigId
# </url>
# <request>
r = requests.get(url, headers={'Ocp-Apim-Subscription-Key': subscriptionKey})
print(r.text)
# </request>
