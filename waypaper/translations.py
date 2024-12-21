"""
Module with translations into various languages.
To add a new language, add a new class, and update the load_language() function.
"""


class English:
    def __init__(self):
        self.msg_desc = "GUI wallpaper setter for Wayland and X11. It works as a frontend for feh, swaybg, wallutils, hyprpaper, mpvpaper, and swww."
        self.msg_info = "For more information, visit:\nhttps://github.com/anufrievroman/waypaper"

        self.msg_arg_help = "print version of the program"
        self.msg_arg_fill = "specify how to fill the screen with chosen image"
        self.msg_arg_rest = "restore last wallpaper"
        self.msg_arg_back = "specify which backend to use to set wallpaper"
        self.msg_arg_rand = "set a random wallpaper"
        self.msg_arg_list = "list wallpapers in json to standard out"
        self.msg_arg_wall = "set the specified wallpaper"
        self.msg_arg_folder = "specify which folder to scan for wallpapers"
        self.msg_arg_statefile = "specify a custom file to store the application state"
        self.msg_arg_monitor = "specify desired monitor using its name"
        self.msg_arg_post = "prevents ruuning post_command"

        self.msg_path = "Selected image path:"
        self.msg_select = "Select"
        self.msg_refresh = "Refresh"
        self.msg_clear = "Clear"
        self.msg_stop = "Stop"
        self.msg_pause = "Pause"
        self.msg_search = "Search"
        self.msg_random = "Random"
        self.msg_exit = "Exit"
        self.msg_options = "Options"
        self.msg_subfolders = "Show subfolders"
        self.msg_recursive = "Recursive Search"
        self.msg_hidden = "Show hidden"
        self.msg_gifs = "Show gifs only"
        self.msg_transitions = "Show transition options"
        self.msg_changefolder = "Folder"
        self.msg_choosefolder = "Please choose a folder"
        self.msg_caching = "Caching wallpapers..."

        self.msg_help = "Waypaper's hotkeys:\n\nhjkl - Navigation (←↓↑→)\nEnter - Set selected wallpaper\nf - Change wallpaper folder\n"
        self.msg_help += "g - Scroll to top\nG - Scroll to bottom\nR - Set random wallpaper\nr - Recache wallpapers\n"
        self.msg_help += ". - Toggle hidden images\ns - Toggle images in subfolders\n? - Help\nq - Exit\n\n"
        self.msg_help += self.msg_info

        self.err_cache = "Error deleting cache"
        self.err_backend = "Looks like none of the wallpaper backends is installed in the system.\n"
        self.err_backend += "Use your package manager to install at least one of these backends:\n\n"
        self.err_backend += "- swaybg (Wayland)\n- swww (Wayland)\n"
        self.err_backend += "- hyprpaper (Wayland)\n- feh (Xorg)\n"
        self.err_backend += "- wallutils (Xorg & Wayland)\n- mpvpaper (Xorg & Wayland)\n\n"
        self.err_backend += self.msg_info

        self.tip_refresh = "Recache the folder of images"
        self.tip_fill = "Choose fill type"
        self.tip_backend = "Choose backend"
        self.tip_sorting = "Choose sorting type"
        self.tip_display = "Choose display"
        self.tip_color = "Choose background color"
        self.tip_random = "Set random wallpaper"
        self.tip_exit = "Exit the application"
        self.tip_transition = "Choose transition type"
        self.tip_mpv_stop = "Stop all mpv processes"
        self.tip_mpv_pause = "Play/Pause video wallpaper"


