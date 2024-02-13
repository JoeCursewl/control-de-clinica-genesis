import customtkinter as ctk
from vistas.acceso import Acceso_cl


if __name__ == "__main__":
    app = ctk.CTk()
    Acceso_cl(app)
    w, h = app.winfo_screenwidth(), app.winfo_screenheight()
    x, y = (w / 2) - 200, (h / 2) - 325
    app.geometry(f"400x600+{int(x)}+{int(y)}")
    app.resizable(0,0)
    app.title("Clínica | Iniciar Sesión")
    app.mainloop()