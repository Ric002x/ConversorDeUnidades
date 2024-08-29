def temperature_calculator(initial_unit, final_unit, initial_unit_value):
    try:
        temperature_value = float(initial_unit_value)
    except ValueError:
        return 'Valor inválido!'

    # Faça a conversão de temperatura conforme as unidades selecionadas
    if initial_unit == final_unit:
        return 'Selecione unidades diferentes'

    conversions = {
        ("Celsius", "Fahrenheit"): lambda x: round((x * 9/5) + 32, 2),
        ("Celsius", "Kelvin"): lambda x: round(x + 273.15, 2),
        ("Fahrenheit", "Celsius"): lambda x: round((x - 32) * 5/9, 2),
        ("Fahrenheit", "Kelvin"): lambda x: round((x - 32) * 5/9 + 273.15, 2),
        ("Kelvin", "Celsius"): lambda x: round(x - 273.15, 2),
        ("Kelvin", "Fahrenheit"): lambda x: round((x - 273.15) * 9/5 + 32, 2),
    }

    temperature_dict = {
        "Kelvin": 'Kelvin',
        "Celsius": 'ºC',
        "Fahrenheit": 'ºF'
    }

    conversion = conversions.get((initial_unit, final_unit))
    if conversion:
        result = conversion(temperature_value)
        return (f'{temperature_value} {temperature_dict[initial_unit]} ='
                f' {result} {temperature_dict[final_unit]}')
    else:
        "Unidade não suportada"