class German:
    def __init__(self):
        self.msg_desc = "Grafisches Hintergrundbild-Auswahlwerkzeug für Wayland und X11. Es dient als Frontend für feh, swaybg, wallutils, hyprpaper, mpvpaper, und swww."
        self.msg_info = "Weitere Informationen finden Sie unter:\nhttps://github.com/anufrievroman/waypaper"

        self.msg_arg_help = "gibt die Programmversion aus"
        self.msg_arg_fill = "legt fest, wie das Bild skaliert werden soll, um den gesamten Bildschirm auszufüllen"
        self.msg_arg_rest = "stellt das zuletzt verwendete Hintergrundbild wieder her"
        self.msg_arg_back = "legt das Backend fest, welches zum Setzen des Hintergrundbildes verwendet werden soll"
        self.msg_arg_rand = "wählt ein zufälliges Hintergrundbild aus"
        self.msg_arg_list = "list wallpapers in json to standard out"
        self.msg_arg_wall = "setzt das angegebene Hintergrundbild"
        self.msg_arg_folder = "legt fest, welcher Ordner nach Hintergrundbildern durchsucht werden soll"
        self.msg_arg_statefile = "specify a custom file to store the application state"
        self.msg_arg_monitor = "geben Sie den gewünschten Monitor mit seinem Namen an"
        self.msg_arg_post = "prevents ruuning post_command"

        self.msg_path = "Pfad zum ausgewählten Bild:"
        self.msg_select = "Auswählen"
        self.msg_refresh = "Aktualisieren"
        self.msg_random = "Zufällig"
        self.msg_clear = "Löschen"
        self.msg_stop = "Stopp"
        self.msg_pause = "Pause"
        self.msg_search = "Suchen"
        self.msg_options = "Optionen"
        self.msg_exit = "Beenden"
        self.msg_subfolders = "Unterordner"
        self.msg_recursive = "Recursive Search"
        self.msg_hidden = "Zeige versteckte"
        self.msg_gifs = "Nur GIFs anzeigen"
        self.msg_transitions = "Übergangsoptionen anzeigen"
        self.msg_changefolder = "Ordner"
        self.msg_choosefolder = "Bitte wählen Sie einen Ordner aus"
        self.msg_caching = "Hintergrundbilder werden zwischengespeichert..."

        self.msg_help = "Waypapers Tastenkürzel:\n\nhjkl - Navigation (←↓↑→)\nf - Hintergrundbild-Ordner ändern\n"
        self.msg_help += "g - Zum Anfang scrollen\nG - Zum Ende scrollen\nR - Zufälliges Hintergrundbild\nr - Hintergrundbilder zwischenspeichern\n"
        self.msg_help += ". - Versteckte Bilder einbeziehen/ausschließen\ns - Unterordner mit einbeziehen\n? - Hilfe\nq - Beenden\n\n"
        self.msg_help += self.msg_info

        self.err_cache = "Fehler beim Löschen des Zwischenspeichers"
        self.err_backend = "Es konnte kein Hintergrundbild-Backend gefunden werden.\n"
        self.err_backend += "Installieren Sie mindestens eines der folgenden Backends:\n\n"
        self.err_backend += "- swaybg (Wayland)\n- swww (Wayland)\n"
        self.err_backend += "- hyprpaper (Wayland)\n- feh (Xorg)\n"
        self.err_backend += "- wallutils (Xorg & Wayland)\n- mpvpaper (Xorg & Wayland)\n\n"
        self.err_backend += self.msg_info

        self.tip_refresh = "Erneutes einlesen des Hintergrundbild-Ordners"
        self.tip_fill = "Skalierungsart auswählen"
        self.tip_backend = "Backend auswählen"
        self.tip_sorting = "Sortierungsart auswählen"
        self.tip_display = "Bildschirm auswählen"
        self.tip_color = "Hintergrundfarbe auswählen"
        self.tip_random = "Ein zufälliges Hintergrundbild auswählen"
        self.tip_exit = "Das Programm beenden"
        self.tip_transition = "Übergangstyp auswählen"
        self.tip_mpv_stop = "Stoppe alle mpv-Prozesse"
        self.tip_mpv_pause = "Pause Video-Wallpaper"

