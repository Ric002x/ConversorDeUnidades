def length_calculator(initial_unit, final_unit, initial_unit_value):
    try:
        length_value = float(initial_unit_value)
    except ValueError:
        return 'Valor inválido!'

    if initial_unit == final_unit:
        return 'Selecione unidades diferentes'

    # Dicionário de conversões
    conversions = {
        'Centímetros': {
            'Metros': 0.01,
            'Pés': 0.0328084,
            'Polegadas': 0.393701,
            'Milhas': 0.0000062137,
            'Jardas': 0.0109361,
            'Quilômetros': 0.00001,
        },
        'Metros': {
            'Centímetros': 100,
            'Pés': 3.28084,
            'Polegadas': 39.3701,
            'Milhas': 0.000621371,
            'Jardas': 1.09361,
            'Quilômetros': 0.001,
        },
        'Pés': {
            'Centímetros': 30.48,
            'Metros': 0.3048,
            'Polegadas': 12,
            'Milhas': 0.000189394,
            'Jardas': 0.333333,
            'Quilômetros': 0.0003048,
        },
        'Polegadas': {
            'Centímetros': 2.54,
            'Metros': 0.0254,
            'Pés': 0.0833333,
            'Milhas': 0.0000157828,
            'Jardas': 0.0277778,
            'Quilômetros': 0.0000254,
        },
        'Milhas': {
            'Centímetros': 160934,
            'Metros': 1609.34,
            'Pés': 5280,
            'Polegadas': 63360,
            'Jardas': 1760,
            'Quilômetros': 1.60934,
        },
        'Jardas': {
            'Centímetros': 91.44,
            'Metros': 0.9144,
            'Pés': 3,
            'Polegadas': 36,
            'Milhas': 0.000568182,
            'Quilômetros': 0.0009144,
        },
        'Quilômetros': {
            'Centímetros': 100000,
            'Metros': 1000,
            'Pés': 3280.84,
            'Polegadas': 39370.1,
            'Milhas': 0.621371,
            'Jardas': 1093.61,
        },
    }

    length_dict = {
        'Quilômetros': 'km',
        'Metros': 'm',
        'Centímetros': 'cm',
        'Jardas': 'yd',
        'Pés': 'ft',
        'Milhas': 'mi',
        'Polegadas': 'in',
    }
    # Calcula a conversão
    if initial_unit in conversions and final_unit in conversions[initial_unit]:
        result = round(length_value * conversions[initial_unit][final_unit], 5)
        return (f'{length_value} {length_dict[initial_unit]}'
                f' = {result} {length_dict[final_unit]}')
    else:
        return 'Unidade não suportada'
