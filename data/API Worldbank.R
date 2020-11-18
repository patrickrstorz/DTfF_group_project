# API Worldbank 

install.packages('WDI')

library(WDI)
library(remotes)
install_github('vincentarelbundock/WDI')


WDIsearch('Central government debt')



data = WDI(indicator= c('NY.GDP.PCAP.KD', 'GC.DOD.TOTL.CN'), country=c('CH','DE','US'), start=1980, end=2015)

write.csv2(dat, "data/data.csv", row.names = FALSE)


