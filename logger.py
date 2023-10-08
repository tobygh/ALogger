import threading

from datetime import datetime

class Config:
    "Config"

class ConfigParser:
    __args = None

    @classmethod
    def get_args(cls):
        return cls.__args
    
    @classmethod
    def set_args(cls,args):
        cls.__args = args

class Logger:
    logger = None
    def __init__(self):
        raise NotImplementedError("not allowed. please use Logger.get_logger")
    
    @classmethod
    def get_logger(cls):
        if not cls.logger is None:
            return cls.logger
        try :
            args = ConfigParser.get_args()
            logger_config = args.logger_config
            cls.logger = cls.__LoggerImpl(logger_config.path,logger_config.is_print,logger_config.is_write)
        except :
            cls.logger = cls.__LoggerImpl(path='log',is_print=True,is_write=True)
            
        return cls.logger

    class __LoggerImpl:
        def __init__(self,path,is_print,is_write) :
            now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            with open(path,"w")as f:    
                f.write(f"{now}\n")
            self.__path = path
            self.__is_print = is_print
            self.__is_write = is_write
            self.__mutex = threading.Lock()

        def show(self,s1,s2):
            self.__mutex.acquire()
            f_str = f"[{s1}] {s2}\n"

            if self.__is_print:
                print(f_str,end='')
            if self.__is_write:
                with open(self.__path,"a",encoding="utf-8") as f:
                    f.write(f_str)
            self.__mutex.release()
        def info(self,s_str):
            self.show('info',s_str)

        def warn(self,s_str):
            self.show('warn',s_str)

        def error(self,s_str):
            self.show('error',s_str)