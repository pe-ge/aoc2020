import re

data = open("input.txt").read().split("\n\n")


def verify_ticket_field(ticket_field, constraints):
    for num_constraint, constraint in enumerate(constraints[::2]):
        if matches_constraint(ticket_field, constraint):
            return True

    return False


def matches_constraint(ticket_field, constraint):
    for min_value, max_value in constraint:
        if min_value <= ticket_field <= max_value:
            return True

    return False


def find_valid_columns(valid_tickets, column_idx, constraints):
    columns = set(range(len(constraints)))
    for ticket in valid_tickets:
        for num_constraint, constraint in enumerate(constraints):
            if not matches_constraint(ticket[column_idx], constraint):
                if num_constraint in columns:
                    columns.remove(num_constraint)

    return columns


# parse constraints
constraints = []
for raw_constraint in data[0].split("\n"):
    parsed_constraint = list(map(int, re.findall(r"\d+", raw_constraint)))
    constraints.append(list(zip(parsed_constraint[:-1:2], parsed_constraint[1::2])))

# select valid tickets
valid_tickets = []
for nearby_ticket in data[2].split("\n")[1:]:
    is_valid = True
    ticket = list(map(int, nearby_ticket.split(",")))
    for ticket_field in ticket:
        if not verify_ticket_field(ticket_field, constraints):
            is_valid = False
            break

    if is_valid:
        valid_tickets.append(ticket)

# assign matching constraints to columns
unpruned_columns = []
for column_idx in range(len(constraints)):
    unpruned_columns.append(find_valid_columns(valid_tickets, column_idx, constraints))

# prune constraints so each column has exactly one constraint
column_to_constraint = {}
while True:
    prune_completed = True
    for idx, valid_columns in enumerate(unpruned_columns):
        if len(valid_columns) == 1:
            valid_column = valid_columns.pop()
            column_to_constraint[valid_column] = idx
            prune_completed = False
            break

    if prune_completed:
        break
    for valid_columns in unpruned_columns:
        if valid_column in valid_columns:
            valid_columns.remove(valid_column)

# parse my ticket
my_ticket = list(map(int, data[1].split("\n")[1].split(",")))

# select all "departure" fields which are first 6 in the input
result = 1
for column in range(6):
    result *= my_ticket[column_to_constraint[column]]

print(result)
