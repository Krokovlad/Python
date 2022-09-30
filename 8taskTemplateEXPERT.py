def main(s : str) -> dict:
    res = dict()

    begin = s.find('(')

    while begin != -1:
        end = s[begin + 1:].find(')') + begin
        word = s[begin + 1:end + 1].split(';')

        for i in range(len(word)):
            word[i] = word[i].strip().replace('`', '')

        begin = s.find('=:') + 1
        end = s[begin + 1:].find('.') + begin
        num = s[begin + 1: end + 1].strip()

        res[num] = word
        s = s[end + 1:]
        begin = s.find('(')

    return res

s = """do<sect> new#( `onan_653 ;`edle_964)=: rare.</sect>, <sect> new
#(`maat; `ordi_429) =:biza_415. </sect>, <sect> new #(`aned ;
`arma_795 ;`quoror ; `dilela_485 ) =: beines. </sect>, <sect> new
#(`onatma ; `xedi_138 ; `tianat) =: isus_130.</sect>,od"""

print(main(s))