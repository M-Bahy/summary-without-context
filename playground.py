from atproto import Client, client_utils
from dotenv import load_dotenv
from bidi.algorithm import get_display
import arabic_reshaper
import os

load_dotenv()

USERNAME = os.getenv("BLUESKY_USERNAME")
PASSWORD = os.getenv("BLUESKY_PASSWORD")


def main():
    client = Client()
    profile = client.login(USERNAME, PASSWORD)
    name = profile.display_name
    # Handle Arabic names
    if not name.isascii():
        reshaped_text = arabic_reshaper.reshape(name)
        name = get_display(reshaped_text)
    print(f"Hello {name} from Python SDK")

    # text = client_utils.TextBuilder().text('Hello World from ')
    # text = text.link('Python SDK', 'https://atproto.blue')
    # post = client.send_post(text)
    # client.like(post.uri, post.cid)


if __name__ == "__main__":
    main()
