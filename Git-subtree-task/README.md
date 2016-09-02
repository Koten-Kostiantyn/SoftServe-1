# git subtree add  
Скрипт пока что работает только с полным путем к файлу и с целочисельными тегами.  
  
использование: ./gits.py гит/репозиторий1 гит/репозиторий2  
  
алгоритм:  
1 идет проверка директорий, есть ли там репозитории  
2 выполняем команду git subtree add  
3 проверяем есть ли теги в 2м репозитории, если не то проверяем теги в 1м репозитории, если нет ставим тег 1  

now everything working fine, script fully support branches:
if only master avaliable it will copy its name, if there more than 1 branches it will copy them with adding "_bracnh" to repo
