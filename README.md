# cmpe273-lab3
## The repository contains 5 files
  - Output.docx contains the screenshots of the output and the answer to question 2.
  - connected_udp_client.py and connected_udp_server.py contains the connected UDP client and server code respectively.
  - multicast_udp_client.py and multicast_udp_server.py contains the multicast UDP client and server code respectively.
## Answer to Question 2:
- In Multicast UDP, there is no server/client differentiation at the protocol level. In this type of UDP, multicast datagrams are sent to     a special multicast group addresses. To, receive any message, one must join the group. The messages are received by all the members who     are in the group. **Hence, even when the server is off the clients in the group receive the messages**

- The server calls the joinGroup method to join the multicast group and sends a unicast message to reply the multicast message it receives   from the client
