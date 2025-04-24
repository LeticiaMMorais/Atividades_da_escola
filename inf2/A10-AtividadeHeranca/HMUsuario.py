class Usuario:
    codigo = ''
    paginas_visitadas = 0
    
    def getCodigo(self):
        return self.codigo
    
    def setCodigo(self, cod):
        self.codigo = cod
    
    def getPaginasVisitadas(self):
        return self.paginas_visitadas
    
    def setPaginasVisitadas(self):
        self.paginas_visitadas += 1