class French:
    def __init__(self):
        self.msg_desc = "Sélecteur de papier peint graphique pour Wayland et X11. Il fonctionne comme une interface pour feh, swaybg, wallutils, hyprpaper, mpvpaper, et swww."
        self.msg_info = "Pour plus d'informations, visitez :\nhttps://github.com/anufrievroman/waypaper"

        self.msg_arg_help = "afficher la version du programme"
        self.msg_arg_fill = "spécifier comment remplir l'écran avec l'image choisie"
        self.msg_arg_rest = "restaurer le dernier papier peint"
        self.msg_arg_back = "spécifier quel backend utiliser pour définir le papier peint"
        self.msg_arg_rand = "définir un papier peint aléatoire"
        self.msg_arg_list = "list wallpapers in json to standard out"
        self.msg_arg_wall = "set the specified wallpaper"
        self.msg_arg_folder = "specify which folder to scan for wallpapers"
        self.msg_arg_statefile = "specify a custom file to store the application state"
        self.msg_arg_monitor = "spécifiez le moniteur souhaité en utilisant son nom"
        self.msg_arg_post = "prevents ruuning post_command"

        self.msg_path = "Chemin de l'image sélectionnée :"
        self.msg_select = "Sélectionner"
        self.msg_refresh = "Actualiser"
        self.msg_random = "Aléatoire"
        self.msg_clear = "Effacer"
        self.msg_stop = "Arrêter"
        self.msg_pause = "Pause"
        self.msg_search = "Rechercher"
        self.msg_options = "Options"
        self.msg_exit = "Quitter"
        self.msg_subfolders = "Sous-dossiers"
        self.msg_recursive = "Recursive Search"
        self.msg_hidden = "Afficher caché"
        self.msg_gifs = "Afficher uniquement les gifs"
        self.msg_transitions = "Afficher les options de transition"
        self.msg_changefolder = "Dossier"
        self.msg_choosefolder = "Veuillez choisir un dossier"
        self.msg_caching = "Mise en cache des papiers peints..."

        self.msg_help = "Raccourcis clavier de Waypaper :\n\nhjkl - Navigation (←↓↑→)\nf - Changer de dossier de papier peint\n"
        self.msg_help += "g - Faire défiler vers le haut\nG - Faire défiler vers le bas\nR - Définir un papier peint aléatoire\nr - Recréer le cache des papiers peints\n"
        self.msg_help += ". - Inclure/exclure les images cachées\ns - Inclure/exclure les images des sous-dossiers\n? - Aide\nq - Quitter\n\n"
        self.msg_help += self.msg_info

        self.err_cache = "Erreur lors de la suppression du cache"
        self.err_backend = "Il semble qu'aucun des backends de papier peint ne soit installé sur le système.\n"
        self.err_backend += "Utilisez votre gestionnaire de paquets pour installer au moins l'un de ces backends :\n\n"
        self.err_backend += "- swaybg (Wayland)\n- swww (Wayland)\n"
        self.err_backend += "- hyprpaper (Wayland)\n- feh (Xorg)\n"
        self.err_backend += "- wallutils (Xorg & Wayland)\n- mpvpaper (Xorg & Wayland)\n\n"
        self.err_backend += self.msg_info

        self.tip_refresh = "Recréer le dossier d'images"
        self.tip_fill = "Choisir le type de remplissage"
        self.tip_backend = "Choisir le backend"
        self.tip_sorting = "Choisir le type de tri"
        self.tip_display = "Choisir l'affichage"
        self.tip_color = "Choisir la couleur de fond"
        self.tip_random = "Définir un papier peint aléatoire"
        self.tip_exit = "Quitter l'application"
        self.tip_transition = "Choisissez le type de transition"
        self.tip_mpv_stop = "Arrêter tous les processus mpv"
        self.tip_mpv_pause = "Pause du fond d'écran vidéo"

