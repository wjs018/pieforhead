# pieforhead

A python wrapper for the PieFed API

## Sample Usage

### Synchronous client

```python
from piefedhead import PieFed

piefed = PieFed("https://instance.tld")
piefed.log_in("username", "password")

piefed.close()
```

Instead of explicitly calling the `close()` function like above, you can alternatively ensure proper termination in two other ways:

```python
# Inside a context manager
with PieFed("https://instance.tld") as piefed:
    piefed.log_in("username", "password")

# The connection is closed after leaving the `with` block
```

```python
# Registering an event handler
import atexit

piefed = PieFed("https://instance.tld")
atexit.register(piefed.close)  # Automatically closes the client at program termination
```
