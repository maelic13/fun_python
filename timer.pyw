import datetime
from os.path import isfile
from tkinter import Button, Label, Tk


class TimerHelper:
    def __init__(self, filename="timestamp"):
        self.root = Tk()
        self.label = Label(
            self.root, font=('calibri', 40, 'bold'),
            background='darkgrey', foreground='black')
        self.label.pack(anchor='center', padx=20, pady=20)
        self.button = Button(self.root, text='RESET', font=('calibri', 20, 'bold'), bg="darkgrey",
                             command=self._write_current_date_and_time)
        self.button.pack()
        self._filename = filename + ".txt"

    def time(self):
        string = str(self._get_elapsed_time()).split(".")[0]
        self._color_text(self.label)
        self.label.configure(text=string)
        self.label.after(1000, self.time)

    def run_timer(self):
        self.root.title('Timer')
        self.root.minsize(300, 200)
        self.root.configure(bg='darkgrey')
        self.button.configure(height=1, width=12)

        self.time()
        self.root.mainloop()

    def _get_elapsed_time(self):
        if not isfile(self._filename):
            self._write_current_date_and_time()
        with open(self._filename) as file:
            loaded = datetime.datetime.strptime(file.readline(), "%Y-%m-%d %H:%M:%S")
            return datetime.datetime.now() - loaded

    def _write_current_date_and_time(self):
        with open(self._filename, 'w') as file:
            file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def _color_text(self, label):
        elapsed_time = self._get_elapsed_time()
        if elapsed_time < datetime.timedelta(days=3):
            label.configure(fg="darkred")
        elif datetime.timedelta(days=3) <= elapsed_time < datetime.timedelta(days=14):
            label.configure(fg="black")
        elif datetime.timedelta(days=14) <= elapsed_time < datetime.timedelta(days=31):
            label.configure(fg="darkgreen")
        elif datetime.timedelta(days=31) < elapsed_time:
            label.configure(fg="darkblue")


if __name__ == "__main__":
    TimerHelper("last_time").run_timer()
