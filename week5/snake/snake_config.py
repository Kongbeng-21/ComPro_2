class Config:
    __setting = {
        'PS_W': 1000,
        'PS_H': 800,

        'BS': 27,
        'ROWS': 20,
        'COLS': 30,

        'COLOR_BK': (0, 0, 0),
        'COLOR_WH': (255, 255, 255),
        'COLOR_R': (255, 0, 0)
    }

    @classmethod
    def get(cls, key):
        return cls.__setting[key]

    @classmethod
    def get_window_size(cls):
        return (cls.__setting['PS_W'], cls.__setting['PS_H'])

    @classmethod
    def get_color(cls, key):
        return cls.__setting['COLOR_' + key]
