from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    def generate_report(self):
        self.fetch_data()
        self.process_data()
        self.formate_data()
        self.save_report()
    
    @abstractmethod
    def fetch_data(self):
        pass
    @abstractmethod
    def process_data(self):
        pass
    @abstractmethod
    def formate_data(self):
        pass
    @abstractmethod
    def save_report(self):
        pass


class PDFReport(ReportGenerator):
    def fetch_data(self):
        print("📥 Fetching data from database for PDF report.")

    def process_data(self):
        print("🔄 Processing data for PDF report.")

    def formate_data(self):
        print("📝 Formatting report as PDF.")

    def save_report(self):
        print("💾 Saving report as PDF file.")

class CSVReport(ReportGenerator):
    def fetch_data(self):
        print("📥 Fetching data from database for CSV report.")

    def process_data(self):
        print("🔄 Processing data for CSV report.")

    def formate_data(self):
        print("📝 Formatting report as CSV.")

    def save_report(self):
        print("💾 Saving report as CSV file.")

pdf_report = PDFReport()
pdf_report.generate_report()
