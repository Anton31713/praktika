import ImageProcessor_module

def main():
    processor = ImageProcessor_module.ImageProcessor()
    
    print("Выберите нужную вам операцию:")
    print("1 - Преобразовать изображение в черно-белое")
    print("2 - Переместить изображение")
    
    user_selection = input("Введите 1 или 2: ")
    picture_way = input("Введите путь к изображению: ")
    
    if user_selection == "1":
        success, result_way, message = processor.convert_to_black_white(picture_way)
        if success:
            print(f"Изображение успешно преобразовано: {result_way}")
        else:
            print(f"Ошибка: {message}")
            
    elif user_selection == "2":
        destination_folder = input("Введите путь к целевой папке: ")
        success, result_way, message = processor.move_image(picture_way, destination_folder)
        if success:
            print(f"Изображение успешно перемещено: {result_way}")
        else:
            print(f"Ошибка: {message}")
            
    else:
        print("Неверный выбор операции")

if __name__ == "__main__":
    main()
