# W3's notes
## Realization
* The key is to use the 'socket' module. Uses TCP sockets for now while DAMA suggested 
  UDP sockets, will check on UDP sockets later.
* To enable the server to take messages from multiple clients at the same time, use modul
  'thread'. 
* Finalized (not really) codes: [script for server](https://github.com/janice-lu-zeng/OMOOC2py/blob/master/_src/om2py3w/3wex0/diaryRecorder_server.py)
  [script for client](https://github.com/janice-lu-zeng/OMOOC2py/blob/master/_src/om2py3w/3wex0/diaryRecorder_client.py)

## Related Resources
### Definitions:
* [Wiki def for network socket](https://en.wikipedia.org/wiki/Network_socket) 
  A net work socket is an endpoint of an inter-process communication across a computer
  network. Today, most communication between computers is based on the Internet Protocol;
  therefore most network sockets are Internet sockets.
  
  An Internet socket is characterized by at least the following:
  
  * Local socket address: Local IP address and port number
  
  * Protocol: A transport protocol (e.g., TCP, UDP, raw IP). Thus, TCP port 53 and UDP
    port 53 are distinct sockets.
