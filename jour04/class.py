class Participant:

    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def afficherParticipant(self):
        print('Name:  {}, Tickets: {}'.format(self.name, self.tickets))

    def ajouterTicket(self):
        self.tickets +=1
        print('{} passe à {} tickets'.format(self.name, self.tickets))


participant1 = Participant('John', 2)
participant2 = Participant('Marc', 4)

participant1.ajouterTicket()
participant2.ajouterTicket()

participant1.afficherParticipant()
participant2.afficherParticipant()
