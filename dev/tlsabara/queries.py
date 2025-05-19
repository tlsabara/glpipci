list_target_tickets = """
select 
    id,
    status,
    date_creation
from glpi_tickets
where status <> 6
  and status <> 1
  and date_creation between '2025-04-01' and '2025-04-13'
"""


get_ticket_followups = """
select
    t1.id,
    t1.is_private,
    t1.content,
    t1.users_id
from glpi_itilfollowups t1
left join glpi_tickets_users t2 on t1.items_id = t2.tickets_id and t1.users_id = t2.users_id and t2.type <> 1
where t1.itemtype = "Ticket"
  and t1.items_id = {ticket_id}
  and t1.is_private = 0
  and t1.users_id <> 0
order by 1 desc
limit 1
"""

get_ticket_solutions = """
select *
from glpi_itilsolutions
where itemtype = "Ticket"
  and items_id = {ticket_id}
"""
