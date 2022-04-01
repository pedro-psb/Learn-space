
## Tips for public API for practicing

* https://github.com/public-apis/public-apis
* https://developers.themoviedb.org/3/getting-started/introduction
* https://newsapi.org/

## Sample usage of environment variables

* In .env: -> for local purposes onlypip
KEY=value

* In app.py:
from dotenv import load_dotenv
import os
load_dotenv()
KEY = os.getenv('KEY')

print(KEY)