class Broker:
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        self.projets = []

        self.clients = []

    def affecter_client(self, client):
        self.clients.append(client)

        print(f"{self.nom} est maintenant responsable de {client.nom}")

    def suivre(self, souscription):
        if souscription.client in self.clients:
            
            self.projets.append(souscription)

            print(f"{self.nom} suit la souscription de {souscription.client.nom}")
            
        else:

            print(f"{self.nom} ne peut pas suivre cette souscription : client non affecte")
