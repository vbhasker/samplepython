ip_address = input('Enter the ip address:')

if ip_address:
    no_of_segments = 1
    segment = ''
    for index in range(0, len(ip_address)):
        if ip_address[index] not in '.':
            segment += ip_address[index]
        else:
            print('Length of segment {0} is {1}'.format(segment, len(segment)))
            no_of_segments += 1
            segment = ''

    print('Length of segment {0} is {1}'.format(segment, len(segment)))
    print('Total segments: {}'.format(no_of_segments))
else:
    print('No input was provided')
