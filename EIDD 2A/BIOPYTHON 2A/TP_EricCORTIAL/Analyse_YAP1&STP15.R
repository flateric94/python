library(ggplot2)

Shuffle.YAP1.MET <- read.table("METseq_YAP1motif_RandomSeq_Hits_Threshold_1.txt")$V1
Shuffle.STP15.MET <- read.table("METseq_SPT15motif_RandomSeq_Hits_Threshold_1.txt")$V1
Shuffle.YAP1.YAP <- read.table("YAPseq_YAP1motif_RandomSeq_Hits_Threshold_1.txt")$V1
Shuffle.STP15.YAP <- read.table("YAPseq_SPT15motif_RandomSeq_Hits_Threshold_1.txt")$V1

YAP1.MET <- 90
STP15.MET <- 19
YAP1.YAP <- 80
STP15.YAP <- 23

Shuffle <- as.data.frame(cbind(Shuffle.YAP1.MET, Shuffle.STP15.MET, Shuffle.YAP1.YAP, Shuffle.STP15.YAP))
names(Shuffle) <- c("threshold_1_YM", "threshold_1_SM", "threshold_1_YY", "threshold_1_SY")


# Threshold = 1

ggplot(Shuffle, aes(threshold_1_YM)) + geom_histogram(binwidth = 1, color="darkred", fill="white") + theme_bw() + labs(title="occurences of YAP1 motif, shuffling model", x="number of occurences", y="number of sequences") + geom_vline(xintercept = YAP1.MET, linetype="dashed", col="darkblue", size=2)
ggplot(Shuffle, aes(threshold_1_SM)) + geom_histogram(binwidth = 1, color="darkred", fill="white") + theme_bw() + labs(title="occurences of YAP1 motif, shuffling model", x="number of occurences", y="number of sequences") + geom_vline(xintercept = STP15.MET, linetype="dashed", col="darkblue", size=2)
ggplot(Shuffle, aes(threshold_1_YY)) + geom_histogram(binwidth = 1, color="darkred", fill="white") + theme_bw() + labs(title="occurences of YAP1 motif, shuffling model", x="number of occurences", y="number of sequences") + geom_vline(xintercept = YAP1.YAP, linetype="dashed", col="darkblue", size=2)
ggplot(Shuffle, aes(threshold_1_SY)) + geom_histogram(binwidth = 1, color="darkred", fill="white") + theme_bw() + labs(title="occurences of YAP1 motif, shuffling model", x="number of occurences", y="number of sequences") + geom_vline(xintercept = STP15.YAP, linetype="dashed", col="darkblue", size=2)

# YAP1 - MET

mean_Shuffle.YAP1.MET <- mean(Shuffle$threshold_1_YM)
sd_Shuffle.YAP1.MET <- sd(Shuffle$threshold_1_YM)

z_Shuffle.YAP1.MET <- (YAP1.MET - mean_Shuffle.YAP1.MET) / sd_Shuffle.YAP1.MET

Pval_Shuffle.YAP1.MET <- pnorm(z_Shuffle.YAP1.MET, lower.tail = FALSE)
print(z_Shuffle.YAP1.MET)
print(Pval_Shuffle.YAP1.MET)

# STP15 - MET

mean_Shuffle.STP15.MET <- mean(Shuffle$threshold_1_SM)
sd_Shuffle.STP15.MET <- sd(Shuffle$threshold_1_SM)

z_Shuffle.STP15.MET <- (STP15.MET - mean_Shuffle.STP15.MET) / sd_Shuffle.STP15.MET

Pval_Shuffle.STP15.MET <- pnorm(z_Shuffle.STP15.MET, lower.tail = FALSE)
print(z_Shuffle.STP15.MET)
print(Pval_Shuffle.STP15.MET)

# YAP1 - YAP

mean_Shuffle.YAP1.YAP <- mean(Shuffle$threshold_1_YY)
sd_Shuffle.YAP1.YAP <- sd(Shuffle$threshold_1_YY)

z_Shuffle.YAP1.YAP <- (YAP1.YAP - mean_Shuffle.YAP1.YAP) / sd_Shuffle.YAP1.YAP

Pval_Shuffle.YAP1.YAP <- pnorm(z_Shuffle.YAP1.YAP, lower.tail = FALSE)
print(z_Shuffle.YAP1.YAP)
print(Pval_Shuffle.YAP1.YAP)

# STP15 - YAP

mean_Shuffle.STP15.YAP <- mean(Shuffle$threshold_1_SY)
sd_Shuffle.STP15.YAP <- sd(Shuffle$threshold_1_SY)

z_Shuffle.STP15.YAP <- (STP15.YAP - mean_Shuffle.STP15.YAP) / sd_Shuffle.STP15.YAP

Pval_Shuffle.STP15.YAP <- pnorm(z_Shuffle.STP15.YAP, lower.tail = FALSE)
print(z_Shuffle.STP15.YAP)
print(Pval_Shuffle.STP15.YAP)
