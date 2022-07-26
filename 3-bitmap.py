import sys

bitmap = """
....................................................................
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                      ***                                       *    *
                    ****              **                 *******   *
                     **     *          fff          *
 ...................................................................."""

print('Bitmapowa wiadomość')
print('Wpisz waidoość, którą chcesz wyświetlić w postaci bitmapy.')
message = input('> ')
if message == '':
    sys.exit()

# Pętla przechodząca przez każdą linijkę bitmapy
for line in bitmap.splitlines():
    # Pętla przechodząca przez każdy znak w linijce
    for i, bit in enumerate(line):
        if bit == ' ':
            # Wyświtlanie spacji w pustych polach bitmapy
            print(' ', end='')
        else:
            # Wyświetlanie znaku wiadomości
            print(message[i % len(message)], end='')
    print()  # Przejście do nowej linii