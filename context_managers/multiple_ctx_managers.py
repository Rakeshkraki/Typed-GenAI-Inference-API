# enter input
#     ↓
# enter output
#     ↓
# execute block
#     ↓
# exit output
#     ↓
# exit input

with open("data.txt", 'r') as input_file, open("logs.txt", 'w') as output_file:
    data = input_file.read()
    output_file.write(data)
