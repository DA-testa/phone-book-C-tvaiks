# python3
# Mareks Siņica-Siņavskis 221RDB430

class Contact:
    def __init__(self, number, name):
        self.number = number
        self.name = name

def read_queries():
    n = int(input())
    return [input().split() for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = {}
    for query in queries:
        query_type = query[0]
        if query_type == 'add':
            number = query[1]
            name = query[2]
            contacts[number] = Contact(number, name)
        elif query_type == 'del':
            number = query[1]
            if number in contacts:
                del contacts[number]
        else:
            number = query[1]
            response = contacts.get(number)
            if response:
                result.append(response.name)
            else:
                result.append('not found')
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
