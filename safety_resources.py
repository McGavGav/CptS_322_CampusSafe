import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

class CampusSafeResourcesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Campus Safe - Safety Resources")

        self.create_resources_tab()

    def create_resources_tab(self):
        self.resources_frame = ttk.Frame(self.root, padding="10")
        self.resources_frame.pack(fill=tk.BOTH, expand=True)

        self.resources_text = tk.Text(self.resources_frame, wrap=tk.WORD, height=20, width=60)
        self.resources_text.pack(pady=10)

        # Safety resources 
        self.resources_text.insert(tk.END, "Campus Safety Resources\n\n")
        self.resources_text.insert(tk.END, "Emergency Services (911):\n")
        self.resources_text.insert(tk.END, "For immediate emergencies, dial 911.\n\n")

        self.resources_text.insert(tk.END, "Campus Security:\n")
        self.resources_text.insert(tk.END, "Phone: 509-335-8548\n")
        self.resources_text.insert(tk.END, "Website: Campus Security Website\n\n")

        self.resources_text.insert(tk.END, "Student Health Services:\n")
        self.resources_text.insert(tk.END, "Phone: 509-335-3575\n")
        self.resources_text.insert(tk.END, "Website: Student Health Website\n\n")

        self.resources_text.insert(tk.END, "Counseling Services:\n")
        self.resources_text.insert(tk.END, "Phone: 509-335-4511\n")
        self.resources_text.insert(tk.END, "Website: Counseling Services Website\n\n")

        self.resources_text.config(state=tk.DISABLED) 

        # Add clickable links
        self.add_link_tags()

    def add_link_tags(self):
        links = {
            "Campus Security Website": "https://police.wsu.edu/contact-us/",
            "Student Health Website": "https://cougarhealth.wsu.edu/home/",
            "Counseling Services Website": "https://cougarhealth.wsu.edu/individual-counseling/"
        }
        for text, url in links.items():
            self.add_link_tag(url, text)

    def add_link_tag(self, url, link_text):
        start_index = self.resources_text.search(link_text, "1.0", tk.END)
        if start_index:
            end_index = f"{start_index}+{len(link_text)}c"
            tag_name = f"link_{link_text.replace(' ', '_')}"  # Unique tag per link
            self.resources_text.tag_add(tag_name, start_index, end_index)
            self.resources_text.tag_config(tag_name, foreground="blue", underline=True)
            self.resources_text.tag_bind(tag_name, "<Button-1>", lambda event, u=url: self.open_link(u))

    def open_link(self, url):
        webbrowser.open_new(url)

def main():
    root = tk.Tk()
    app = CampusSafeResourcesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
