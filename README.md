# System_scan
 Сначала импортируем 3 встроенных модуля:
 1.Platform - для сбора сведений об ОС.
 2.Json - чтобы выгрузить собранные данные в файл в формате json.
 3.Shutil - именно в этой программе мы используем его для того, чтобы собрать сведения об диске.

Все полученные данные складываются в один словарь system_data, который разбит на три раздела: OS, Disk и Python.
В разделе OS хранятся Username, OS name, Machine type и System's version.
В разделе Disk — Total space(in GB), Used space(in GB) и Free space(in GB).
В разделе Python — Python version и Python implementation.

В конце программа программа переписывает полученные данные в созданный ею файл system_data
