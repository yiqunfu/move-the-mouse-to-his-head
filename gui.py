import threading
import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
from main import run_detection_loop, stop_detection_loop


class ControlGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Move the Mouse to His Head")
        self.geometry("320x180")
        self.resizable(False, False)

        self.status_var = tk.StringVar(value="Idle")
        self._setup_widgets()

    def _setup_widgets(self):
        padding = {"padx": 10, "pady": 8}

        ttk.Label(self, text="Head Lock Controller").pack(**padding)
        ttk.Label(self, textvariable=self.status_var).pack(**padding)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=8)

        self.start_btn = ttk.Button(btn_frame, text="Start", command=self.start)
        self.stop_btn = ttk.Button(btn_frame, text="Stop", command=self.stop, state=tk.DISABLED)

        self.start_btn.grid(row=0, column=0, padx=6)
        self.stop_btn.grid(row=0, column=1, padx=6)

        ttk.Button(self, text="Exit", command=self.on_exit).pack(**padding)

    def start(self):
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.status_var.set("Running...")
        threading.Thread(target=self._run_loop_safe, daemon=True).start()

    def _run_loop_safe(self):
        try:
            run_detection_loop()
        except Exception as exc:
            self.status_var.set("Error")
            messagebox.showerror("Error", str(exc))
            self.stop_btn.config(state=tk.DISABLED)
            self.start_btn.config(state=tk.NORMAL)

    def stop(self):
        stop_detection_loop()
        self.status_var.set("Stopped")
        self.stop_btn.config(state=tk.DISABLED)
        self.start_btn.config(state=tk.NORMAL)

    def on_exit(self):
        self.stop()
        self.destroy()


def main():
    pyautogui.FAILSAFE = False
    app = ControlGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
