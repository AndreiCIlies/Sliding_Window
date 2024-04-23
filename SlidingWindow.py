class Packet:
    def __init__(self, isSent, isReceived, hasSendError, hasReceiveError):
        self.isSent = False
        self.isReceived = False
        self.hasSendError = hasSendError
        self.hasReceiveError = hasReceiveError

class SlidingWindow:
    def __init__(self, windowSize, windowStep):
        self.windowSize = windowSize
        self.windowStep = 0
        
class Sender:
    def __init__(self, packets, slidingWindow):
        self.packets = packets
        self.slidingWindow = SlidingWindow(slidingWindow.windowSize, slidingWindow.windowStep)
        
class Receiver:
    def __init__(self, receivedPackets):
        self.receivedPackets = receivedPackets
        
def slidingWindow(packets, sender, receiver):
    acknowledgedPackets = []

    while sender.slidingWindow.windowStep < len(packets):
        
        if packets[sender.slidingWindow.windowStep].isSent == False:
            if packets[sender.slidingWindow.windowStep].hasSendError == False:
                packets[sender.slidingWindow.windowStep].isSent = True
                print("Sender sent the packet " + str(sender.slidingWindow.windowStep + 1) + " to receiver")
                
                if receiver.receivedPackets.count(sender.slidingWindow.windowStep + 1) == 0:
                    receiver.receivedPackets.append(sender.slidingWindow.windowStep + 1)

                if packets[sender.slidingWindow.windowStep].hasReceiveError == False:
                    packets[sender.slidingWindow.windowStep].isReceived = True
                    print("Packet " + str(sender.slidingWindow.windowStep + 1) + " is acknowledged")
                    
                    if acknowledgedPackets.count(sender.slidingWindow.windowStep + 1) == 0:
                        acknowledgedPackets.append(sender.slidingWindow.windowStep + 1)

                    sender.slidingWindow.windowStep += 1
                    print()
                
                else:
                    packets[sender.slidingWindow.windowStep].hasReceiveError = False
                    packets[sender.slidingWindow.windowStep].isSent = False
                    print("Packet " + str(sender.slidingWindow.windowStep + 1) + " has receive Error")
                    print("Packet " + str(sender.slidingWindow.windowStep + 1) + " is not acknowledged")
            
            else:
                packets[sender.slidingWindow.windowStep].hasSendError = False
                print("Packet " + str(sender.slidingWindow.windowStep + 1) + " has send Error")
                print("Sender did not send the packet " + str(sender.slidingWindow.windowStep + 1) + " to receiver")
                print("Packet " + str(sender.slidingWindow.windowStep + 1) + " is not received")
                print()

                endSlidingWindowIndex = min(sender.slidingWindow.windowStep + sender.slidingWindow.windowSize, len(packets))
                    
                for i in range(sender.slidingWindow.windowStep + 1, endSlidingWindowIndex):
                    if packets[i].isSent == False:
                        if packets[i].hasSendError == False:
                            packets[i].isSent = True
                            print("Sender sent the packet " + str(i + 1) + " to receiver")
                            
                            if receiver.receivedPackets.count(i + 1) == 0:
                                receiver.receivedPackets.append(i + 1)
                            
                            if packets[i].hasReceiveError == False:
                                packets[i].isReceived = True
                                print("Packet " + str(i + 1) + " is acknowledged")
                                
                                if acknowledgedPackets.count(i + 1) == 0:
                                    acknowledgedPackets.append(i + 1)

                                print()
                            
                            else:
                                packets[i].hasReceiveError = False
                                packets[i].isSent = False
                                print("Packet " + str(i + 1) + " has receive Error")
                                print("Packet " + str(i + 1) + " is not acknowledged")
                                print()
                        
                        else:
                            packets[i].hasSendError = False
                            print("Packet " + str(i + 1) + " has send Error")
                            print("Sender did not send the packet " + str(i + 1) + " to receiver")
                            print("Packet " + str(i + 1) + " is not received")
                            print()
                    
                    else:
                        if packets[i].isReceived == False:
                            if packets[i].hasReceiveError == False:
                                packets[i].isReceived = True
                                print("Packet " + str(i + 1) + " is acknowledged")

                                if acknowledgedPackets.count(i + 1) == 0:
                                    acknowledgedPackets.append(i + 1)

                                print()
                            
                            else:
                                packets[i].hasReceiveError = False
                                packets[i].isSent = False
                                print("Packet " + str(i + 1) + " has receive Error")
                                print("Packet " + str(i + 1) + " is not acknowledged")
                                print()

                packets[sender.slidingWindow.windowStep].hasSendError = False
                packets[sender.slidingWindow.windowStep].isSent = True
                print("Sender sent the packet " + str(sender.slidingWindow.windowStep + 1) + " to receiver")
                
                if receiver.receivedPackets.count(sender.slidingWindow.windowStep + 1) == 0:
                    receiver.receivedPackets.append(sender.slidingWindow.windowStep + 1)
                
                if packets[sender.slidingWindow.windowStep].hasReceiveError == False:
                    packets[sender.slidingWindow.windowStep].isReceived = True
                    print("Packet " + str(sender.slidingWindow.windowStep + 1) + " is acknowledged")

                    if acknowledgedPackets.count(sender.slidingWindow.windowStep + 1) == 0:
                        acknowledgedPackets.append(sender.slidingWindow.windowStep + 1)

                    print()
                
                else:
                    packets[sender.slidingWindow.windowStep].hasReceiveError = False
                    packets[sender.slidingWindow.windowStep].isSent = False
                    print("Packet " + str(sender.slidingWindow.windowStep + 1) + " has receive Error")
                    print("Packet " + str(sender.slidingWindow.windowStep + 1) + " is not acknowledged")
                    print()
        
        else:
            sender.slidingWindow.windowStep += 1
        
    print("Packets in the order of joining receiver:", ' '.join(str(i) for i in receiver.receivedPackets))
    
    print("Packets in the order of being acknowledged:", ' '.join(str(i) for i in acknowledgedPackets))
    
    receiver.receivedPackets.sort()
    
    print("Sorted packets:", ' '.join(str(i) for i in receiver.receivedPackets))

def main():
    noOfPackets = int(input("Introduce the amount of packets: "))
    packets = [Packet(False, False, False, False) for i in range(noOfPackets)]
    
    # Simulate interruptions
    packets[2].hasSendError = True
    packets[3].hasSendError = True
    packets[4].hasReceiveError = True
    
    slidingWindowSize = int(input("Introduce the sliding window size: "))
    sender = Sender(packets, SlidingWindow(slidingWindowSize, 0))
    receiver = Receiver([])
    
    print()
    
    slidingWindow(packets, sender, receiver)
    
main()