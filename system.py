import platform


system_stat=[

   	
    platform.system(),
    platform._sys_version(),
    platform.version(),
    platform.python_compiler(),
    platform.machine(),
    platform.python_version(),
    platform.node(),

]


for system in system_stat:
    print(system)
