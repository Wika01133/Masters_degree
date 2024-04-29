#ZADANIE 1
goale <- c(2, 4, 1, 4, 3, 3, 0, 5, 2, 3, 1, 3, 2, 0, 1, 4, 2, 4, 4, 0, 1, 3, 8, 2, 1, 3, 2, 6, 5, 4, 5, 3, 2, 0, 2, 1, 3, 0, 1, 2, 5, 0, 2, 4, 5)

lambda <- mean(goale)
print(lambda)

prawdopodobienstwa <- dpois(0:max(goale), lambda)

wszystkie_gole <- 0:max(goale)

obserwowane_rozszerzone <- table(factor(goale, levels = wszystkie_gole))

prawdopodobienstwa_norm <- prawdopodobienstwa / sum(prawdopodobienstwa)

test_chi <- chisq.test(obserwowane_rozszerzone, p = prawdopodobienstwa_norm)
print(test_chi)

#######wykres 1
boxplot(goale, col = "lightblue",
        main = "Rozkład liczby goli w meczach",
        xlab = "Liczba goli", ylab = "Liczba meczów")
abline(h = lambda, col = "red", lw = 2)

#######wykres 2
liczba_goli <- names(obserwowane_rozszerzone)
obserwowane_czestosci <- as.numeric(obserwowane_rozszerzone)

barplot(obserwowane_czestosci, names.arg = liczba_goli, col = "lightblue",
        main = "Porównanie obserwowanych i teoretycznych liczb goli w meczach",
        xlab = "Liczba goli", ylab = "Liczba meczów", ylim = c(0,12))
lines(prawdopodobienstwa_norm * sum(obserwowane_rozszerzone), col = "red", lw = 2)



#ZADANIE 2
dane2 <- c(-0.6, 0.12, -0.02, 0.15, 2.1, 0.9, 0.2, -1.7, 1.8, -1.3, -1.64,-4.8, 11.1, 4.34, -0.8, 2.5, -6.9, -2.3, -2.3, 1.0)

ks_test <- ks.test(dane2, "pnorm", mean(dane2), sd(dane2))
ks_test

plot(ecdf(dane2), las=1, xlim=c(-7,12), ylim=c(0,1.1))
arg = seq(-7,12,0.2)
wart = pnorm(arg)
lines(arg,wart,col=55,lwd=2)

shapiro_test <- shapiro.test(dane2)
shapiro_test

# Wykres kwantylowy
qqnorm(dane2)
qqline(dane2, col = 2)


#ZADANIE 3
n1 <- c(34.4, 30.2, 36.5, 30.0, 31.1, 32.5, 30.5, 31.0)
n2 <- c(28.5, 32.0, 32.5, 31.0, 29.0, 30.5, 30.8, 32.2)
n3 <- c(27.5, 29.2, 32.5, 31.0, 30.4, 26.8, 28.0)
n4 <- c(30.6, 28.5, 32.5, 27.0, 28.8, 30.5)

dane3 <- list(n1, n2, n3, n4)

kruskal_test <- kruskal.test(dane3)
kruskal_test

rangi <- rank(unlist(dane3)) 
rangi 

rozmiar <- sapply(dane3, length) 
rozmiar 

srednie <- tapply(rangi, rep(1:4, rozmiar), mean) 
srednie


#ZADANIE 4
probka <- c(16, 53, 289, 75, 94, 643, 27, 48, 78, 95, 154, 192, 634, 421, 15,
            87, 16, 302, 250, 82, 101, 506, 230, 672, 55, 65, 17, 102, 21,
            304, 640, 25, 339, 85, 240, 295, 720, 407, 230, 84, 12, 26, 30,
            458, 370, 483, 610, 75, 300, 435, 92, 180, 405, 26, 315, 40, 532,
            926, 604, 177, 681, 45, 31, 258, 725, 152, 193, 92, 488, 166, 10,
            307, 260, 89, 450, 62, 445, 71, 165, 201, 236, 354, 58, 120, 81,
            710, 42, 310, 345, 127, 476, 620, 160, 23, 28, 60, 366, 470, 92,
            67, 125, 45, 127, 185, 125, 597, 182, 393, 175, 86, 45, 12, 50)

czestosci <- table(factor(as.character(probka), levels = 0:9))
czestosci <- czestosci + 0.1

test_losowosci <- chisq.test(czestosci)
test_losowosci

X <- as.integer(substr(as.character(probka), 1, 1))
Y <- as.integer(substr(as.character(probka), 2, 2))

czestosci_dwuwymiarowe <- table(X, Y)

test_niezaleznosci <- chisq.test(czestosci_dwuwymiarowe)
test_niezaleznosci

#ZADANIE 5
#install.packages("plotrix")
library(plotrix)

library(latticeExtra)

data("USAge.df", package = "latticeExtra")

rok_1961 <- subset(USAge.df, Year == 1961)

przerwy <- c(seq(0, max_age, by = 6), Inf)

etykiety_wiek <- c("0-5","6-11","12-17","18-23","24-29","30-35","36-41",
                   "42-47","48-53","54-59","60-65","66-71","72 i więcej")

rok_1961$AgeGroup <- cut(rok_1961$Age, breaks = przerwy, 
                         labels = etykiety_wiek, right = FALSE)

summary_data <- aggregate(Population ~ AgeGroup + Sex, data = rok_1961, sum)

pyramid.plot(
  summary_data$Population[summary_data$Sex == "Male"], 
  summary_data$Population[summary_data$Sex == "Female"],
  labels = etykiety_wiek,
  top.labels = c("Mężczyźni", "Grupy wiekowe", "Kobiety"),
  main = "Wykres piramidowy dla USA w 1961",
  gap = 3,
  show.values = TRUE, 
  lxcol = 55, 
  rxcol = 66
)



#ZADANIE 6
dlugosc <- c(rep(65.5, 3), rep(68, 14), rep(70, 30), rep(72, 28), rep(74, 18), rep(78, 10))

shapiro.test(dlugosc)

srednia <- mean(dlugosc)
odchylenie <- sd(dlugosc)

srednia
odchylenie

hist(dlugosc, freq = T, main = "Histogram długości tkaniny", xlab = "Długość", ylab = "Gęstość")

qqnorm(dlugosc)
qqline(dlugosc, col = 2)
