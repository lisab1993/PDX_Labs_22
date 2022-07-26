
# Version 1
# ft_input = int(input('What is the distance in feet? '))
# meters = round(ft_input * 0.3048, 4)

# print(f'{ft_input}\' is {meters} m')

# Version 2

from dis import dis


to_meters = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
}


distance = int(input('What is the distance?  ').strip())
unit = input(
    'What unit is this distance? (ft, mi, m, km, yd, in)  ').lower().strip()
convert_to = input(
    'What unit would you like to convert to? (ft, mi, m, km, yd, in)  ').lower().strip()

# convert the distance to meters
meter_conversion = round(distance * to_meters[unit], 4)
any_unit_conversion = round(meter_conversion/to_meters[convert_to], 7)
print(f'{distance} {unit} is {any_unit_conversion} {convert_to}.')
