import os

from dotenv import load_dotenv
from notion_client import Client

load_dotenv()

notion = Client(
    auth=os.getenv("NOTION_API_KEY")
)

PAGE_ID = "335fca33-84fc-80c4-b5ea-f7bc51673049"


response = notion.blocks.children.list(
    block_id=PAGE_ID
)

print(f"Found {len(response['results'])} blocks\n")

for block in response["results"]:

    block_type = block["type"]

    print("TYPE:", block_type)

    if block_type == "paragraph":
        text = block["paragraph"]["rich_text"]

        for item in text:
            print(item["plain_text"])

    elif block_type == "heading_1":
        text = block["heading_1"]["rich_text"]

        for item in text:
            print(item["plain_text"])

    elif block_type == "heading_2":
        text = block["heading_2"]["rich_text"]

        for item in text:
            print(item["plain_text"])

    elif block_type == "bulleted_list_item":
        text = block["bulleted_list_item"]["rich_text"]

        for item in text:
            print(item["plain_text"])

    print()