import requests
import json
import os
import time

from dotenv import load_dotenv
from ques_verifier import verify

load_dotenv()

users = int(os.getenv("users"))

query = """
query submissionList($offset: Int!, $limit: Int!) {
  submissionList(offset: $offset, limit: $limit) {
    submissions {
      title
      statusDisplay
      timestamp
    }
  }
}
"""

for i in range(1, users + 1):

    part1 = "TARGET_USERNAME{number}".format(number=i)
    part2 = "CSRF_TOKEN{number}".format(number=i)
    part3 = "LEETCODE_SESSION{number}".format(number=i)
    part4 = "Name{number}".format(number=i)

    TARGET_USERNAME = os.getenv(part1)
    CSRF_TOKEN = os.getenv(part2)
    LEETCODE_SESSION = os.getenv(part3)
    Name=os.getenv(part4)

    url = os.getenv("url")

    cookies = {
        "LEETCODE_SESSION": LEETCODE_SESSION,
        "csrftoken": CSRF_TOKEN
    }

    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "X-CSRFToken": CSRF_TOKEN
    }

    payload = {
        "query": query,
        "variables": {
            "offset": 0,
            "limit": 20
        }
    }

    submissions = {
        "data": {
            "submissionList": {
                "submissions": []
            }
        }
    }

    offset = 0

    while len(submissions["data"]["submissionList"]["submissions"]) < 251:

        payload["variables"]["offset"] = offset

        details = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=payload
        )

        data = details.json()
        page_subs = data["data"]["submissionList"]["submissions"]

        if not page_subs:
            break

        submissions["data"]["submissionList"]["submissions"].extend(page_subs)

        offset += 20
        time.sleep(0.3)

    Ques_solved = verify(submissions)

    print(
        "The number of Verified Questions solved by {Name} are {number}".format(
            Name=Name,
            number=Ques_solved
        )
    )
