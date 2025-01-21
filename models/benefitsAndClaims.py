from playwright.sync_api import expect

class Benefits: 
    def __init__(self, page):
        self.page = page

    def navigateToHandsetClaim(self):
        expect(self.page.get_by_text("Benefits And Claims")).to_be_visible()
        self.page.get_by_text("Benefits And Claims").click()

        expect(self.page.get_by_text("Handset Claim", exact=True)).to_be_visible()
        self.page.get_by_text("Handset Claim", exact=True).click()

        expect(self.page.locator("app-ess-handset-claim").get_by_text("Handset Claim", exact=True)).to_be_visible()