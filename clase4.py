import tkinter as tk
from tkinter import messagebox

class CajeroAutomatico:
    def __init__(self, root):
        self.root = root
        self.root.title("Cajero Automático")
        self.root.geometry("400x450")
        
        # Datos iniciales
        self.saldo = 1000.0
        self.nip_correcto = "1234"
        self.intentos = 0
        self.max_intentos = 3

        # Contenedor principal
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill="both")

        self.mostrar_login()

    def limpiar_pantalla(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def mostrar_login(self):
        self.limpiar_pantalla()
        
        tk.Label(self.main_frame, text="BIENVENIDO", font=("Arial", 16, "bold")).pack(pady=20)
        tk.Label(self.main_frame, text="Ingrese su NIP:").pack()
        
        self.entry_nip = tk.Entry(self.main_frame, show="*", justify="center", font=("Arial", 14))
        self.entry_nip.pack(pady=10)
        
        tk.Button(self.main_frame, text="Entrar", command=self.verificar_nip, 
                  bg="#4CAF50", fg="white", width=15, height=2).pack(pady=20)

    def verificar_nip(self):
        nip = self.entry_nip.get()
        if nip == self.nip_correcto:
            self.mostrar_menu()
        else:
            self.intentos += 1
            intentos_restantes = self.max_intentos - self.intentos
            if self.intentos < self.max_intentos:
                messagebox.showwarning("Error", f"NIP incorrecto. Te quedan {intentos_restantes} intentos.")
            else:
                messagebox.showerror("Bloqueado", "Máximo de intentos alcanzado. Cerrando sistema.")
                self.root.destroy()

    def mostrar_menu(self):
        self.limpiar_pantalla()
        
        tk.Label(self.main_frame, text="MENÚ PRINCIPAL", font=("Arial", 14, "bold")).pack(pady=10)
        
        self.lbl_saldo = tk.Label(self.main_frame, text=f"Saldo: ${self.saldo:.2f}", font=("Arial", 12))
        self.lbl_saldo.pack(pady=10)

        # Campo para ingresar montos
        tk.Label(self.main_frame, text="Monto para Depósito/Retiro:").pack()
        self.entry_monto = tk.Entry(self.main_frame, justify="center")
        self.entry_monto.pack(pady=5)

        # Botones de acción
        tk.Button(self.main_frame, text="Depositar", width=20, command=self.depositar).pack(pady=5)
        tk.Button(self.main_frame, text="Retirar", width=20, command=self.retirar).pack(pady=5)
        tk.Button(self.main_frame, text="Consultar Saldo", width=20, command=self.consultar_saldo).pack(pady=5)
        tk.Button(self.main_frame, text="Salir", width=20, bg="#f44336", fg="white", command=self.root.destroy).pack(pady=20)

    def consultar_saldo(self):
        messagebox.showinfo("Saldo", f"Su saldo actual es: ${self.saldo:.2f}")

    def depositar(self):
        try:
            monto = float(self.entry_monto.get())
            if monto > 0:
                self.saldo += monto
                self.actualizar_interfaz(f"Depósito exitoso de ${monto:.2f}")
            else:
                messagebox.showwarning("Error", "Ingrese una cantidad válida mayor a 0.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese solo números.")

    def retirar(self):
        try:
            monto = float(self.entry_monto.get())
            if 0 < monto <= self.saldo:
                self.saldo -= monto
                self.actualizar_interfaz(f"Retiro exitoso de ${monto:.2f}")
            elif monto > self.saldo:
                messagebox.showwarning("Fondos Insuficientes", "No tienes suficiente saldo.")
            else:
                messagebox.showwarning("Error", "Ingrese una cantidad válida.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese solo números.")

    def actualizar_interfaz(self, mensaje):
        self.lbl_saldo.config(text=f"Saldo: ${self.saldo:.2f}")
        self.entry_monto.delete(0, tk.END)
        messagebox.showinfo("Operación Exitosa", mensaje)

if __name__ == "__main__":
    root = tk.Tk()
    app = CajeroAutomatico(root)
    root.mainloop()