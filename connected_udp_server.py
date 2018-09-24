from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class EchoUDP(DatagramProtocol):
    def datagramReceived(self, datagram, address):
        if(datagram == "n" or datagram == "N"):
            print("Datagram received from the client: '%s'"%datagram)
            print("\nClient decided to terminate")
            self.transport.write(datagram,address)
            reactor.stop()
        elif(datagram=="blank"):
            print("No data received from client...\nClient decided to terminate")
            self.transport.write(datagram,address)
            reactor.stop()
        else:
            print("Datagram received from the client: '%s'"%datagram)
            print("\nNotifying client...!!!")
            self.transport.write(datagram, address)
       
        
def main():
    reactor.listenUDP(8000, EchoUDP())
    reactor.run()

if __name__ == '__main__':
    main()
