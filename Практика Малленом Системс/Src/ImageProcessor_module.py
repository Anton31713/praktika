from PIL import Image
import os
import shutil
import logging

class ImageProcessor:
    """
    Модуль обработки и работы с изображениями
    """
    
    def __init__(self):
        self.supported_formats = {'.png', '.jpg', '.jpeg', '.bmp'}
        self.setup_logging()
    
    def setup_logging(self):
        """Настройка логирования"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('image_processor.log', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def validate_image_path(self, image_path):
        """Проверка корректности пути к изображению"""
        if not os.path.exists(image_path):
            return False, "Файл не существует"
        
        file_ext = os.path.splitext(image_path)[1].lower()
        if file_ext not in self.supported_formats:
            return False, f"Неподдерживаемый формат файла: {file_ext}"
        
        return True, "OK"
    
    def convert_to_black_white(self, image_path):
        """
        Преобразование изображения в черно-белое
        Код функции: IP-001
        """
        try:
            # Проверка входных данных
            is_valid, message = self.validate_image_path(image_path)
            if not is_valid:
                return False, None, message
            
            # Загрузка и преобразование изображения
            with Image.open(image_path) as img:
                bw_image = img.convert('L')
            
            # Формирование пути для сохранения
            directory = os.path.dirname(image_path)
            filename = os.path.basename(image_path)
            name, ext = os.path.splitext(filename)
            output_filename = f"{name}_bw{ext}"
            output_path = os.path.join(directory, output_filename)
            
            # Сохранение результата
            bw_image.save(output_path)
            self.logger.info(f"Изображение успешно преобразовано: {output_path}")
            
            return True, output_path, "Операция выполнена успешно"
            
        except Exception as e:
            error_msg = f"Ошибка при преобразовании изображения: {str(e)}"
            self.logger.error(error_msg)
            return False, None, error_msg
    
    def move_image(self, source_path, destination_folder):
        """
        Перемещение файла изображения
        Код функции: IP-002
        """
        try:
            # Проверка исходного файла
            is_valid, message = self.validate_image_path(source_path)
            if not is_valid:
                return False, None, message
            
            # Проверка целевой директории
            if not os.path.exists(destination_folder):
                return False, None, "Целевая директория не существует"
            
            if not os.path.isdir(destination_folder):
                return False, None, "Указанный путь не является директорией"
            
            # Проверка прав доступа
            if not os.access(destination_folder, os.W_OK):
                return False, None, "Нет прав на запись в целевую директорию"
            
            # Перемещение файла
            filename = os.path.basename(source_path)
            destination_path = os.path.join(destination_folder, filename)
            
            # Если файл с таким именем уже существует
            counter = 1
            name, ext = os.path.splitext(filename)
            while os.path.exists(destination_path):
                new_filename = f"{name}_{counter}{ext}"
                destination_path = os.path.join(destination_folder, new_filename)
                counter += 1
            
            shutil.move(source_path, destination_path)
            self.logger.info(f"Файл перемещен: {source_path} -> {destination_path}")
            
            return True, destination_path, "Файл успешно перемещен"
            
        except Exception as e:
            error_msg = f"Ошибка при перемещении файла: {str(e)}"
            self.logger.error(error_msg)
            return False, None, error_msg
    
    def get_supported_formats(self):
        """Получение списка поддерживаемых форматов"""
        return list(self.supported_formats)
