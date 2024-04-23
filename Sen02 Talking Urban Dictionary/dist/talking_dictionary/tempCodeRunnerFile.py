            textArea.config(state=DISABLED)

        else:
            textArea.delete(1.0, END)
            messagebox.showinfo('Information', 'Please type a correct word.')
            enterWordEntry.delete(0, END)

    else:
        messagebox.showerror('Error', 'The word does not exist. Please double check it.')
        enterWordEntry.delete(0, END)