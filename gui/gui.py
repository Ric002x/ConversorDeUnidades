import customtkinter as ctk
from calculators import (temperature_calculator,
                         speed_calculator, length_calculator)


# Configurar janela principal
class ConversorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('450x450')

        # Input Measure Frame And Label
        self.input_label = ctk.CTkLabel(
            self.root, text="Selecione a medida para conversão:",
            font=("Roboto", 18))
        self.input_label.pack_configure(anchor='center', pady=(15, 0))
        self.input_measure_frame = ctk.CTkFrame(
            self.root, width=400, height=50
        )
        self.input_measure_frame.pack_configure(anchor='center', pady=(15, 15))

        # Input Measure
        self.measures = ['Temperatura', 'Comprimento', 'Velocidade']
        self.var_measure = ctk.StringVar()
        self.input_measure = ctk.CTkOptionMenu(
            self.input_measure_frame, values=self.measures,
            variable=self.var_measure, command=self.layout_update)
        self.input_measure.pack_configure(anchor='center')
        self.var_measure.set(self.measures[0])

        # Output Label
        self.output_label = ctk.CTkLabel(
            self.root, fg_color='gray', width=400, height=50, text='Resultado',
            corner_radius=5, font=("Roboto", 16))
        self.output_label.pack_configure(anchor='center', pady=(10, 0))

        # Input Units Frame And Label
        self.input_units_label = ctk.CTkLabel(
            self.root, text="Selecione as variáveis para conversão",
            font=('Roboto', 18)
        )
        self.input_units_label.pack_configure(anchor='center', pady=(15, 0))
        self.input_units_frame = ctk.CTkFrame(
            self.root, width=400, height=100, fg_color='transparent',
        )
        self.input_units_frame.pack_configure(anchor='center', pady=(15, 0))

        # Input Entry Frame And Label
        self.input_entry_label = ctk.CTkLabel(
            self.root, text="Digite o valor a ser convertido",
            font=('Roboto', 18)
        )
        self.input_entry_label.pack_configure(anchor='center', pady=(15, 0))

        self.input_entry_frame = ctk.CTkFrame(
            self.root, width=400, height=50, fg_color='transparent'
        )
        self.input_entry_frame.pack_configure(anchor='center', pady=(15, 0))

        self.var_entry = ctk.StringVar()
        self.entry_input = ctk.CTkEntry(
            self.input_entry_frame, textvariable=self.var_entry,
            width=200)
        self.entry_input.pack_configure(anchor='center')

        self.button_enter = ctk.CTkButton(
            self.root, text='Converter', font=('Roboto', 14),
            command=self.calculate_result)
        self.button_enter.pack_configure(anchor='center', pady=(15, 0))

        self.layout_update()

    def layout_update(self, *args):
        for widget in self.input_units_frame.winfo_children():
            widget.destroy()

        if self.var_measure.get() == 'Temperatura':
            self.temperature_widgets()
        elif self.var_measure.get() == 'Comprimento':
            self.lenght_widgets()
        elif self.var_measure.get() == 'Velocidade':
            self.speed_widgets()

    def temperature_widgets(self):
        units = ['Celsius', 'Fahrenheit', 'Kelvin']

        self.var_unit_initial = ctk.StringVar()
        self.unit_inital = ctk.CTkOptionMenu(
            self.input_units_frame, values=units,
            variable=self.var_unit_initial
        )
        self.unit_inital.pack_configure(anchor='center', pady=(15, 0))
        self.var_unit_initial.set(units[0])

        self.var_unit_final = ctk.StringVar()
        self.unit_final = ctk.CTkOptionMenu(
            self.input_units_frame, values=units,
            variable=self.var_unit_final
        )
        self.unit_final.pack_configure(anchor='center', pady=(15, 0))
        self.var_unit_final.set(units[1])

    def lenght_widgets(self):
        units = ['Centímetros', 'Metros', 'Quilômetros', 'Pés',
                 'Polegadas', 'Milhas', 'Jardas']

        self.var_unit_initial = ctk.StringVar()
        self.unit_inital = ctk.CTkOptionMenu(
            self.input_units_frame, values=units,
            variable=self.var_unit_initial
        )
        self.unit_inital.pack_configure(anchor='center', pady=(15, 0))
        self.var_unit_initial.set(units[0])

        self.var_unit_final = ctk.StringVar()
        self.unit_final = ctk.CTkOptionMenu(
            self.input_units_frame, values=units,
            variable=self.var_unit_final
        )
        self.unit_final.pack_configure(anchor='center', pady=(15, 0))
        self.var_unit_final.set(units[1])

    def speed_widgets(self):
        units = ['Metros por segundo', 'Quilômetros por hora',
                 'Milhas por segundo', 'Milhas por hora']

        self.var_unit_initial = ctk.StringVar()
        self.unit_inital = ctk.CTkOptionMenu(
            self.input_units_frame, values=units,
            variable=self.var_unit_initial
        )
        self.unit_inital.pack_configure(anchor='center', pady=(15, 0))
        self.var_unit_initial.set(units[0])

        self.var_unit_final = ctk.StringVar()
        self.unit_final = ctk.CTkOptionMenu(
            self.input_units_frame, values=units,
            variable=self.var_unit_final
        )
        self.unit_final.pack_configure(anchor='center', pady=(15, 0))
        self.var_unit_final.set(units[1])

    def calculate_result(self, *args):
        initial_unit = self.var_unit_initial.get()
        final_unit = self.var_unit_final.get()
        value = self.var_entry.get()

        if self.var_measure.get() == 'Temperatura':
            result = temperature_calculator(initial_unit, final_unit, value)
            self.output_label.configure(text=result)
        elif self.var_measure.get() == 'Velocidade':
            result = speed_calculator(initial_unit, final_unit, value)
            self.output_label.configure(text=result)
        elif self.var_measure.get() == "Comprimento":
            result = length_calculator(initial_unit, final_unit, value)
            self.output_label.configure(text=result)


if __name__ == '__main__':
    root = ctk.CTk()
    root.resizable(False, False)
    app = ConversorApp(root)
    root.mainloop()
