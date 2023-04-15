
from autobahn.asyncio.component import Component, run
from cyborg.accelerator.drivers.fpga.base import FPGADriver

import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
whost = "controller"
wport = 8181
wamp_transport = [ 
    {
        "url": "wss://192.168.6.100:8181/",
        "max_retries": -1,
        "serializers": ["json"],
        "endpoint": {
            "type": "tcp",
            "host": whost,
            "port": wport,
            "tls": ctx
            },
        },
    ]

class CyborgWampAgent():
    def __init__(self):
        self.driver = FPGADriver()
        self.component = Component(transports=wamp_transport, realm="s4t")
        
        @self.component.on_join
        def start(session, details):
            print("connessione stabilita")
            agent = CyborgWampAgent()
            try:
                yield from session.register(funzione, 'cyborg.funzione')
                yield from session.register(program, 'cyborg.program')
                print("funzioni registrate")
            except Exception as e:
                print("RPC non registrate -> errore: {0}".format(e))

        def funzione():
            print("esecuzione della funzione tramite Cyborg-WAMP")
            return str("ho eseguito la funzione, risultato tramite wamp")

        def program():
            driver = self.driver.create("xilinx")
            driver.program()
            return
        
    def exec(self):
        run([self.component])
        