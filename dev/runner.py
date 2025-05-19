from sqlalchemy import create_engine
from dotenv import load_dotenv

from .queries import list_target_tickets, get_ticket_followups, get_ticket_solutions
from pyglpi.comunicator.api import GLPIApiClient
from pyglpi.comunicator.v10_0.endpoints.tickets.core import GlpiTicket
from pyglpi.comunicator.v10_0.endpoints.tickets.itil_folowups import GlpiTicketItilFollowups
from pyglpi.comunicator.v10_0.endpoints.tickets.itil_solutions import GlpiTicketItilSolutions

def get_target_list(engine):
    """Coleta a lista de tickets alvos
    """

    result = engine.execute(list_target_tickets)
    target_tickets = [dict(row) for row in result]

    return target_tickets

def get_ticket_followups(ticket_id, engine):
    """Coleta o último followup público de um ticket
    """
    result = engine.execute(get_ticket_followups.format(ticket_id=ticket_id))
    followups = [dict(row) for row in result]

    if len(followups) > 0:
        followup = followups[0]
    else:
        followup = None
    return followup


def get_ticket_solutions(ticket_id, engine):
    """Coleta a solução de um ticket
    """
    result = engine.execute(get_ticket_solutions.format(ticket_id=ticket_id))
    solutions = [dict(row) for row in result]
    if len(solutions) > 0:
        solution = solutions[0]
    else:
        solution = None
    return solution


def send_ticket_followup(ticket_item, followup, glpi_client):
    """Envia o body do followup para o ticket via GlpiClient
    """



def send_ticket_solution(ticket_item, solution, glpi_client):
    """Envia o body da solução para o ticket via GlpiClient
    """
    ...


def process_ticket(ticket_id, engine):
    """Realiza o procedimento para um ticket

    Checa se ja existe solução, caso tenha envia soluçao, caso não tenha envia followup
    """





def main():
    load_dotenv()
    engine = create_engine('mysql+pymysql://root:root@localhost/glpi')
    connection = engine.connect()

    # Get target tickets
    target_tickets = get_target_list()

    # Initialize GLPI API client
    glpi_client = GLPIApiClient(
        url='http://localhost/glpi/apirest.php',
        app_token='your_app_token',
        user_token='your_user_token'
    )

    glpi_client

    for ticket in target_tickets:
        ticket_id = ticket['id']

        # Process each ticket
        process_ticket(ticket_id, engine)



