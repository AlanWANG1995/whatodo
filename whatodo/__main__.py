# import ptvsd

# # Allow other computers to attach to ptvsd at this IP address and port.
# ptvsd.enable_attach(address=('127.0.0.1', 5232), redirect_output=True)

# # Pause the program until a remote debugger is attached
# ptvsd.wait_for_attach()

from .app import app
app.run()