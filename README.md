# notes-api
1) Запус сервиса - **docker-compose up -d** (работает на localhost)
2) Запуск контейнера с тестами - **docker-compose -f docker-compose.tests.yml up -d**

# API
| Описание                      | Метод          | Ресурс                                                         |
| :---                          |     :---:      | :---                                                           |
| Получить все заметки          | `GET`          |/api/v1/notes                                                   |
| Создать заметку               | `POST`         |/api/v1/notes/create                                            |
| Получить определенную заметку | `GET`          |/api/v1/notes/{note_id}                                         |
| Пометить как выполненное      | `PATCH`        |/api/v1/notes/{note_id}/complete                                |
| Удалить заметкуу              | `DELETE`       |/api/v1/notes/{note_id}/delete                                  |