class Polish:
    def __init__(self):
        self.msg_desc = "GUI narzędzie do ustawiania tapety dla Wayland i X11. Jest interfejsem dla feh, swaybg, wallutils, hyprpaper, mpvpaper i swww."
        self.msg_info = "Aby dowiedzieć się więcej, odwiedź:\nhttps://github.com/anufrievroman/waypaper"

        self.msg_arg_help = "pokaż wersję programu"
        self.msg_arg_fill = "ustaw jak wypełnić ekran wybranym obrazem"
        self.msg_arg_rest = "przywróć ostatnią tapetę"
        self.msg_arg_back = "ustaw zaplecze do wyświetlania tapety"
        self.msg_arg_rand = "ustaw losową tapetę"
        self.msg_arg_list = "wypisz tapety na standardowe wyjście w formacie json"
        self.msg_arg_wall = "ustaw wybraną tapetę"
        self.msg_arg_folder = "ustaw folder do przeskanowania szukając tapet"
        self.msg_arg_statefile = "ustaw plik, żeby przechowywać stan aplikacji"
        self.msg_arg_monitor = "ustaw pożądany monitor używając jego nazwy"
        self.msg_arg_post = "prevents ruuning post_command"

        self.msg_path = "Ustaw ścieżkę pliku:"
        self.msg_select = "Wybierz"
        self.msg_refresh = "Odświerz"
        self.msg_clear = "Wyczyść"
        self.msg_stop = "Stop"
        self.msg_pause = "Pauza"
        self.msg_search = "Szukaj"
        self.msg_random = "Losowa"
        self.msg_exit = "Wyjdź"
        self.msg_options = "Opcje"
        self.msg_subfolders = "Pokaż podfolder"
        self.msg_recursive = "Recursive Search"
        self.msg_hidden = "Pokaż ukryte"
        self.msg_gifs = "Pokaż tylko Gify"
        self.msg_transitions = "Pokaż opcje przejścia"
        self.msg_changefolder = "Folder"
        self.msg_choosefolder = "Proszę wybrać folder"
        self.msg_caching = "Buforowanie tapet..."

        self.msg_help = "Skróty klawiszowe Waypaper'a:\n\nhjkl - Nawigacja (←↓↑→)\nEnter - Ustaw wybraną tapetę\nf - Zmień folder tapet\n"
        self.msg_help += "g - Przewiń na górę\nG - Przewiń na dół\nR - Ustaw losową tapetę\nr - Jeszcze raz buferuj tapety\n"
        self.msg_help += ". - Pokaż/ukryj ukryte tapety\ns - Włącz/wyłącz tapety w podfolderach\n? - Pomoc\nq - Wyjście\n\n"
        self.msg_help += self.msg_info

        self.err_cache = "Błąd w usuwaniu bufera"
        self.err_backend = "Żadne zaplecze nie zostało znalezione.\n"
        self.err_backend += "Use your package manager to install at least one of these backends:\n\n"
        self.err_backend += "Użyj twojego instalera, żeby zainstalować co najmiej jedno zaplecze:\n\n"
        self.err_backend += "- swaybg (Wayland)\n- swww (Wayland)\n"
        self.err_backend += "- hyprpaper (Wayland)\n- feh (Xorg)\n"
        self.err_backend += "- wallutils (Xorg & Wayland)\n- mpvpaper (Xorg & Wayland)\n\n"
        self.err_backend += self.msg_info

        self.tip_refresh = "Ponownie buferuj folder tapet"
        self.tip_fill = "Ustaw sposób wypełnienia"
        self.tip_backend = "Wybierz zaplecze"
        self.tip_sorting = "Wybierz sposób sortowania"
        self.tip_display = "Wybierz monitor"
        self.tip_color = "Ustaw kolor tła"
        self.tip_random = "Ustaw losową tapetę"
        self.tip_exit = "Wyjdź z aplikacji"
        self.tip_transition = "Ustaw sposób przejścia"
        self.tip_mpv_stop = "Zatrzymaj wszystkie procesy mpv"
        self.tip_mpv_pause = "Odtwarzaj/Zatrzymaj animowaną"

