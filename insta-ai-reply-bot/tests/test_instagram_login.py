from instagram.client import InstagramClient
import time


client = InstagramClient()

page = client.start()

page.goto(
    "https://www.instagram.com/"
)


time.sleep(10)


print(
    "Current URL:",
    page.url
)


input(
    "Press Enter to close..."
)


client.close()