# System_scan
Сначала импортируем три встроенных модуля:
1.platform — для сбора сведений об ОС.
2.json — чтобы выгрузить собранные данные в файл в формате JSON.
3.shutil — в этой программе мы используем его для того, чтобы собрать сведения о диске.

Все полученные данные складываются в один словарь system_data, который разбит на три раздела: OS, Disk и Python.
В разделе OS хранятся Username, OS name, Machine type и System's version.
В разделе Disk — Total space (in GB), Used space (in GB) и Free space (in GB).
В разделе Python — Python version и Python implementation.

В конце программа записывает полученные данные в созданный ею файл system_data.json.
