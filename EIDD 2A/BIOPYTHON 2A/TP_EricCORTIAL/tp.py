from Bio import Seq, SeqIO, SeqRecord, motifs
from Bio import Seq
import random as rd
from IPython.display import Image, display
from math import log
from joblib import Parallel, delayed
import multiprocessing


MET = SeqIO.parse(open("MET_up800.fasta", "r"), "fasta")
YAP = SeqIO.parse(open("YAP_up800.fasta", "r"), "fasta")
MET_Seq = [rec for rec in MET]
YAP_Seq = [rec for rec in YAP]
motifYAP1 = motifs.read(open("MA0386.1.pfm", "r"), "jaspar")
motifSPT15 = motifs.read(open("MA0415.1.pfm", "r"), "jaspar")
print(motifYAP1)
print(motifSPT15)

# identification des oligomères dans les séquences :

MET_TATA = 0
MET_CGGC = 0
MET_len = 0
YAP_TATA = 0
YAP_CGGC = 0
YAP_len = 0

for seqRecord in MET_Seq:
    seq = seqRecord.seq
    MET_TATA += seq.count('TATA')
    MET_CGGC += seq.count('CGGC')
    MET_len += len(seq)

for seqRecord in YAP_Seq:
    seq = seqRecord.seq
    YAP_TATA += seq.count('TATA')
    YAP_CGGC += seq.count('CGGC')
    YAP_len += len(seq)

print("TATA est comptée dans MET "+str(MET_TATA)+ " fois")
print("CGGC est comptée dans MET "+str(MET_CGGC)+ " fois")
print("TATA est comptée dans YAP "+str(YAP_TATA)+ " fois")
print("CGGC est comptée dans YAP "+str(YAP_CGGC)+ " fois\n")

# shuffling sur 1000 seq :

# fichier1 = open("valeurs_MET.txt","w")

# for i in range(1000):
#     MET_TATA = 0
#     MET_CGGC = 0
#     for seqRecord in MET_Seq:
#         seq = seqRecord.seq
#         seq1= seq.tomutable()
#         rd.shuffle(seq1)
#         MET_TATA += seq1.count('TATA')
#         MET_CGGC += seq1.count('CGGC')
#     fichier1.write(str(MET_TATA)+'\t'+str(MET_CGGC)+ '\n')

# fichier1.close()


# fichier2 = open("valeurs_YAP.txt","w")

# for i in range(1000):
#     YAP_TATA = 0
#     YAP_CGGC = 0
#     for seqRecord in YAP_Seq:
#         seq = seqRecord.seq
#         seq1= seq.tomutable()
#         rd.shuffle(seq1)
#         YAP_TATA += seq1.count('TATA')
#         YAP_CGGC += seq1.count('CGGC')
#     fichier2.write(str(YAP_TATA)+'\t'+str(YAP_CGGC)+ '\n')

# fichier2.close()


# création des logos pour les motifs :
motifYAP1.weblogo("YAP1_Motif_Logo.png")
motifSPT15.weblogo("SPT15_Motif_Logo.png")

# Then display them:
display(Image(filename = "YAP1_Motif_Logo.png", width = 500, height = 300))
display(Image(filename = "SPT15_Motif_Logo.png", width = 500, height = 300))

# modification des matrices :
motifYAP1_pfm = motifYAP1.counts
motifSPT15_pfm = motifSPT15.counts

motifYAP1_pssm = motifYAP1_pfm.normalize(pseudocounts = {'A':0.31, 'C':0.19, 'G':0.19, 'T':0.31})
motifSPT15_pssm = motifSPT15_pfm.normalize(pseudocounts = {'A':0.31, 'C':0.19, 'G':0.19, 'T':0.31})

# print(motifYAP1_pssm)
# print(motifSPT15_pssm)

motifYAP1_pwm = motifYAP1_pssm.log_odds(background = {'A':0.31, 'C':0.19, 'G':0.19, 'T':0.31})
motifSPT15_pwm = motifSPT15_pssm.log_odds(background = {'A':0.31, 'C':0.19, 'G':0.19, 'T':0.31})
print(motifYAP1_pwm)
print(motifSPT15_pwm)

scores_MET_YAP1 = []
scores_MET_SPT15 = []

scores_YAP_YAP1 = []
scores_YAP_SPT15 = []

def calculate_motif_scores(seq_reqs, pwm):
    """Return the list of motif scores for each SeqRecord in the seq_recs list"""
    motif_scores = []
    for seq_rec in seq_reqs:
        seq_rec.seq.alphabet = pwm.alphabet 
        motif_scores.append(pwm.calculate(seq_rec.seq)) 
    return motif_scores

