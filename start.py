print(' -- Configure for -- ')
print('[1] - Lightshot')
print('[2] - Sendspace (Not working well)')
print('[3] - Wetransfer (Not working')
print('[4] - Imgur')

config = input(" > ")

if config == 'none':
    thelink = input('Add the link: ')
    letters = int(input('How many letters ? '))
    case = input('Lowercase or Uppercase or both ? l/u/b')
    numbers = int(input('How many numbers ? '))
    randomcheck = input('Shuffle ? y/n ')
    scan = input("Element to scan ? ")
    logs_name = input("Enter the name of the log file")
    extension = input('Extension')
    save_img = input('Do you want to save the image ?')

    if screenshot == 'y':
        file = input("Folder for screenshots (pictures/filename): ")

if config == '1':
    thelink = 'https://prnt.sc/'
    letters = int(3)
    case = 'l'
    numbers = int(3)
    randomcheck = 'y'
    img_position = 0
    file = "pictures/lightshot/"
    logs_name = 'lightshot_logs'
    tag_scan = 1
    save_img = 'y'


if config == '2':
    thelink = 'https://www.sendspace.com/file/'
    letters = int(4)
    case = 'l'
    numbers = int(2)
    randomcheck = 'y'
    img_position = 0
    file = "pictures/sendspace/"
    logs_name = 'sendspace_logs'
    save_img = 'n'
    tag_scan = 2

if config == '3':
    thelink = 'https://we.tl/t-'
    letters = int(10)
    case = 'b'
    numbers = int(0)
    randomcheck = 'y'
    img_position = 0
    file = "pictures/wetransfer/"
    logs_name = 'wetransfer_logs'
    save_img = 'n'
    tag_scan = 3

if config == '4':
    thelink = "https://imgur.com/iPP0bpw"
    letters = int(6)
    case = 'b'
    numbers = int(1)
    randomcheck = 'y'
    img_position = 0
    file = "pictures/imgur/"
    logs_name = 'imgur_logs'
    save_img = 'y'
    tag_scan = 4



