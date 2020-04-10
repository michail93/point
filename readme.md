### Разворачивание и запуск приложения
* из директории в которой раходится manage.py запустите команду
```
bash start_app.sh
```

### Обращения к api

#### Работоспособность сервиса
* Метод GET на url /api/ping/

#### Пополнение баланса
* Метод POST на url /api/add/ с json вида: 
```
{
	"uuid": "<uuid>",
	"amount": <int/float>
}
```
"uuid" - uuid пользователя

"amount" - сумма

#### Уменьшение баланса
* Метод POST на url /api/substract/ с json вида: 
```
{
	"uuid": "<uuid>",
	"amount": <int/float>
}
```
"uuid" - uuid пользователя

"amount" - сумма

#### Статус-остаток по счету
* Метод POST на url /api/status/ с json вида:
```
{
	"uuid": "<uuid>"
}
```
"uuid" - uuid пользователя
