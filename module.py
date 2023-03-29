class Versenyzo:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.szul_ev:int = int(v[1])
        self.rajt_szam:int = int(v[2])
        self.nem:bool = v[3] == 'f'
        self.kategoria:str = v[4]
        self.idoeredmenyek:dict = {
            'úszás': v[5],
            'depó 1': v[6],
            'kerékpár': v[7],
            'depó 2': v[8],
            'futás': v[9]
        }
        self.ossz_mp:int = 0
        for ie in self.idoeredmenyek.values():
            opm:list[str] = ie.split(':')
            self.ossz_mp += (int(opm[0]) * 3600 + int(opm[1]) * 60 + int(opm[2]))