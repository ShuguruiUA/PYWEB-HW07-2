# CLI bot for PostgreSQL DB manipulating

## Steps
1. Run your docker or connect to yours PostgreSQL and create a new DB - DEV
2. Init alembic and make changes in its configuration (dev.py)
3. Run seed.py to generate random data in the DB tables
4. Run from console CRUD_CLI.py using arguments to manipulate data in DB 
5. tables groups and students has relationship if you delete a group students are gone...
## Example
```commandline
   $ python3 CRUD_CLI.py -h or --help
```
options:
```commandline
  -h, --help            show this help message and exit
  -a {create,list,update,remove}, --action {create,list,update,remove}
                        Дія для виконання: create, list, update, remove
  -m {Teacher,Group,Grade,Student,Subject}, --model {Teacher,Group,Grade,Student,Subject}
                        Модель, над якою виконується операція
  -id RECORD_ID, --record_id RECORD_ID
                        Ключ запису для оновлення або видалення в БД
  -n NAME, --name NAME  Значення для створення імені, оцінки або оновлення запису

```