import customtkinter as ctk


class TaxCalculator:
    def __init__(self):
        # Initialize our window
        self.window = ctk.CTk()
        self.window.title('Tax Calculator')
        self.window.geometry('560x140') # dimension of the window
        self.window.resizable(False, False)

        # Widget padding
        self.padding: dict = {'padx': 20, 'pady': 10}

        # Income label and entry
        self.income_label = ctk.CTkLabel(self.window, text='Income:')
        self.income_label.grid(row=0, column=0, **self.padding)  # **self.padding, same as saying 'padx': 20, 'pady': 10
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Tax label and entry
        self.tax_rate_label = ctk.CTkLabel(self.window, text='Percent:')
        self.tax_rate_label.grid(row=0, column=3, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=0, column=4, **self.padding)
    
        # Result label and entry
        self.result_label = ctk.CTkLabel(self.window, text='Tax:')
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, '0')
        self.result_entry.grid(row=2, column=1, **self.padding)

        # Calculate button
        self.calculate_button = ctk.CTkButton(self.window, text='Calculate', command=self.calculate_tax, width=160, height=40)
        self.calculate_button.grid(row=2, column=3, **self.padding, columnspan=2)
    

    def update_result(self, text: str):
        """Updates the result of the tax field."""

        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        """Calculates the total tax based on the percent."""

        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())
            self.update_result(f'€{income * (tax_rate / 100):,.2f}')
        except ValueError:
            self.update_result('Invalid input')

    def run(self):
        """Runs the tkinter app."""

        self.window.mainloop()


if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()
