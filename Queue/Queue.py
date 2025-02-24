from collections import deque

class PrintQueue:
    def __init__(self):
        self.queue = deque()
    
    def add_job(self, document):
        """Add a print job to the queue (enqueue)."""
        self.queue.append(document)
        print(f"Added to queue: {document}")
    
    def process_job(self):
        """Print the next document in the queue (dequeue)."""
        if not self.queue:
            return "No jobs in the queue!"
        document = self.queue.popleft()
        print(f"Printing: {document}")
        return document
    
    def show_queue(self):
        """Display pending print jobs."""
        print("Pending jobs:", list(self.queue))

# Demo
printer = PrintQueue()
printer.add_job("Resume.pdf")
printer.add_job("Report.docx")
printer.add_job("Invoice.xlsx")

print("\n--- Processing Jobs ---")
printer.process_job()  # Resume.pdf
printer.process_job()  # Report.docx
printer.show_queue()   # ['Invoice.xlsx']