class Russian:
    def __init__(self):
        self.msg_desc = "Графический интерфейс для установки обоев на Wayland и X11. Работает как фронтенд для feh, swaybg, wallutils, hyprpaper, mpvpaper и swww."
        self.msg_info = "Для получения дополнительной информации посетите:\nhttps://github.com/anufrievroman/waypaper"

        self.msg_arg_help = "вывести версию программы"
        self.msg_arg_fill = "указать, как заполнить экран выбранным изображением"
        self.msg_arg_rest = "восстановить последние обои"
        self.msg_arg_back = "указать бэкенд для установки обоев"
        self.msg_arg_rand = "установить случайные обои"
        self.msg_arg_list = "вывести обои и мотиноры в формате json"
        self.msg_arg_wall = "указать путь к изображению"
        self.msg_arg_folder = "указать путь к папке с обоями"
        self.msg_arg_statefile = "указать путь к файлу состояния"
        self.msg_arg_monitor = "указать имя монитора для которого устанавливаются обои"
        self.msg_arg_post = "предотвратить выполнение post_command"

        self.msg_path = "Выбранный путь к изображению:"
        self.msg_select = "Выбрать"
        self.msg_refresh = "Обновить"
        self.msg_random = "Случайно"
        self.msg_clear = "Очистить"
        self.msg_stop = "Стоп"
        self.msg_pause = "Пауза"
        self.msg_search = "Поиск"
        self.msg_options = "Опции"
        self.msg_exit = "Выход"
        self.msg_subfolders = "Показать подпапки"
        self.msg_recursive = "Recursive Search"
        self.msg_hidden = "Показать скрытые"
        self.msg_gifs = "Показать только gif"
        self.msg_transitions = "Показать опции перехода"
        self.msg_changefolder = "Папка"
        self.msg_choosefolder = "Пожалуйста, выберите папку"
        self.msg_caching = "Кэширование обоев..."

        self.msg_help = "Горячие клавиши Waypaper:\n\nhjkl - Навигация (←↓↑→)\nf - Изменить папку с обоями\n"
        self.msg_help += "g - Прокрутка в начало\nG - Прокрутка в конец\nR - Установить случайные обои\nr - Обновить кэш обоев\n"
        self.msg_help += ". - Показать/скрыть скрытые файлы \ns - Показать/скрыть вложенные папки\n? - Справка\nq - Выход\n\n"
        self.msg_help += self.msg_info

        self.err_cache = "Ошибка при удалении кэша"
        self.err_backend = "Похоже, что ни один из бэкендов для установки обоев не установлен в системе.\n"
        self.err_backend += "Используйте менеджер пакетов для установки хотя бы одного из следующих бэкендов:\n\n"
        self.err_backend += "- swaybg (Wayland)\n- swww (Wayland)\n"
        self.err_backend += "- hyprpaper (Wayland)\n- feh (Xorg)\n"
        self.err_backend += "- wallutils (Xorg & Wayland)\n- mpvpaper (Xorg & Wayland)\n\n"
        self.err_backend += self.msg_info

        self.tip_refresh = "Обновить папку с изображениями"
        self.tip_fill = "Выбрать тип заполнения"
        self.tip_backend = "Выбрать бэкенд"
        self.tip_sorting = "Выбрать тип сортировки"
        self.tip_display = "Выбрать дисплей"
        self.tip_color = "Выбрать цвет фона"
        self.tip_random = "Установить случайные обои"
        self.tip_exit = "Выйти из приложения"
        self.tip_transition =  "Выберите тип перехода"
        self.tip_mpv_stop = "Остановить все mpv процессы"
        self.tip_mpv_pause = "Плей/пауза видео-обоев"


