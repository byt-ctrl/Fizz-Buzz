# WRITTEN BY OM [byt-ctrl]

def console_fizzbuzz() :
    print("\n--- Console FizzBuzz ---")
    try :
        start=int(input("Enter the starting number --> "))
        end=int(input("Enter the ending number --> "))

        for num in range(start,end+1) :
            if num%3==0 and num%5==0 :
                print("FizzBuzz")
            elif num%3==0 :
                print("Fizz")
            elif num% 5==0 :
                print("Buzz")
            else :
                print(num)

    except ValueError : 
        print("Please enter valid integers!!!! ")

# FOR GUI FizzBuzz
# ----------------------------
import tkinter as tk
from tkinter import scrolledtext

def gui_fizzbuzz() :
    def fizzbuzz_run() :
        try:
            start=int(start_entry.get())
            end=int(end_entry.get())
            output_text.delete(1.0,tk.END)

            for num in range(start,end+1):
                if num%3==0 and num%5==0 :
                    output_text.insert(tk.END,"FizzBuzz\n")
                elif num%3==0 :
                    output_text.insert(tk.END,"Fizz\n")
                elif num%5==0 :
                    output_text.insert(tk.END,"Buzz\n")
                else :
                    output_text.insert(tk.END,f"{num}\n")

        except ValueError :
            output_text.insert(tk.END,"Please enter valid integers!!!!\n")

    window=tk.Tk()
    window.title("FizzBuzz App")
    window.geometry("500x500")

    tk.Label(window,text="Start :").pack()
    start_entry=tk.Entry(window)
    start_entry.pack()

    tk.Label(window, text="End :").pack()
    end_entry=tk.Entry(window)
    end_entry.pack()

    run_button=tk.Button(window,text="Run FizzBuzz",command=fizzbuzz_run)
    run_button.pack(pady=11)

    output_text=scrolledtext.ScrolledText(window,width=41,height=16)
    output_text.pack()

    window.mainloop()


# MAIN FUNCTION TO RUN THE PROGRAM
if __name__ == "__main__":

    print("Choose Mode:\n1. Console FizzBuzz\n2. GUI FizzBuzz")
    choice=input("Enter 1 or 2 --> ")

    if choice=="1" :
        console_fizzbuzz()
    elif choice=="2":
        gui_fizzbuzz()
    else :
        print("Invalid choice . Please enter 1 or 2.")


 #END
