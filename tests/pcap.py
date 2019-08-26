import pcapy
from impacket.ImpactDecoder import LinuxSLLDecoder, EthDecoder
from threading import Thread

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class DecoderThread(Thread):
    def __init__(self, pcapObj):
        datalink = pcapObj.datalink()
        if pcapy.DLT_EN10MB == datalink:
            self.decoder = EthDecoder()
        elif pcapy.DLT_LINUX_SLL == datalink:
            self.decoder = LinuxSLLDecoder()
        else:
            raise Exception("Tipo de datalink não suportado: " % datalink)

        self.pcap = pcapObj
        Thread.__init__(self)

    def run(self):
        self.pcap.loop(0, self.packetHandler)

    def display_hex(self, pkt):
        return pkt.get_data_as_string()


    def packetHandler(self, hdr, data):
        p = self.decoder.decode(data)
        ip = p.child()
        tcp = ip.child()
        src = (ip.get_ip_src(), tcp.get_th_sport())
        dst = (ip.get_ip_dst(), tcp.get_th_dport())
        seq = tcp.get_th_seq()
        ack = tcp.get_th_ack()
        flags = tcp.get_th_flags()
        win = tcp.get_th_win()
        sum = tcp.get_th_sum()
        urp = tcp.get_th_urp()
        payload = self.display_hex(p)
        print('\n')
        print(f'SRC -> {src[0]}:{src[1]} | DST -> {dst[0]}:{dst[1]} | [{flags}:{ack}] Seq={seq} Win={win} Size={len(payload)} Sum={sum} Urp={urp}')

        if dst[0] == '172.17.7.232':
            print(bcolors.OKGREEN + str(payload) + bcolors.ENDC)
        else:
            print(bcolors.WARNING + str(payload) + bcolors.ENDC)

        print('\n')


dev = 'wlp2s0'

cap = pcapy.open_live(dev, 65536, 0, 100)
cap.setfilter(r'ip proto \tcp')

print("Ouvindo com %s: net=%s, mascara=%s, tipo=%d" % (dev, cap.getnet(), cap.getmask(), cap.datalink()))

#devices = pcapy.findalldevs()

#for device in devices:
#    print(device)

DecoderThread(cap).start()
