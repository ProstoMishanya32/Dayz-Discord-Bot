from modules.config_creater import CreatingConfig


class Config(CreatingConfig):
    def __init__(self) -> None:
        super().__init__(path = 'config.json')

        self.bot = self.Bot(config = self)
        self.database = self.Database(config = self)
        self.server = self.Server(config = self)
        self.embed = self.Embed(config = self)
    class Bot:
        def __init__(self, config : CreatingConfig) -> None:
            self.token = config.config_field(key = 'token', layer = 'bot', default = 'Здесь ваш Discord Токен')
            self.prefix = config.config_field(key = 'prefix', layer = 'bot', default = '!')

    class Server:
        def __init__(self, config : CreatingConfig) -> None:
            self.ul_image_server = config.config_field(key = 'url_image_server', layer = 'server', default = 'Ссылка на изображение вашего сервера')
            self.name_server = config.config_field(key = 'name_server', layer = 'server', default = 'INNOCENCE SERVER')
            self.admin_role = config.config_field(key = 'admin_role', layer = 'server', default = 'Роль админа' )
    class Embed:
        def __init__(self, config: CreatingConfig) -> None:
            self.embed_main = config.config_field(key = 'embed_main', layer = 'Embed', default = 'Ссылка на изображение для первого окна')
            self.embed_welcome = config.config_field(key = 'embed_welcome', layer = 'Embed', default = 'Ссылка на изображение для первого окна')
    class Database:
        def __init__(self, config : CreatingConfig) -> None:
            self.path = config.config_field(key = 'path', layer = 'database', default = 'database.db')