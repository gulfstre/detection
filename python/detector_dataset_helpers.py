import requests
import os
import zipfile
import shutil



class DetectorDatasetHelper:
    @staticmethod
    def create_folder(path):
        # Проверяем, существует ли уже папка
        if not os.path.exists(path):
            try:
                # Создаем папку
                os.makedirs(path)
                print(f"Папка '{path}' успешно создана.")
            except OSError as error:
                print(f"Ошибка при создании папки {path}: {error}")
        else:
            print(f"Папка '{path}' уже существует.")


    @staticmethod
    def download_file(url, path):
        # Извлекаем имя файла из URL
        filename = url.split('/')[-1]

        # Составляем полный путь к файлу
        file_path = os.path.join(path, filename)

        print(f'Начинаем загрузку файла: {filename}')

        # Отправляем GET-запрос к указанному URL
        response = requests.get(url)

        # Проверяем, что запрос выполнен успешно (код ответа 200)
        if response.status_code == 200:
            # Открываем файл для записи в бинарном режиме и сохраняем тело ответа
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f'Файл успешно скачан и сохранён как: {file_path}')
        else:
            print(f'Ошибка при скачивании файла. Код ответа: {response.status_code}')


    @staticmethod
    def download_file_with_resume(url, folder_path):
        # Извлекаем имя файла из URL
        filename = url.split('/')[-1]
        file_path = os.path.join(folder_path, filename)

        # Определяем размер уже скачанной части файла, если файл существует
        if os.path.exists(file_path):
            downloaded_bytes = os.path.getsize(file_path)
            print(f'Продолжаем загрузку файла: {filename}')
        else:
            downloaded_bytes = 0
            print(f'Начинаем загрузку файла: {filename}')

        # Сначала получаем размер файла на сервере
        response = requests.head(url)
        total_bytes = int(response.headers.get('content-length', 0))

        # Проверяем, совпадает ли размер файла на сервере с размером уже скачанного файла
        if downloaded_bytes >= total_bytes > 0:
            print(f'Файл "{filename}" уже полностью скачан.')
            return



        # Если файл не полностью скачан, продолжаем с последнего байта
        headers = {'Range': f'bytes={downloaded_bytes}-'}
        response = requests.get(url, headers=headers, stream=True)

        # Проверяем поддержку сервером докачки
        if response.status_code in [200, 206]:
            # Дозаписываем в файл оставшиеся байты
            with open(file_path, 'ab') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f'Файл "{filename}" успешно скачан в "{folder_path}".')
        else:
            print(f'Ошибка при скачивании файла. Код ответа: {response.status_code}')


    @staticmethod
    def unzip_file(zip_path, extract_to):
        # Проверяем, существует ли ZIP-файл
        if not os.path.isfile(zip_path):
            print(f"Файл {zip_path} не найден.")
            return

        # Попытка открыть и извлечь ZIP-файл
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
                print(f"Файлы из {zip_path} успешно извлечены в {extract_to}")
        except zipfile.BadZipFile:
            print(f"Ошибка: файл {zip_path} повреждён или не является ZIP-архивом.")
        except Exception as e:
            print(f"Произошла ошибка при извлечении файлов: {e}")


    @staticmethod
    def unzip_file_nopaths(zip_path, extract_to):
        # Проверяем, существует ли ZIP-файл
        if not os.path.isfile(zip_path):
            print(f"Файл {zip_path} не найден.")
            return

        print(f'Начинаем распаковку файла: {zip_path}')
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                # Получаем список всех элементов в архиве
                members = zip_ref.namelist()
                # Извлекаем каждый элемент индивидуально
                for member in members:
                    # Строим абсолютный путь к файлу/папке в целевой директории
                    target_path = os.path.join(extract_to, os.path.basename(member))
                    # Если элемент является директорией, создаем ее
                    if member.endswith('/'):
                        os.makedirs(target_path, exist_ok=True)
                    else:
                        # Извлекаем файл с корректировкой пути
                        with zip_ref.open(member) as source, open(target_path, "wb") as target:
                            shutil.copyfileobj(source, target)
                print(f"Файлы из {zip_path} успешно извлечены в {extract_to}")
        except zipfile.BadZipFile:
            print(f"Ошибка: файл {zip_path} повреждён или не является ZIP-архивом.")
        except Exception as e:
            print(f"Произошла ошибка при извлечении файлов: {e}")


    @staticmethod
    def delete_file(file_path):
        # Проверяем, существует ли файл
        if os.path.exists(file_path):
            try:
                # Удаляем файл
                os.remove(file_path)
                print(f"Файл '{file_path}' успешно удален.")
            except OSError as e:
                print(f"Ошибка при удалении файла '{file_path}': {e}")
        else:
            print(f"Файл '{file_path}' не найден.")

    @staticmethod
    def filter_labels_and_images(path, valid_classes):

        print(f"Начинаем фильтрацию файлов")

        for split in ['train', 'val']:
            labels_path = os.path.join(path, 'labels', f'{split}2017')
            images_list_path = os.path.join(path, f'{split}2017.txt')  # Путь к файлу со списком изображений

            remaining_images = []  # Список для хранения путей к оставшимся изображениям

            for filename in os.listdir(labels_path):
                if not filename.endswith('.txt'):
                    continue

                full_path = os.path.join(labels_path, filename)
                with open(full_path, 'r') as file:
                    lines = file.readlines()

                filtered_lines = [line for line in lines if line.split()[0] in valid_classes]

                if filtered_lines:
                    with open(full_path, 'w') as file:
                        file.writelines(filtered_lines)
                    # Добавляем путь к изображению в список оставшихся изображений
                    remaining_images.append(f"./images/{split}2017/{filename.replace('.txt', '.jpg')}\n")
                else:
                    # Если аннотации пусты, удаляем файл аннотаций и соответствующее изображение
                    image_path = os.path.join(path, 'images', f'{split}2017', filename.replace('.txt', '.jpg'))
                    os.remove(full_path)  # Удалить пустой файл аннотаций
                    if os.path.exists(image_path):
                        os.remove(image_path)  # Удалить соответствующий файл изображения

            # Перезаписываем файл со списком оставшихся изображений
            with open(images_list_path, 'w') as file:
                file.writelines(remaining_images)

        print(f"Фильтрация файлов завершена") 
