import bluetooth
data = False


class BlueTooth:

    def __init__(self):
        self.bt_pkg = bluetooth
        self.devices = {}
        while True:
            self.selection()
        pass

    @staticmethod
    def reset():
        global data
        data = False
        return

    def menu(self):
        global data
        try:
            try:
                if len(self.devices) > 0:
                    print("Targets Available")
                data = input("""1.) Scan for devices
2.) Show devices
Enter choice: """)
                return data, self.devices
            except ValueError:
                return data
        except KeyboardInterrupt:
            return data, self.devices

    def scan(self):
        print("scanning")
        devices = self.bt_pkg.discover_devices(lookup_names=True)
        for x in devices:
            self.devices[x[0]] = x[1]
        return

    def show(self):
        for k, v in self.devices.items():
            print(f"{k}: {v}")
        return

    def selection(self):
        funcs = ["return", self.scan, self.show]
        data, devices = self.menu()
        if not data:
            return
        try:
            data = int(data)
            pass
        except ValueError or TypeError:
            return
        if data == 0:
            return

        funcs[data]()


BlueTooth()
