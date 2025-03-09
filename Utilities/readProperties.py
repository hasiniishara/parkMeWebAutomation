import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common info', 'userName')
        return username

    @staticmethod
    def getUserPassword():
        userpassword = config.get('common info', 'userPw')
        return userpassword