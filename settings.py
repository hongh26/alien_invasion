class Settings:
    """存储游戏Alien Invasion中所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置。"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 子弹设置
        # self.bullet_width = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 9

        # 飞船设置
        self.ship_limit = 3

        # 外星人设置
        self.fleet_drop_speed = 10

        # 加快游戏节奏的速度。
        self.speedup_scale = 1.5
        # 外星人分数提高的速度。
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.bullet_speed = 3.0
        self.ship_speed = 1.5
        self.alien_speed = 0.5

        # fleet_direction 为 1 表示向右移，为 -1 表示向左移
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50


    def increase_speed(self):
        """提高速度设置和外星人的分数"""
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)