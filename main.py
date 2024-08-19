import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def get_nickname(self):
        return self.nickname


class Video:

    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
        self.videos = []



    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        if not self.current_user is None:
            print('Вы уже в системе !')
            return
        elif self.current_user is None:
            for user in self.users:
                if user.nickname == login:
                    if user.password == hash(password):
                        self.current_user = user
                        print(f'Вы вошли в систему {user.nickname}')
                        return
            else:
                print('Такой пользователь не найден !')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        print(f'Создал нового пользователя {nickname}')
        self.current_user = new_user

    def add(self, *all_videos):
        for video in all_videos:
            if any(vid.title == video.title for vid in self.videos):
                print(f'видео с названием {video.title} уже есть')
            else:
                print(f'видео с названием {video.title} добавлено')
                self.videos.append(video)

    def get_videos(self, word):
        word = word.lower()
        list_w = []
        for i in self.videos:
            obj = i.title.lower()
            if word in obj:
                list_w.append(i.title)
                if len(list_w) > 0:
                    print('Нашел похожее видео -', list_w)
                else:
                    print('Нет ничего похожего')

    def watch_video(self, name_video):
        if not self.current_user is None:
            for i in self.videos:
                if name_video == i.title:
                    if self.current_user.age >= 18:
                        while i.time_now <= i.duration:
                            print(f'{i.time_now}', end=' ')
                            i.time_now += 1
                            time.sleep(1)
                    else:
                        print('Видео с ограничениями по возрасту ,покиньте пожалуйста страницу!')
        else:
            print('Вы не авторизованы ,войдите пожалуйтса в аккаунт ! ')



if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode := True)
    v3 = Video('Для чего девушкам парень программист?', 10, adult_mode := True)
    # Добавление видео
    ur.add(v1, v2, v3)

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