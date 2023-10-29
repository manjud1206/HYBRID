from configparser import RawConfigParser

config = RawConfigParser()    # <<  RawConfigParser is a class & config is a object for this class  >>
config.read(r"C:\Users\manju\PycharmProjects\HYBRID\Configurations\config.ini") # config.ini filr location

class ReadConfig:
    @staticmethod
    def geturl():
        url = config.get('common info','base_url')
        return url

    @staticmethod
    def getusername():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info','password')
        return password
print(ReadConfig.geturl())
print(ReadConfig.getpassword())
print(ReadConfig.getusername())