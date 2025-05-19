from comunicator.v10_0.endpoints.tickets.core import GlpiTicket


CONTEXT_URI_PATTERN = "/ITILFollowup"


class GlpiTicketItilFollowups:

    def __init__(self, ticket_instance: GlpiTicket) -> None:
        self.ticket_instance = ticket_instance

    def get_itil_followups(self) -> list[dict]:
        """
        Get the list of ITIL followups for a ticket.
        """
        endpoint = self.ticket_instance.api_object_endpoint + CONTEXT_URI_PATTERN
        response = self.ticket_instance.api_client.make_get(
            endpoint,
            headers=self.ticket_instance.api_client.auth_headers
        )
        if response.status_code == 200:
            return response.json()
        else:
            self.ticket_instance.api_client.request_error_handler(
                status_code=response.status_code,
                message=response.text
            )

    def add_itil_followup(self, itil_followup: dict) -> dict:
        """
        Add a new ITIL followup for a ticket.

        TODO: Implement to change from dict to specific class
        """
        endpoint = self.ticket_instance.api_object_endpoint + CONTEXT_URI_PATTERN
        response = self.ticket_instance.api_client.make_post(
            endpoint,
            headers=self.ticket_instance.api_client.auth_headers,
            json=itil_followup
        )
        if response.status_code == 200:
            return response.json()
        else:
            self.ticket_instance.api_client.request_error_handler(
                status_code=response.status_code,
                message=response.text
            )
