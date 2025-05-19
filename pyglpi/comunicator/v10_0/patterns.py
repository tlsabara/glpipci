class GlpiApiBodies:

    def create_solution_body(self, ticket_id, solution):
        return {
        # "id": 916,
        "itemtype": "Ticket",
        "items_id": 9091,
        "solutiontypes_id": 0,
        "solutiontype_name": None,
        "content": "&#60;p&#62;Solução aplicada&#60;/p&#62;",
        "date_creation": "2025-04-12 05:29:09",
        "date_mod": "2025-04-12 05:29:09",
        "date_approval": None,
        "users_id": 38256,
        "user_name": None,
        "users_id_editor": 0,
        "users_id_approval": 0,
        "user_name_approval": None,
        "status": 2,
        "itilfollowups_id": None,
    }

    def create_followup_body(self, ticket_id, followup):
        return  {
        # "id": 1423,
        "itemtype": "Ticket",
        "items_id": 9091,
        "date": "2025-04-12 03:56:47",
        "users_id": 38256,
        "users_id_editor": 0,
        "content": "&#60;p&#62;Teste thiago-localhost-prod&#60;/p&#62;",
        "is_private": 0,
        "requesttypes_id": 1,
        "date_mod": "2025-04-12 03:56:47",
        "date_creation": "2025-04-12 03:56:47",
        "timeline_position": 4,
        "sourceitems_id": 0,
        "sourceof_items_id": 0,

    }



