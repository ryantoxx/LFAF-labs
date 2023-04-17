class CNF:
    def __init__(self, VN, VT, P, S):
        self.VN = VN
        self.VT = VT
        self.P = P
        self.S = S
   
    def null_production(self):
        P = self.P.copy()
        eps = []
        for production in P:
            if '' in P[production]:
                eps.append(production)
                P[production].remove('')

        eliminate = []
        for i in P.keys():
            if not P[i]:
                eliminate.append(i)
        for item in eliminate:
            P.pop(item)
            self.VN.remove(item)

        for item in eps:
            for production in P:
                for i in range(len(P[production])):
                    P[production][i] = P[production][i].replace(item, '')
        self.P = P
        print("\nP = ", self.P)

    def unit_production(self):
        for production in self.P:
            for symbol in self.P[production]:
                if symbol in self.VN:
                    self.P[production].remove(symbol)
                    self.P[production].extend(self.P[symbol])
        print("\nP = ", self.P)

    def eliminate_useless_symbols(self):
        reached = set()
        for vt in self.VN:
            for production in self.P:
                for symbol in self.P[production]:
                    if vt in symbol:
                        reached.add(vt)

        useless = []
        for item in list(self.P.keys()):
            if item not in reached:
                useless.append(item)

        for item in useless:
            del self.P[item]
            self.VN.remove(item)
        print("\nP = ", self.P)


    def toNormalForm(self):
        self.VN.append('S0')
        dict = {'S0': ['S']}
        self.P = {**dict, **self.P}

        final = {}
        dict = {}
        flag = 0
        for production in self.P:
            for symbol in self.P[production]:
                if len(symbol) > 1:
                    for char in symbol:
                        if char in self.VT and char not in final.values():
                            final[chr(70 + flag)] = char
                            dict[char] = chr(70 + flag)
                            flag += 1

        for item in dict.keys():
            for production in self.P:
                for i in range(len(self.P[production])):
                    if len(self.P[production][i]) > 1:
                        self.P[production][i] = self.P[production][i].replace(item, dict[item])

        self.P = {**self.P, **final}
        flag = 1
        final = {}
        for production in self.P:
            for symbol in self.P[production]:
                if len(symbol) > 2:
                    final[production] = 'Y'

        production = list(self.P.keys())[1]
        for symbol in self.P[production]:
            if len(symbol) > 2:
                while len(symbol) > 2:
                    final[('X' + str(flag))] = symbol[:2]
                    print(('X' + str(flag)), '->', symbol[:2])
                    flag += 1
                    if len(symbol[2:]) > 2:
                        final[('X' + str(flag))] = ('X' + str(flag + 1)) + symbol[-1]
                        print(('X' + str(flag)), '->', ('X' + str(flag + 1)) + symbol[-1])
                        flag += 1
                    symbol = symbol[2:]

        for production in self.P:
            for symbol in self.P[production]:
                if len(symbol) > 2:
                    self.P[production].remove(symbol)

        for production in final:
            if production in self.P:
                self.P[production].append(final[production])
            else:
                self.P[production] = final[production]

        print("\nP =" , self.P)
    


