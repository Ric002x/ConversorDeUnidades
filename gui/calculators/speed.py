def speed_calculator(initial_unit, final_unit, initial_unit_value):
    try:
        speed_value = float(initial_unit_value)
    except ValueError:
        return 'Valor inválido!'

    if initial_unit == final_unit:
        return 'Selecione unidades diferentes'

    conversions = {
        "Metros por segundo": {
            'Quilômetros por hora': 3.6,
            'Milhas por segundo': 0.000621371,
            'Milhas por hora': 2.23694,
        },
        "Quilômetros por hora": {
            'Metros por segundo': 0.277778,
            'Milhas por segundo': 0.000172603,
            'Milhas por hora': 0.621371,
        },
        'Milhas por segundo': {
            'Quilômetros por hora': 5793.64,
            'Metros por segundo': 1609.34,
            'Milhas por hora': 3600,
        },
        'Milhas por hora': {
            'Metros por segundo': 0.44704,
            'Quilômetros por hora': 1.60934,
            'Milhas por segundo': 0.000277778
        },
    }

    speed_dict = {
        'Metros por segundo': 'm/s',
        'Quilômetros por hora': 'km/h',
        'Milhas por segundo': 'mi/s',
        'Milhas por hora': 'mi/h',
    }

    if initial_unit in conversions and final_unit in conversions[initial_unit]:
        result = round(speed_value * conversions[initial_unit][final_unit], 5)
        return (f'{speed_value} {speed_dict[initial_unit]} ='
                f' {result} {speed_dict[final_unit]}')
    else:
        return 'Unidade não suportada'
