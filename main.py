import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self, nickname):
        return self.nickname

    def get_nickname(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        adult_mode = False

    def __str__(self, title):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        if not self.current_user is None:
            print('Вы уже в системе ! ')
        elif self.current_user is None:
            for user in self.users:
                if user.nickname == login:
                    if user.password == hash(password):
                        self.current_user = user
                        print(f'Вы вошли в систему {user.nickname}')
                        break
            else:
                print('Такой пользователь не найден !')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                if user.password == password:
                    self.current_user = user
                    print(f'Пользователь {nickname} уже существует')
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            print(f'Создал нового пользователя {nickname}')

    def log_out(self, User):
        self.current_user = None

    def add(self, *all_videos):
        list = []
        if self.current_user is None:
            print('Ошибка')
        else:
            for i in all_videos:
                if i not in self.videos:
                    list.append(i)
                if len(list) > 0:
                    self.videos.extend(list)
                    print('Добавил' * list, 'в видео')
                else:
                    print('Такие видео уже есть!')

    def get_videos(self, word):
        word = word.lower()
        list_w = []
        for i in self.videos:
            obj = i.title.lower()
            if word in obj:
                list_w.append(i.title)
                if len(list_w) > 0:
                    print('Нашел похожее видео -' * list_w)
                else:
                    print('Нет ничего похожего')

    def watch_video(self, name_video):
        if not self.current_user is None:
            for i in self.videos:
                if name_video == i.title:
                    if self.current_user.age >= 18:
                        for j in range(i.time_now, i.duration):
                            print(self.current_user.age)
                            print(f'Просмотр фильма {i.title} : {j} из {i.duration}')
                            i.time_now = j
                            time.sleep(1)
                    else:
                        print('Видео с ограничениями по возрасту ,покиньте пожалуйста страницу!')
        else:
            print('Вы не авторизованы ,войдите пожалуйтса в аккаунт ! ')

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200,0,False)
    v2 = Video('Для чего девушкам парень программист?', 10,0,True)
    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')