from log import LogPrintMixin

class Eletronico:
    def __init__(self, name):
        self._name = name 
        self._on = False
    
    def on(self):
        if not self._on:
            self._on = True
    
    def off(self):
        if self._on:
            self._on = False

class Smartphone(Eletronico, LogPrintMixin):
    def on(self):
        super().on()
        if self._on:
            msg_success = f'{self._name} is now ON'
            self.log_success(msg_success)
    
    def off(self):
        super().off()
        if not self._on:
            msg_error = f'{self._name} is now OFF'
            self.log_error(msg_error)

class Tv(Eletronico, LogPrintMixin):
    def on(self):
        super().on()
        if self._on:
            msg_success = f'{self._name} is now ON'
            self.log_success(msg_success)
    
    def off(self):
        super().off()
        if not self._on:
            msg_error = f'{self._name} is now OFF'
            self.log_error(msg_error)