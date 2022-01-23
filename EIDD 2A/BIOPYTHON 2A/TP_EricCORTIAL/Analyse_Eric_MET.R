# Calcul de la p-value pour le shuffling :

### Dans MET

# Loading the results
Shuffle.TATA <- read.table("valeurs_MET.txt", h=F, sep="\t", stringsAsFactors = F)$V1
Shuffle.CGGC <- read.table("valeurs_MEt.txt", h=F, sep="\t", stringsAsFactors = F)$V2
Lambda.TATA <- 78
Lambda.CGGC <- 13
Shuffle <- as.data.frame(cbind(Shuffle.TATA, Shuffle.CGGC))
names(Shuffle) <- c("TATA", "CGGC")

library(ggplot2)
# Oligomère TATA
ggplot(Shuffle, aes(TATA)) + geom_histogram(binwidth = 1, color="darkred", fill="white") + theme_bw() + labs(title="occurences of TATA, shuffling model", x="number of occurences", y="number of sequences") + geom_vline(xintercept = Lambda.TATA, linetype="dashed", col="darkblue", size=2)

# Computing the z-score
mean_TATA_Shuffle <- mean(Shuffle$TATA)
sd_TATA_Shuffle <- sd(Shuffle$TATA)

z_TATA_Shuffle <- (Lambda.TATA - mean_TATA_Shuffle) / sd_TATA_Shuffle

# Computing the probability associated with the z-score (P(Zâ‰¤z_score)
Pval_TATA_Shuffle <- pnorm(z_TATA_Shuffle)
print(z_TATA_Shuffle)
print(Pval_TATA_Shuffle)


# oligomère CGGC
ggplot(Shuffle, aes(CGGC)) + geom_histogram(binwidth = 1, color="darkred", fill="white") + theme_bw() + labs(title="occurences of CGGC, shuffling model", x="number of occurences", y="number of sequences") + geom_vline(xintercept = Lambda.CGGC, linetype="dashed", col="darkblue", size=2)

# Computing the z-score
mean_CGGC_Shuffle <- mean(Shuffle$CGGC)
sd_CGGC_Shuffle <- sd(Shuffle$CGGC)

z_CGGC_Shuffle <- (Lambda.CGGC - mean_CGGC_Shuffle) / sd_CGGC_Shuffle

# Computing the probability associated with the z-score (P(Zâ‰¤z_score)
Pval_CGGC_Shuffle <- pnorm(z_CGGC_Shuffle)
print(z_CGGC_Shuffle)
print(Pval_CGGC_Shuffle)
