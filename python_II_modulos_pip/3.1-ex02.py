import os

# 1 - Desligar o computador
#os.system('shutdown /s')  # Windows
#os.system('shutdown /s /t 60')  # Windows em 60 segundos
#os.system('shutdown -h now') # Linux

# 2 - Cancelar o desligamento
#os.system('shutdown /a')  # Windows

def turn_off_one_hour():
    os.system('shutdown /s /t 3600')  # Windows
    # os.system('shutdown -h 60')  # Linux

def turn_off_half_an_hour(minutes):
    os.system(f'shutdown /s /t 1800')  # Windows
    # os.system(f'shutdown -h {minutes}')  # Linux

def cancel_shutdown():
    os.system('shutdown /a')  # Windows
    # os.system('shutdown -c')  # Linux

#turn_off_one_hour()
#cancel_shutdown()
#turn_off_half_an_hour()
cancel_shutdown()
