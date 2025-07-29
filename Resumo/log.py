# Abstracao 
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implement the log method')

    def log_error(self,msg):
        return self._log(f'Error: {msg}')

    def log_success(self,msg):
        return self._log(f'Success: {msg}')

    
class LogFileMixin(Log):
    def _log(self,msg):
        msg_format = f'{msg} ({self.__class__.__name__})'
        print('Saving log to file', msg_format)
        with open(LOG_FILE, 'w') as file:
            file.write(msg_format)
            file.write('\n')

class LogPrintMixin(Log):
    def _log(self,msg):
        msg_format = f'{msg} ({self.__class__.__name__})'
        print(msg_format)

if __name__ == '__main__':
    # Log Print
    lp = LogPrintMixin()
    lp.log_error('Any message')
    lp.log_success('Cool message')
    
    # Log File
    lf = LogFileMixin()
    lf.log_error('Any message')
    lf.log_success('Cool message')