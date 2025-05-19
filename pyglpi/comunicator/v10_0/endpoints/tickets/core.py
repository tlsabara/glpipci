from pyglpi.comunicator.v10_0.api import GLPIApiClient

CONTEXT_URI_PATTERN = "/Ticket"

class GlpiTicket:
    """
    Class to manage a ticket in GLPI.
    """
    def __init__(self, ticket_id: str, api_client: GLPIApiClient) -> None:
        self.ticket_id = ticket_id
        self.api_client = api_client
        self.api_object_endpoint = f"/{CONTEXT_URI_PATTERN}/{self.ticket_id}"

        # TODO: Trazer os atributod de um ticket para esta classe

    def get_ticket(self) -> dict:
        """
        Get the ticket details.
        """
        response = self.api_client.get(self.api_object_endpoint, headers=self.api_client.auth_headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")


class GlpiTickets:
    """
    Class to manage tickets in GLPI.
    """

    def __init__(self) -> None:
        ...

    def get_tickets(self) -> list[dict]:
        """
        Get the lifst of tickets.
        """
        endpoint = self.api_object_endpoint + CONTEXT_URI_PATTERN
        response = self._api_client.get(endpoint, headers=self.auth_headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