scores_MET_YAP1 = calculate_motif_scores(MET_Seq, motifYAP1_pwm)
scores_MET_SPT15 = calculate_motif_scores(MET_Seq, motifSPT15_pwm)
scores_YAP_YAP1 = calculate_motif_scores(YAP_Seq, motifYAP1_pwm)
scores_YAP_SPT15 = calculate_motif_scores(YAP_Seq, motifSPT15_pwm)

def calculate_motif_hits(seq_reqs, pwm, thres):
    """Return the totalnumber of hits of a motif on a list of SeqRecords given a threshold."""
    hits = 0
    all_scores = calculate_motif_scores(seq_reqs, pwm)
    for rec_scores in all_scores:
        for pos_score in rec_scores:
            if pos_score >= thres:
                hits += 1
    return hits

# Threshold = 1
# MET - YAP1
hits_MET_YAP1 = calculate_motif_hits(MET_Seq, motifYAP1_pwm, 1)
print("YAP1 hits, MET seqs, threshold 1: {}".format(hits_MET_YAP1))
# MET - SPT15
hits_MET_SPT15 = calculate_motif_hits(MET_Seq, motifSPT15_pwm, 1)
print("STP15 hits, MET seqs, threshold 1: {}".format(hits_MET_SPT15))
# YAP - YAP1
hits_YAP_YAP1 = calculate_motif_hits(YAP_Seq, motifYAP1_pwm, 1)
print("YAP1 hits, YAP seqs, threshold 1: {}".format(hits_YAP_YAP1))
# YAP - SPT15
hits_YAP_SPT15 = calculate_motif_hits(YAP_Seq, motifSPT15_pwm, 1)
print("SPT15 hits, YAP seqs, threshold 1: {}".format(hits_YAP_SPT15))


num_cores = multiprocessing.cpu_count()

def randomise_SeqRecords(recs):
    """recs is a list of Bio:SeqRecords."""
    rnd_recs = []
    for rec in recs:
        rnd_seq = rec.seq.tomutable()
        rd.shuffle(rnd_seq)
        # Attention au SeqRecord.SeqRecord sinon erreur : 'module' object is not callable
        rnd_recs.append(SeqRecord.SeqRecord(rnd_seq.toseq())) 
    return rnd_recs
    

randomSeqs_MET = Parallel(n_jobs = num_cores)(delayed(randomise_SeqRecords)(MET_Seq) for i in range(1000))
randomSeqs_YAP = Parallel(n_jobs = num_cores)(delayed(randomise_SeqRecords)(YAP_Seq) for i in range(1000))
hits_MET_YAP1_1_RANDOM = Parallel(n_jobs = num_cores)(delayed(calculate_motif_hits)(randomSeqs_MET[i], motifYAP1_pwm, thres = 1) for i in range(1000))
hits_MET_SPT15_1_RANDOM = Parallel(n_jobs = num_cores)(delayed(calculate_motif_hits)(randomSeqs_MET[i], motifSPT15_pwm, thres = 1) for i in range(1000))
hits_YAP_YAP1_1_RANDOM = Parallel(n_jobs = num_cores)(delayed(calculate_motif_hits)(randomSeqs_YAP[i], motifYAP1_pwm, thres = 1) for i in range(1000))
hits_YAP_SPT15_1_RANDOM = Parallel(n_jobs = num_cores)(delayed(calculate_motif_hits)(randomSeqs_YAP[i], motifSPT15_pwm, thres = 1) for i in range(1000))

# Printing the results in a file
with open('METseq_YAP1motif_RandomSeq_Hits_Threshold_1.txt', 'w') as f:
    for item in hits_MET_YAP1_1_RANDOM:
        f.write("%s\n" % item)
with open('METseq_SPT15motif_RandomSeq_Hits_Threshold_1.txt', 'w') as f:
    for item in hits_MET_SPT15_1_RANDOM:
        f.write("%s\n" % item)
with open('YAPseq_YAP1motif_RandomSeq_Hits_Threshold_1.txt', 'w') as f:
    for item in hits_YAP_YAP1_1_RANDOM:
        f.write("%s\n" % item)
with open('YAPseq_SPT15motif_RandomSeq_Hits_Threshold_1.txt', 'w') as f:
    for item in hits_YAP_SPT15_1_RANDOM:
        f.write("%s\n" % item)

