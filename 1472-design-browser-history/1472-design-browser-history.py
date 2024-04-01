class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr_page = homepage
        self.forwards = []
        self.backs = []

    def visit(self, url: str) -> None:
        self.backs.append(self.curr_page)
        self.curr_page = url
        self.forwards = []
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.backs:
                break
            self.forwards.append(self.curr_page)
            self.curr_page = self.backs.pop(-1)
        return self.curr_page

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.forwards:
                break
            self.backs.append(self.curr_page)
            self.curr_page = self.forwards.pop(-1)
        return self.curr_page
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)