

class ContactUsPage:
    def __init__(self, page):
        self.page = page

        def navigate(self):
            self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")

        def submit_form(self, text):
            self.page.fill("input[name='name']", "Symon")
            self.page.fill("input[name='address']", "123 Main Street")
            self.page.fill("input[name='email']", "123@gmail.com")
            self.page.fill("input[name='phone']", "9802345690")
            self.page.fill("input[name='subject']", "no subject")
            self.page.fill("[placeholder = 'Type your message here...']", "no message")
            self.page.click("text=Submit")
            self.page.wait_for_timeout(1000)





