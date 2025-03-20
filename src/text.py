"""Texts for bot answers and keyboards."""

greet = 'Добрый день! Добавьте новые веб-сайты для парсера.'
menu = 'Главное меню'
request_user_upload_file = ('Загрузите файл Excel в формате «XLSX», '
                            'чтобы добавить новые ресурсы для парсера.')

add_resources_start_message = ('Эти веб-сайты успешно добавлены в '
                               'источники парсера:\n\n')
added_resouce = ('{index}) {title} — {url} — {xpath}\n')

all_resources_invalid_message = (
    'Все ресурсы переданы в невалидном формате.\n'
    '\nУбедитесь, что файл содержит таблицу из трех полей:\n'
    '  A. title (Название)\n'
    '  B. url (Ссылка на источник)\n'
    '  C. xpath (Путь к элементу с ценой)\n'
)
