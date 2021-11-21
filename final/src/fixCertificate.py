import pandas as pd

#Trata classificações indicativas em formato americano
def handleCertificate(certificate):
    if(certificate=='TV-MA' or certificate=='R' or certificate=='NR' or certificate=='NC-17'):
        return '18+'
    elif(certificate=='TV-14'):
        return '16+'
    elif(certificate=='PG-13'):
        return '13+'
    elif(certificate=='PG' or certificate=='TV-Y7' or certificate=='TV-Y7-FV' or certificate=='TV-PG'):
        return '7+'
    elif(certificate=='G' or certificate=='TV-G' or certificate=='TV-Y'):
        return 'all'
    elif(certificate=='Not Rated'):
        return ''
    else:
        return certificate

new = pd.read_csv('data/new/series2.0.csv',converters={'Classificacao Indicativa':handleCertificate})
new.to_csv("data/new/seriesclassificacao.csv", index=False)