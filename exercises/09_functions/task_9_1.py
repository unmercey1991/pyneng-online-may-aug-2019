# -*- coding: utf-8 -*-
'''
Задание 9.1

Создать функцию, которая генерирует конфигурацию для access-портов.

Функция ожидает такие аргументы:

- словарь с соответствием интерфейс-VLAN такого вида:
    {'FastEthernet0/12':10,
     'FastEthernet0/14':11,
     'FastEthernet0/16':17}
- шаблон конфигурации access-портов в виде списка команд (список access_mode_template)

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_mode_template.
В конце строк в списке не должно быть символа перевода строки.

В этом задании заготовка для функции уже сделана и надо только продолжить писать само тело функции.


Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):
[
'interface FastEthernet0/12',
'switchport mode access',
'switchport access vlan 10',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
'interface FastEthernet0/17',
'switchport mode access',
'switchport access vlan 150',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
...]

Проверить работу функции на примере словаря access_config.


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}


def gen_access_config(access_mode_template, access_config):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''
    for intf, vlan in access_config.items():
        print('interface ' + intf)
        for command in access_mode_template:
            if command.endswith('access vlan'):
                print(' {} {}'.format(command, vlan))
            else:
                print(' {}'.format(command))
gen_access_config(access_mode_template, access_config)
