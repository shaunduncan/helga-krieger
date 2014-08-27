from helga.plugins import command


@command('krieger', aliases=['kreiger'], help='film film FILM FILM FILM! FILM!! FILM!!!')
def krieger(client, channel, nick, message, cmd, args):
    """
    film film FILM FILM FILM! FILM!! FILM!!!
    """
    fmt = '{0} {0} {1} {1} {1}! {1}!! {1}!!!'
    try:
        word = args[0]
    except IndexError:
        word = 'film'
    return fmt.format(word.lower(), word.upper())
