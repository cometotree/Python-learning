import tkinter as tk

class CalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        
        # 输入框和标签
        self.input1_label = tk.Label(self.root, text="Input 1:")
        self.input1_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.input1_entry = tk.Entry(self.root, width=20)
        self.input1_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.input2_label = tk.Label(self.root, text="Input 2:")
        self.input2_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.input2_entry = tk.Entry(self.root, width=20)
        self.input2_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.result_entry = tk.Entry(self.root, width=20)
        self.result_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # 计算按钮
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        self.root.mainloop()
        
    def calculate(self):
        try:
            input1 = float(self.input1_entry.get())
            input2 = float(self.input2_entry.get())
            result = input1 * input2
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, str(result))
        except ValueError:
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Invalid input")

if __name__ == "__main__":
    calc = CalculatorGUI()
