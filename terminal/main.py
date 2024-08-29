from calculators import temperature_calculator


class CoversorDeUnidades:
    def __init__(self) -> None:
        self.get_measure()
        self.get_convertion_units()
        self.get_unit_value()
        self.convert_temperature()

    def get_measure(self):
        while True:
            print('Selecione primeiro a medida de conversão.'
                  '\nDigite:\n    1 se: Temperatura\n    2 se: Comprimento\n'
                  '    3 se: Velocidade')
            self.measure = input()

            try:
                if self.measure == '1':
                    self.measure = 'Temperatura'
                elif self.measure == '2':
                    raise ValueError(
                        'Essa opção ainda não está disponível no momento...\n'
                    )
                elif self.measure == '3':
                    raise ValueError(
                        'Essa opção ainda não está disponível no momento...\n'
                    )
                else:
                    raise ValueError(
                        'Opção Inválida! Digite um número'
                        ' correspondente a uma medida')

                print(f"Você selecionou: {self.measure}!\n")
                return self.measure

            except ValueError as err:
                print(err)

    def get_convertion_units(self):
        while True:
            if self.measure == 'Temperatura':
                print('Selecione a unidade de origem e a unidade final:\n'
                      '1: Celsius para Fahrenheit\n'
                      '2: Celsius para Kelvin\n'
                      '3: Fahrenheit para Celsius\n'
                      '4: Fahrenheit para Kelvin\n'
                      '5: Kelvin para Celsius\n'
                      '6: Kelvin para Fahrenheit\n'
                      )

                self.client_input = input()

                units_temperature = {
                    '1': ('Celsius', 'Fahrenheit'),
                    '2': ('Celsius', 'Kelvin'),
                    '3': ('Fahrenheit', 'Celsius'),
                    '4': ('Fahrenheit', 'Kelvin'),
                    '5': ('Kelvin', 'Celsius'),
                    '6': ('Kelvin', 'Fahrenheit'),
                }

                try:
                    if self.client_input in units_temperature:
                        self.initial_unit, self.final_unit = (
                            units_temperature[self.client_input])
                    else:
                        raise ValueError('Opção inválida! Escolha'
                                         ' um número de 1 a 6.')

                    self.convertion_units = (f'{self.initial_unit}'
                                             f' para {self.final_unit}')

                    print(f'você irá converter {self.convertion_units}\n')

                    return self.convertion_units

                except ValueError as err:
                    print(err)

    def get_unit_value(self):
        print('Digite o valor para a'
              f' unidade inicial {self.initial_unit}: ')
        self.initial_unit_value = input()

    def convert_temperature(self):
        if self.measure == 'Temperatura':
            final_value = temperature_calculator(
                initial_unit_value=self.initial_unit_value,
                initial_unit=self.initial_unit,
                final_unit=self.final_unit)
        print('')
        print(final_value)


if __name__ == "__main__":
    start = CoversorDeUnidades()