class Belarusian:
    def __init__(self):
        self.msg_desc = "Графічны інтэрфейс для ўстаноўкі шпалер на Wayland і X11. Працуе як фронтэнд для feh, swaybg, wallutils, hyprpaper, mpvpaper і swww."
        self.msg_info = "Для атрымання дадатковай інфармацыі наведайце:\nhttps://github.com/anufrievroman/waypaper"

        self.msg_arg_help = "вывесці версію праграмы"
        self.msg_arg_fill = "пазначыць, як запоўніць экран абранай выявай"
        self.msg_arg_rest = "аднавіць апошнія шпалеры"
        self.msg_arg_back = "паказаць бэкенд для ўстаноўкі шпалер"
        self.msg_arg_rand = "ўсталяваць выпадковыя шпалеры"
        self.msg_arg_list = "вывесці шпалеры і матыноры ў фармаце json"
        self.msg_arg_wall = "пазначыць шлях да выявы"
        self.msg_arg_folder = "ўкажыце, які тэчку сканаваць для выявы"
        self.msg_arg_statefile = "ўкажыце карыстацкі файл для захавання стану прыкладання"
        self.msg_arg_monitor = "określ żądany monitor, używając jego nazwy"
        self.msg_arg_post = "prevents ruuning post_command"

        self.msg_path = "Абраны шлях да выявы:"
        self.msg_select = "Выбраць"
        self.msg_refresh = "Абнавіць"
        self.msg_random = "Выпадкова"
        self.msg_clear = "Ачысціць"
        self.msg_stop = "Стоп"
        self.msg_pause = "Паўза"
        self.msg_search = "Шукаць"
        self.msg_options = "Опцыі"
        self.msg_exit = "Вынахад"
        self.msg_subfolders = "Паказаць падтэчкі"
        self.msg_recursive = "Recursive Search"
        self.msg_hidden = "Паказаць схаваныя"
        self.msg_gifs = "Паказаць толькі gif"
        self.msg_transitions = "Show transition options"
        self.msg_changefolder = "Тэчка"
        self.msg_choosefolder = "Калі ласка, абярыце тэчку"
        self.msg_caching = "Кэшаванне шпалер..."

        self.msg_help = "Гарачыя клавішы Waypaper:\n\nhjkl - Навігацыя (←↓↑→)\nf - Змяніць тэчку са шпалерамі\n"
        self.msg_help += "g - Пракрутка ў пачатак\nG - Пракрутка ў канец\nR - Усталяваць выпадковыя шпалеры\nr - Абнавіць кэш шпалер\n"
        self.msg_help += ". - Паказаць/схаваць схаваныя файлы \ns - Паказаць/схаваць укладзеныя тэчкі\n? - Даведка\nq - Вынахад\n\n"
        self.msg_help += self.msg_info

        self.err_cache = "Памылка пры выдаленні кэша"
        self.err_backend = "Падобна, што ніводны з бэкэндаў для ўсталёўкі шпалер не ўсталяваны ў сістэме.\n"
        self.err_backend += "Выкарыстоўвайце менеджэр пакетаў для ўстаноўкі хаця б аднаго з наступных бэкендаў:\n\n"
        self.err_backend += "- swaybg (Wayland)\n- swww (Wayland)\n"
        self.err_backend += "- hyprpaper (Wayland)\n- feh (Xorg)\n"
        self.err_backend += "- wallutils (Xorg & Wayland)\n- mpvpaper (Xorg & Wayland)\n\n"
        self.err_backend += self.msg_info

        self.tip_refresh = "Абнавіць тэчку з выявамі"
        self.tip_fill = "Выбраць тып запаўнення"
        self.tip_backend = "Выбраць бэкенд"
        self.tip_sorting = "Выбраць тып сартавання"
        self.tip_display = "Выбраць дысплей"
        self.tip_color = "Выбраць колер фону"
        self.tip_random = "Усталяваць выпадковыя шпалеры"
        self.tip_exit = "Выйсці з прыкладання"
        self.tip_transition = "Выберыце тып пераходу"
        self.tip_mpv_stop = "Спыніць усе працэсы mpv"
        self.tip_mpv_pause = "Паўза відэа-абояў"


