import unicornhathd as uni

class OutputFramework:
    @staticmethod
    def show(ausgabe: list):
        """
        Zeigt eine Ausgabe an.
        :param ausgabe: Liste mit Dimensionen (16,16,3) (r (0 - 255) , g (0 - 255), b (0 - 255))
        """
        for x in range(len(ausgabe)):
            for y in range(len(ausgabe[x])):
                uni.set_pixel(x, y, ausgabe[x][y][0], ausgabe[x][y][1], ausgabe[x][y][2])
        uni.show()