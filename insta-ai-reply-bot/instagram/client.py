from playwright.sync_api import sync_playwright


class InstagramClient:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None


    def start(self):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )

        try:
            context = self.browser.new_context(
                storage_state="instagram_session.json"
            )

        except:

            context = self.browser.new_context()

        self.page = context.new_page()

        return self.page


    def close(self):

        self.browser.close()
        self.playwright.stop()