class Chinese:
    def __init__(self):
        self.msg_desc = "Wayland 和 X11 的 GUI 壁纸设置器。它用作 feh、swaybg、hyprpaper、mpvpaper、wallutils 和 swww 的前端。"
        self.msg_info = "欲了解更多信息，请访问:\nhttps://github.com/anufrievroman/waypaper"

        self.msg_arg_help = "版本信息"
        self.msg_arg_fill = "指定所选图像填充屏幕"
        self.msg_arg_rest = "恢复上个壁纸"
        self.msg_arg_back = "指定使用哪个后端来设置壁纸"
        self.msg_arg_rand = "设置随机壁纸"
        self.msg_arg_list = "以 JSON 格式列出壁纸并输出到标准输出"
        self.msg_arg_wall = "设置指定的壁纸"
        self.msg_arg_folder = "指定扫描壁纸的文件夹"
        self.msg_arg_statefile = "指定用于存储应用程序状态的自定义文件"
        self.msg_arg_monitor = "通过其名称指定所需的显示器"
        self.msg_arg_post = "prevents ruuning post_command"

        self.msg_path = "选择的图像路径："
        self.msg_select = "选择"
        self.msg_refresh = "刷新"
        self.msg_random = "随机"
        self.msg_clear = "清除"
        self.msg_stop = "停止"
        self.msg_pause = "暂停"
        self.msg_search = "搜索"
        self.msg_options = "选项"
        self.msg_exit = "退出"
        self.msg_subfolders = "子文件夹"
        self.msg_recursive = "Recursive Search"
        self.msg_hidden = "显示隐藏项"
        self.msg_gifs = "仅显示GIF"
        self.msg_transitions = "显示过渡选项"
        self.msg_changefolder = "文件夹"
        self.msg_choosefolder = "请选择一个文件夹"
        self.msg_caching = "缓存壁纸..."

        self.msg_help = "Waypaper 的热键：\n\nhjkl -导航 (←↓↑→)\nf -更改壁纸文件夹\n"
        self.msg_help += "g -滚动到顶部\nG -滚动到底部\nR -设置随机壁纸\nr -重新缓存壁纸\n"
        self.msg_help += ". - 包括/排除隐藏图像\ns -包含/排除子文件夹中的图像\n？ -帮助\nq -退出\n\n"
        self.msg_help += self.msg_info

        self.err_cache = "删除缓存时出错"
        self.err_backend = "系统中似乎没有安装壁纸后端。\n"
        self.err_backend += "使用包管理器安装至少以下后端之一：\n\n"
        self.err_backend += "- swaybg (Wayland)\n- swww (Wayland)\n"
        self.err_backend += "- hyprpaper (Wayland)\n- feh (Xorg)\n"
        self.err_backend += "- wallutils (Xorg & Wayland)\n- mpvpaper (Xorg & Wayland)\n\n"
        self.err_backend += self.msg_info

        self.tip_refresh = "重新缓存图像文件夹"
        self.tip_fill = "选择填充类型"
        self.tip_backend = "选择后端"
        self.tip_sorting = "选择排序类型"
        self.tip_display = "选择显示"
        self.tip_color = "选择背景颜色"
        self.tip_random = "设置随机壁纸"
        self.tip_exit = "退出应用程序"
        self.tip_transition = "选择过渡类型"
        self.tip_mpv_stop = "停止所有 mpv 进程"
        self.tip_mpv_pause = "暂停视频壁纸"

