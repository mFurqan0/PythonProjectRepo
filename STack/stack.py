class BrowserHistory:
    def __init__(self):
        self.history = []
    
    def visit_page(self, page):
        """Add a new page to the history (push)."""
        self.history.append(page)
        print(f"Visited: {page}")
    
    def go_back(self):
        """Return to the previous page (pop)."""
        if not self.history:
            return "No pages left to go back!"
        previous_page = self.history.pop()
        print(f"Going back to: {previous_page}")
        return previous_page
    
    def show_history(self):
        """Display the current history."""
        print("Current history:", " -> ".join(self.history))

# Demo
browser = BrowserHistory()
browser.visit_page("google.com")
browser.visit_page("github.com")
browser.visit_page("deepseek.com")

print("\n--- Navigating Back ---")
browser.go_back()  # deepseek.com
browser.go_back()  # github.com
browser.show_history()  # google.comx