# dictionary = {"rev.":"rev."}
# print type(dictionary)
# if isinstance(dictionary,dict):
#     print "yes"
# else:
#     print "no"
#
# print type('') is str
# # for k, v in dict.items():
# #     newKey = k.replace('.', '')
# #     dict[newKey] = dict.pop(k)
# # print dict


PARSE_APP_ID = 'lzb0o0wZHxbgyIHSyZLlooijAK9afoyN8RV4XwcM'
PARSE_SECRET = 'tHZLsIENdHUpZXlfG1AZVLXsETYbgvr5lUorFegP'
PARSE_SERVER_URL = 'https://ptparse.herokuapp.com/parse'
PARSE_REST_KEY = 'YTeYDL8DeSDNsmZT219Lp8iXgPZ24ZGu3ywUjo23'

import json, httplib
connection = httplib.HTTPSConnection('ptparse.herokuapp.com', 443)
connection.connect()
connection.request('GET', '/parse/classes/CongressRequiredEmailFields','',
                   {
                       "X-Parse-Application-Id": PARSE_APP_ID,
                       "X-Parse-REST-API-Key": PARSE_REST_KEY,
                       "Content-Type": "application/json"
                   })
result = json.loads(connection.getresponse().read())
field_list_objects = result['results']
# print "get fields", required_fields

#
# field_list = []
# for required_field_list in field_list_objects:
#     print "required fields:", required_field_list['required_fields']
#     for field in required_field_list['required_fields']:
#         print field['value']
#         field_list.append(field['value'])
#
# print field_list
# print "printing set"
# print set(field_list)
# json.loads()



ordered_array = []
# for ordered_item in master_ordered_list:
for field_list_object in field_list_objects:
    # print field_list_object
    bioguideId = field_list_object['bioguideId']

    for field in field_list_object['required_fields']:
        # if field['value'] == ordered_item:
        try:
            options_length = len(field['options_hash'])
        except:
            options_length = 0
        temp_dict = {
            "value": field['value'],
            "bioguideId": bioguideId,
            "maxlength": field['maxlength'],
            "options_hash": field['options_hash'],
            "options_length": options_length
            }
        ordered_array.append(temp_dict)


import operator
sorted_array = sorted(ordered_array, key=operator.itemgetter('value','options_length'))
# print sorted_array
print len(sorted_array)

#  Strip out extra duplictes, group bioguide IDs
count = 0
length = len(sorted_array)
sorted_clip = []
previous_item = "A"
for item in sorted_array:
    count = count + 1
    if count != length:
        if previous_item == "A":
            previous_item = item
        elif previous_item['value'] == 'TOPIC':
            sorted_clip.append(previous_item)
            previous_item = item
        elif item['value'] != previous_item['value']:
            sorted_clip.append(previous_item)
            previous_item = item
        elif item['value'] == previous_item['value']:
            previous_item['bioguideId'] = previous_item['bioguideId'] + ' ' + item['bioguideId']
    elif count == length: # behavior different if last in list
        if previous_item['value'] == 'TOPIC':
            sorted_clip.append(previous_item)
            sorted_clip.append(item)
        elif item['value'] != previous_item['value']:
            sorted_clip.append(previous_item)
            sorted_clip.append(item)
        elif item['value'] == previous_item['value']:
            sorted_clip.append(previous_item)

# print len(sorted_clip)
# print sorted_clip

# order them
master_ordered_list = [
    "MESSAGE",
    "NAME_PREFIX",
    "NAME_FIRST",
    "NAME_LAST",
    "EMAIL",
    "PHONE",
    "ADDRESS_STREET",
    "ADDRESS_CITY",
    "ADDRESS_ZIP4",
    "ADDRESS_ZIP5",
    "SUBJECT",
    "TOPIC",
]

# separate into those to order and those to put at end
objects_to_end = []
objects_to_order = []
for item in sorted_clip:
    found = False
    for list_item in master_ordered_list:
        if item['value'] == list_item:
            found = True
    if found:
        objects_to_order.append(item)
    elif not found:
        objects_to_end.append(item)

# order the list to be ordered based on master list
ordered_objects = []
for list_item in master_ordered_list:
    print list_item
    for object_item in objects_to_order:
        print "testing against:", object_item['value']
        if object_item['value'] == list_item:
            ordered_objects.append(object_item)
            print "appending object:"
        else:
            print "exception"

if len(ordered_objects) != 0:
    ordered_objects = ordered_objects + objects_to_end
print len(objects_to_order)
print len(ordered_objects)
print ordered_objects
#


























