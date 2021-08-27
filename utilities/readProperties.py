import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadProperties:

    @staticmethod
    def getApplicationURL():
        url = config.get('login page', 'URL')
        return url

    @staticmethod
    def getUserEmail():
        useremail = config.get('login page', 'email')
        return useremail

    @staticmethod
    def getPassword():
        password = config.get('login page', 'password')
        return password


