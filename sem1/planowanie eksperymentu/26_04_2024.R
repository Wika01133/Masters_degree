#zad1 z zadania4.5
Cyrus=c(171,205,196,169,151,189,223,196,157,188,215,235)
Lipa=c(184,183,209,193,203,194,208,258,221,218,166)
boxplot(list(Cyrus, Lipa),col=55,las=1)
boxplot(list(Cyrus, Lipa),col=55,las=1, horizontal=T)

mean(Cyrus)
mean(Lipa)
shapiro.test(Cyrus)

qqnorm(Cyrus)
qqline(Cyrus)

shapiro.test(Lipa)

t.test(Cyrus,Lipa)

summary(Cyrus)

summary(Lipa)
var(Cyrus);var(Lipa)
var.test(Cyrus,Lipa)

t.test(Cyrus,Lipa)
t.test(Cyrus,Lipa,var.equal = T)

qqplot(Cyrus,Lipa)
abline(0,1)
stripchart(list(Cyrus,Lipa), pch=16)

wilcox.test(Cyrus,Lipa)

ks.test(Cyrus,Lipa)

### zad 1.5 zestaw 4.5 cyrus lipa
cyrus2 = c(Cyrus, Cyrus)
lipa2 = c(Lipa,Lipa)

cyrus2
lipa2
boxplot(list(cyrus2, lipa2),col=55,las=1)
boxplot(list(cyrus2, lipa2),col=55,las=1, horizontal=T)

mean(cyrus2)
mean(lipa2)
shapiro.test(cyrus2)

qqnorm(cyrus2)
qqline(cyrus2)

shapiro.test(lipa2)

t.test(cyrus2,lipa2)

summary(cyrus2)

summary(lipa2)
var(cyrus2);var(lipa2)
var.test(cyrus2,lipa2)

t.test(cyrus2,lipa2)
t.test(cyrus2,lipa2,var.equal = T)

qqplot(cyrus2,lipa2)
abline(0,1)
stripchart(list(cyrus2,lipa2), pch=16)

wilcox.test(cyrus2,lipa2)

ks.test(cyrus2,lipa2)

#zadanie 3, zestaw 4.5
pub=c(4.2,6.1,4.9,8.5,4.6,9.1,7.7,6.5,6.2,10.2,11.6,10.4,5.0, 10.4,8.1)
priv=c(13.0,18.8,13.2,14.4,17.7,17.7,17.6,19.8,16.8,16.1)

boxplot(list(pub,priv),col=55,las=1,horizontal=T)
summary(pub)
summary(priv)

shapiro.test(pub)
shapiro.test(priv)

var.test(priv,pub)

t.test(priv,pub)
t.test(priv,pub,mu=10)
t.test(priv,pub,mu=11)
t.test(priv,pub,mu=10.94)

t.test(priv,pub,mu=11,alternative = c("greater"))

t.test(priv,pub,mu=11,alternative = c("less"))

#zadanie 4 zestaw 4.5
przed=c(0.21,0.12,0.32,0.29,0.3,0.2,0.14) # niezapylona
po=c(0.78,0.76,0.43,0.92,0.86,0.59,0.68) # zapylona

roznica = po-przed
boxplot(przed,po,col=55,las=1)
#??

t.test(przed,po)#nielegalny
t.test(przed,po,paired=T)
t.test(po,przed,paired=T)

wilcox.test(przed,po,paired=T)
shapiro.test((roznica))

t.test(po,przed,paired=T,alternative = "greater")
stripchart(roznica,pch=16)

#zestaw 4 , zadanie 13
przed=c(179, 131, 188, 126, 162, 192, 174, 191, 161, 149, 155, 186,
        213, 158, 192, 186, 169, 169, 185, 141)
po=c(145, 166,179, 189, 155, 163, 168, 141, 143, 169, 153, 148,
     167, 185, 173, 180, 173, 162, 178, 159)

roznica=przed-po

shapiro.test(roznica)
qqnorm(roznica,las=1)
qqline(roznica)

stripchart(roznica,pch=16)
t.test(przed,po)
var(przed);var(po)
t.test(roznica,mu=0)
#powinno byc wiecej


#zestaw 4, zadanie14
n=100
srednia=995
wariancja=36

library(PASWR2)
tsum.test(srednia,sqrt(wariancja),n,mu=1000)
#powinno byc wiecej

#zestaw 4, zadanie 16
dane=c(104, 100, 105, 110, 106, 105, 102, 107, 106, 105)
library(EnvStats)
varTest(dane,sigma.squared=4)

#normalnosc
shapiro.test(dane)


##############?cyrus cos z jedna srednia, badanie? testowanie?
Cyrus
summary(Cyrus)
t.test(Cyrus,mu=200)

walk2 <- function(m)
{
  s=numeric()
  s[1]=sample(c(-1,1),size=1)###p=1/2
  for(i in c(2:m))
  {
    s[i]=s[i-1]+sample(c(-1,1),size=1)
  }
  ind=which(s==0)#indeksy zer
    zmiana=0
    for(i in ind){
      if(((i+1)<=m) &(s[i-1]*s[i+1]<0)){
        zmiana=zmiana+1
      }
    }
  zero=length(which(s==0)) ### liczba zer
  tytul=paste("liczba zer = ",zmiana,"w ",m,"krokach")
  plot(c(0:m),c(0,s),las=1,type="l",main=tytul)
  abline(h=0,col=2)
  return(zmiana)
} 
walk2(1000)

##dzien urodzin
dane=numeric()
for(i in c(1:100000)){
  x=sample(c(1:365),23,replace=T)
  dane[i]=length((unique(x)))
}
dane
dane2=table(dane)
dane2b=dane2/sum(dane2)
dane2b

barplot(dane2b,col=55,las=1)
1-0.49206