class Spanish:
    def __init__(self):
        self.msg_desc = 'Cambiador de fondo de pantalla para "Wayland" y "X11". Trabaja como una interfaz gráfica para "feh", "swaybg", "wallutils", "swww" y "hyprpaper".'
        self.msg_info = "Para más información, visita:\nhttps://github.com/anufrievroman/waypaper"

        self.msg_arg_help = "imprime la versión del programa"
        self.msg_arg_fill = "específica una forma de rellenar la pantalla con la imagen escogida"
        self.msg_arg_rest = "restaura la última imagen de fondo"
        self.msg_arg_back = "específica cuál es el programa a utilizar para cambiar la imagen de fondo"
        self.msg_arg_rand = "aplica una imagen de fondo aleatoria"
        self.msg_arg_list = 'imprime un listado de las imágenes de fondo al terminal en formato "JSON"'
        self.msg_arg_wall = "establece el fondo especificado"
        self.msg_arg_folder = "specify which folder to scan for wallpapers"
        self.msg_arg_statefile = "specify a custom file to store the application state"
        self.msg_arg_monitor = "especifique el monitor deseado usando su nombre"
        self.msg_arg_post = "prevents ruuning post_command"

        self.msg_path = "Ubicación de la imagen:"
        self.msg_select = "Selecciona"
        self.msg_refresh = "Actualizar"
        self.msg_random = "Aleatorio"
        self.msg_clear = "Borrar"
        self.msg_stop = "Detener"
        self.msg_pause = "Pausa"
        self.msg_search = "Buscar"
        self.msg_options = "Opciones"
        self.msg_exit = "Salir"
        self.msg_subfolders = "Ver subcarpetas"
        self.msg_recursive = "Busqueda recursiva"
        self.msg_hidden = "Ver archivos ocultos"
        self.msg_gifs = 'Ver solamente imágenes de tipo "GIF"'
        self.msg_transitions = "Show transition options"
        self.msg_changefolder = "Carpeta"
        self.msg_choosefolder = "Por favor, selecciona una carpeta"
        self.msg_caching = "Almacenando en el caché..."

        self.msg_help = 'Controles para usar "Waypaper":\n\nhjkl - Navegación (←↓↑→)\n"Enter" (⏎) - Actualizar imagen de fondo a la imágen seleccionada\nf - Cambiar carpeta de imágenes\n'
        self.msg_help += "g - Ir a la parte de arriba\nG - Ir a la parte de abajo\nR - Cambiar imagen de fondo a una imágen aleatoria\nr - Recrear caché de imágenes\n"
        self.msg_help += ". - Ver/Omitir archivos ocultos\ns - Ver/Omitir imágenes en subcarpetas\n? - Ayuda\nq - Cerrar aplicación\n\n"
        self.msg_help += self.msg_info

        self.err_cache = "Error borrando el caché"
        self.err_backend = "Parece ser que ningún programa para actualizar la imagen de fondo está instalado en su sistema.\n"
        self.err_backend += "Por favor, instala uno de los siguientes programas para poder cambiar la imagen de fondo:\n\n"
        self.err_backend += "- swaybg (Wayland)\n- swww (Wayland)\n"
        self.err_backend += "- hyprpaper (Wayland)\n- feh (Xorg)\n"
        self.err_backend += "- wallutils (Xorg & Wayland)\n- mpvpaper (Xorg & Wayland)\n\n"
        self.err_backend += self.msg_info

        self.tip_refresh = "Volver a almacenar la carpeta de imágenes"
        self.tip_fill = "Escoja el tipo de relleno"
        self.tip_backend = "Escoja el programa para cambiar la imagen de fondo"
        self.tip_sorting = "Escoja una forma de ordenar"
        self.tip_display = "Escoja el nombre de la pantalla"
        self.tip_color = "Escoja un color de fondo"
        self.tip_random = "Actualizar la imagen de fondo a una imagen aleatoria"
        self.tip_exit = "Cerrar la aplicación"
        self.tip_transition = "Elige el tipo de transición"
        self.tip_mpv_stop = "Detener todos los procesos de mpv"
        self.tip_mpv_pause = "Pausar fondo de pantalla de video"


def load_language(lang):
    """Load the language package according to selected language"""
    if lang == "de":
        txt = German()
    elif lang == "fr":
        txt = French()
    elif lang == "ru":
        txt = Russian()
    elif lang == "by":
        txt = Belarusian()
    elif lang == "pl":
        txt = Polish()
    elif lang == "zh":
        txt = Chinese()
    elif lang == "es":
        txt = Spanish()
    else:
        txt = English()
    return txt

