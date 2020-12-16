import re

data = open("input.txt").read().split("\n\n")


def verify_ticket_field(ticket_field, constraints):
    for min_value, max_value in constraints:
        if min_value <= ticket_field <= max_value:
            return True

    return False


constraints = []
for raw_constraint in data[0].split("\n"):
    parsed_constraint = list(map(int, re.findall("\d+", raw_constraint)))
    constraints.extend(zip(parsed_constraint[:-1:2], parsed_constraint[1::2]))

invalid_ticket_fields = []
for nearby_ticket in data[2].split("\n")[1:]:
    ticket_fields = map(int, nearby_ticket.split(","))
    for ticket_field in ticket_fields:
        if not verify_ticket_field(ticket_field, constraints):
            invalid_ticket_fields.append(ticket_field)

print(sum(invalid_ticket_fields))
