from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class EchoClientDatagramProtocol(DatagramProtocol):

    def startProtocol(self):
        self.transport.connect('127.0.0.1', 8000)
        datagram = raw_input("Enter the message to send:  ")
        self.sendDatagram(datagram)
    
    
    def sendDatagram(self,datagram):

        #if len(self.datagram):
        if datagram =="n" or datagram == "N":
            self.transport.write(datagram)
            print("Connection Terminated")
            reactor.stop()
        elif datagram == "":
            datagram = "blank"
            self.transport.write(datagram)
            print("No data...\nConnection Terminated")
            reactor.stop()
        elif len(datagram):   
            self.transport.write(datagram)
            print("Datagram sent to server: ", repr(datagram))
        else:
            reactor.stop()
            

    def datagramReceived(self, datagramFromServer, host):
        #if(self.datagramToCheck == datagramFromServer):
        print('Notification from server on receiving the datagram: ', repr(datagramFromServer))
        check = raw_input("Press y to continue and n to exit\n")
        if(check == 'y' or check == 'Y'):
            datagram = raw_input("Enter the message to send:  ")
            self.sendDatagram(datagram)  
        elif(check == 'n' or check == 'N'):
            datagram="n"
            self.sendDatagram(datagram)
        
def main():
    protocol = EchoClientDatagramProtocol()
    t = reactor.listenUDP(0, protocol)
    reactor.run()
    

if __name__ == '__main__':
    main()
