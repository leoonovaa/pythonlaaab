import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
import json
import os

FILE_NAME = "events.json"

def load_events():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f: 
            return json.load(f)
    return {}

def save_events(events):
    with open(FILE_NAME, "w") as f:
        json.dump(events, f)

class EventPlannerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Planner")
        self.geometry("400x400")
        
        self.events = load_events()
        
        self.cal = Calendar(self, selectmode="day", date_pattern="yyyy-mm-dd" , showweeknumbers=False)
        self.cal.pack(pady=20)
        
        self.add_event_btn = tk.Button(self, text="Add event", command=self.open_add_event_window)
        self.add_event_btn.pack(pady=5)
        
        self.view_event_btn = tk.Button(self, text="See events", command=self.open_view_events_window)
        self.view_event_btn.pack(pady=5)
        
        self.quit_btn = tk.Button(self, text="Exit", command=self.quit)
        self.quit_btn.pack(pady=5)
        
    def open_add_event_window(self):
        AddEventWindow(self)
        
    def open_view_events_window(self):
        selected_date = self.cal.get_date()
        if selected_date in self.events:
            ViewEventsWindow(self, selected_date, self.events[selected_date])
        else:
            messagebox.showinfo("Events", "No events on this date")

class AddEventWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add event")
        self.geometry("300x300")
        
        self.name_label = tk.Label(self, text="Event name")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)
        
        self.start_date_label = tk.Label(self, text="Date of start")
        self.start_date_label.pack(pady=5)
        self.start_date_entry = DateEntry(self, date_pattern="yyyy-mm-dd")
        self.start_date_entry.pack(pady=5)
        
        self.end_date_label = tk.Label(self, text="Day of end")
        self.end_date_label.pack(pady=5)
        self.end_date_entry = DateEntry(self, date_pattern="yyyy-mm-dd")
        self.end_date_entry.pack(pady=5)
        
        self.desc_label = tk.Label(self, text="Description")
        self.desc_label.pack(pady=5)
        self.desc_entry = tk.Text(self, height=5)
        self.desc_entry.pack(pady=5)
        

        self.save_btn = tk.Button(self, text="Save", command=self.save_event)
        self.save_btn.pack(pady=5)
        self.cancel_btn = tk.Button(self, text="Cancel", command=self.destroy)
        self.cancel_btn.pack(pady=5)
    
    def save_event(self):
        event_name = self.name_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        description = self.desc_entry.get("1.0", tk.END).strip()
        
        if not event_name:
            messagebox.showerror("Error", "Name cannnot be empty.")
            return
        
        events = self.master.events
        if start_date not in events:
            events[start_date] = []
        events[start_date].append({
            "name": event_name,
            "start": start_date,
            "end": end_date,
            "description": description
        })
        save_events(events)
        
        messagebox.showinfo("!", "Event added")
        self.destroy()

class ViewEventsWindow(tk.Toplevel):
    def __init__(self, parent, date, events):
        super().__init__(parent)
        self.title(f"Events on {date}")
        self.geometry("400x300")
        
        self.events = events
        self.date = date
        
        self.events_list = ttk.Treeview(self, columns=("name", "start", "end"), show="headings")
        self.events_list.heading("name", text="Name")
        self.events_list.heading("start", text="Start")
        self.events_list.heading("end", text="End")
        
        for event in events:
            self.events_list.insert("", "end", values=(event["name"], event["start"], event["end"]))
        
        self.events_list.pack(pady=10)
        
        self.close_btn = tk.Button(self, text="Exit", command=self.destroy)
        self.close_btn.pack(pady=10)

if __name__ == "__main__":
    app = EventPlannerApp()
    app.mainloop()
