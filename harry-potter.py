class Escola:
    
    
    def __init__(self, nome):
        self.nome = nome
        self.casas = []
        
    
    def incluir_casa(self, casa):
        self.casas.append(casa)
        
        
class Casa:
    
    
    def __init__(self, nome, animal):
        self.nome = nome
        self.animal = animal
        self.diretor = None
        self.monitor = None
        
        
    def set_diretor(self, professor):
        self.diretor = professor
        
        
    def set_monitor(self, aluno):
        self.monitor = aluno
        
        
class Professor:
    
    
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.disciplina = []
        
    
    def incluir_disciplina(self, Disciplina):
        self.disciplina.append(Disciplina)
        
        
class Disciplina:
    
    
    def __init__(self, nome, ementa):
        self.nome = nome
        self.ementa = ementa 
        self.alunos = []
        
        
    def incluir_aluno(self, aluno):
        self.alunos.append(aluno)
        
        
class Aluno:
    
    
    def __init__(self, nome, nascimento, tipo):
        self.nome = nome
        self.nascimento = nascimento
        self.tipo = tipo
        self.casa = None
        self.__triunfos = 0
        self.__mau_feitos = 0
        
        
    def set_casa(self, Casa):
        self.casa = Casa
        
    
    def incluir_triunfo(self, pontos):
        self.__triunfos += pontos
        
        
    def incluir_mau_feito(self, pontos):
        self.__mau_feitos += pontos
        
        
    def get_triunfos(self):
        return self.__triunfos 
    
    
    def get_mau_feitos(self):
        return self.__mau_feitos
    
    
class Torneio:
    
    
    def __init__(self, casa1, casa2):
        self.casa1 = casa1
        self.casa2 = casa2
        self.__pontos_casa1 = 0
        self.__pontos_casa2 = 0
        
        
    def marcar_ponto(self, casa, pontos):
        if casa == self.casa1:
            self.__pontos_casa1 += pontos
            
        else:
            self.__pontos_casa2 += pontos
            
            
    def get_pontos_casa1(self):
        return self.__pontos_casa1
    
    
    def get_pontos_casa2(self):
        return self.__pontos_casa2
    