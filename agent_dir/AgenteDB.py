from . agents import *
from random import randint


class AgenteDBClass(Agent):

    def __init__(self, x=2, y=2):
        Agent.__init__(self)

        ##
        # Personalize the identifier of this class.
        # Will be used instead of the class name
        # in neighbours info
        
        self.name = 'AgenteDB'
        #limite per lo stop dell'agente
        self.maxnoClean = 50
        #contatore mosse senza pulizia
        self.ripet = 0;
        #ultima direzione presa
        self.lastpos = 'GoNorth'
        
        self.visited = [(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0)]# lista caselle visitate 7 el
        self.wall = [(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0)]# lista muri incontrati
        self.ag2visited = [(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0)]# lista caselle visitate dai vicini
        self.coord = (0, 0) # coordinate attuali
        self.cont = 0 #contatore lista visitati
        self.contW = 0 #contatore lista muri
        self.contavv=0 #contatore lista vicini
        
        
        #funzione per stabilire la mossa successiva        
        def nextDir():
            #controllo limitazione della lista dei visitati
            if self.cont==7:
                self.cont=0;
            #estraggo a caso la direzione    
            dir = randint(0,3)
            #controllo che in base alla direzione scelta questa non sia presente ne nei nodi visitati, nei muri o nei nodi 
            #visitati dai vicini. Controlo questo per tutte e 4 le possibili direzioni
            if dir == 0 and (self.coord[0]+1,self.coord[1]) not in self.visited and (self.coord[0]+1,self.coord[1]) not in self.wall and (self.coord[0]+1,self.coord[1]) not in self.ag2visited:
                #aggiorno le coordinate
                self.coord=(self.coord[0]+1,self.coord[1])
                #aggiorno i nodi visitati
                self.visited[self.cont]=(self.coord)
                #aggiorno contatore dei visitati
                self.cont+=1;
                #aggiorno l'ultima direzione presa
                self.lastpos = 'GoEast'
                #ritorno la direzione
                return 'GoEast'
                
            elif dir == 1 and (self.coord[0]-1,self.coord[1]) not in self.visited and (self.coord[0]-1,self.coord[1]) not in self.wall and (self.coord[0]-1,self.coord[1]) not in self.ag2visited:
                
                self.coord=(self.coord[0]-1,self.coord[1])
                self.visited[self.cont]=(self.coord)
                self.cont+=1;
                
                self.lastpos = 'GoWest'
                return 'GoWest'
            elif dir == 2 and (self.coord[0],self.coord[1]+1) not in self.visited and (self.coord[0],self.coord[1]+1) not in self.wall and (self.coord[0],self.coord[1]+1) not in self.ag2visited:
                
                self.coord=(self.coord[0],self.coord[1]+1)
                self.visited[self.cont]=(self.coord) 
                self.cont+=1;
                
                self.lastpos = 'GoNorth'
                return 'GoNorth'
               
            elif dir== 3 and (self.coord[0],self.coord[1]-1) not in self.visited and (self.coord[0],self.coord[1]-1) not in self.wall and (self.coord[0],self.coord[1]-1) not in self.ag2visited:
                
                self.coord=(self.coord[0],self.coord[1]-1)
                self.visited[self.cont]=(self.coord)
                self.cont+=1;
                
                self.lastpos = 'GoSouth'
                return 'GoSouth'
            else: #rilasso i vincoli e permetto di percorrere le caselle già visitate ri-estraendo la posizione
                dir=randint(0,3)
                
            if dir == 0 and (self.coord[0]+1,self.coord[1]) not in self.wall and (self.coord[0]+1,self.coord[1]) not in self.ag2visited:
                
                self.coord=(self.coord[0]+1,self.coord[1])
                #controllo che la casella non ci sia nei nodi visitati per non sprecare memoria
                if self.coord not in self.visited:
                    self.visited[self.cont]=(self.coord)
                    self.cont+=1;
                    
                
                self.lastpos = 'GoEast'
                return 'GoEast'
            elif dir == 1 and (self.coord[0]-1,self.coord[1]) not in self.wall and (self.coord[0]-1,self.coord[1]) not in self.ag2visited:
                
                self.coord=(self.coord[0]-1,self.coord[1])
                if self.coord not in self.visited:
                    self.visited[self.cont]=(self.coord)
                    self.cont+=1;
                    
                
                self.lastpos = 'GoWest'
                return 'GoWest'
                
            elif dir == 2 and (self.coord[0],self.coord[1]+1) not in self.wall and (self.coord[0],self.coord[1]+1) not in self.ag2visited:
                
                self.coord=(self.coord[0],self.coord[1]+1)
                if self.coord not in self.visited:
                    self.visited[self.cont]=(self.coord)
                    self.cont+=1;
                    
                
                self.lastpos = 'GoNorth'
                return 'GoNorth'
               
            elif dir == 3 and (self.coord[0],self.coord[1]-1) not in self.wall and (self.coord[0],self.coord[1]-1) not in self.ag2visited:
                
                self.coord=(self.coord[0],self.coord[1]-1)
                if self.coord not in self.visited:
                    self.visited[self.cont]=(self.coord)
                    self.cont+=1;
                    
                
                self.lastpos = 'GoSouth'
                return 'GoSouth'
                
              		   	
		   
		   
        def program(status, bump, neighbors):
            """Main function of the Agent.

            Params:
                status (string): 'Dirty' or 'Clean'
                bump (string): 'Bump' or 'None'
                neighbors (list of tuples): [
                        ( (agent_id, agent_type), (r_x, r_y) ),
                        ...,
                        ...
                    ]

            Returns:
                 (string): one of these commands:
                            - 'Suck'
                            - 'GoNorth'
                            - 'GoSouth'
                            - 'GoWest'
                            - 'GoEast'
                            - 'NoOp' or 'Noop'

            """
            
            
            

            ##
            # Controllo le posizioni dei vicini e se non sono già presenti le inserisco nella lista
            for (agent_id, agent_class), pos in neighbors:
                if agent_id != self.id:
                    #controllo limitazione lista vicini
                    if self.contavv==7:
                        self.contavv=0
                        
                    vicino=(pos[0]+self.coord[0],pos[1]+self.coord[1])#somma della mia posizione più la relativa del vicino
                    if vicino not in self.ag2visited:
                        self.ag2visited[self.contavv]=vicino;
                        self.contavv+=1

            #controllo se lo stato è sporco in caso do il comando di pulizia e azzero le ripetizioni
            if status=='Dirty':
                self.ripet=0;
               
                return 'Suck'
            elif bump!='Bump':
                #se non ho sbattuto e non sono arrivato al maxripetizioni richiamo la funzione per scegliere la mossa successiva
            	if self.ripet > self.maxnoClean:
            	    return 'NoOp'
            	else:
            	    
            	    
            	    self.ripet+=1
            	    
            	    return nextDir()
            else:
                #ho sbattuto quindi aggiorno la lista dei muri
                	
                #controllo limitazione lista muri	
                if self.contW==7:
                    self.contW=0
                else:
                	
                    self.wall[self.contW]=self.coord;
                    self.contW+=1
                    self.cont-=1

                    #aggiorno le coordinate perchè ho sbattuto e devo tornare indietro
                    if self.lastpos == 'GoNorth':
                        self.coord=(self.coord[0],self.coord[1]-1)
                    elif self.lastpos == 'GoSouth':
                        self.coord=(self.coord[0],self.coord[1]+1)
                    elif self.lastpos == 'GoEast':
                        self.coord=(self.coord[0]-1,self.coord[1])
                    else:
                        self.coord=(self.coord[0]+1,self.coord[1])
                    
                
        self.program = program
