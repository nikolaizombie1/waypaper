"""Перевод на русский язык интерфейса программы"""

MSG_DESC = "Графический интерфейс для установки обоев на Wayland и X11. Работает как фронтенд для feh, swaybg, wallutils и swww."
MSG_INFO = "Для получения дополнительной информации посетите:\nhttps://github.com/anufrievroman/waypaper"

MSG_ARG_HELP = "вывести версию программы"
MSG_ARG_FILL = "указать, как заполнить экран выбранным изображением"
MSG_ARG_REST = "восстановить последние обои"
MSG_ARG_BACK = "указать бэкенд для установки обоев"
MSG_ARG_RAND = "установить случайные обои"

MSG_PATH = "Выбранный путь к изображению:"
MSG_SELECT = "Выбрать"
MSG_REFRESH = "Обновить"
MSG_RANDOM = "Случайно"
MSG_EXIT = "Выход"
MSG_SUBFOLDERS = "Подпапки"
MSG_CHANGEFOLDER = "Изменить папку с обоями"
MSG_CHOOSEFOLDER = "Пожалуйста, выберите папку"
MSG_CACHING = "Кэширование обоев..."
MSG_SETWITH = "Отправлена команда на установку обоев с использованием"

MSG_HELP = "Горячие клавиши Waypaper:\n\nhjkl - Навигация (←↓↑→)\nf - Изменить папку с обоями\n"
MSG_HELP += "g - Прокрутка в начало\nG - Прокрутка в конец\nR - Установить случайные обои\nr - Обновить кэш обоев\n"
MSG_HELP += "s - Включить/отключить изображения в подпапках\n? - Справка\nq - Выход\n\n"
MSG_HELP += MSG_INFO

ERR_CACHE = "Ошибка при удалении кэша"
ERR_BACKEND = "Похоже, что ни один из бэкендов для установки обоев не установлен в системе.\n"
ERR_BACKEND += "Используйте менеджер пакетов для установки хотя бы одного из этих бэкендов:\n\n"
ERR_BACKEND += "- swaybg (для Wayland)\n- swww (для Wayland)\n"
ERR_BACKEND += "- feh (для Xorg)\n- wallutils (для Xorg и Wayland)\n\n"
ERR_BACKEND += MSG_INFO
ERR_WALL = "Ошибка при смене обоев:"
ERR_NOTSUP = "Бэкенд не поддерживается:"
ERR_DISP = "Ошибка определения названий мониторов:"
ERR_KILL = "Предупреждение связанное с killall:"

TIP_SUBFOLDER = "Включить/отключить изображения в подпапках"
TIP_REFRESH = "Обновить папку с изображениями"
TIP_FILL = "Выбрать тип заполнения"
TIP_BACKEND = "Выбрать бэкенд"
TIP_SORTING = "Выбрать тип сортировки"
TIP_DISPLAY = "Выбрать дисплей"
TIP_COLOR = "Выбрать цвет фона"
TIP_RANDOM = "Установить случайные обои"
TIP_EXIT = "Выйти из приложения"