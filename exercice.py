#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	resultat =0
	for letter in text:
		 if str(letter).isalnum():
			 resultat +=1
	return resultat

def get_word_length_histogram(text):
	listMot = text.split()
	nbLettreMot = [get_num_letters(x) for x in listMot]
	resultat = [0]*(max(nbLettreMot)+1)
	for nb in nbLettreMot:
		resultat[nb] += 1
	return resultat


def format_histogram(histogram):
	ROW_CHAR = "*"
	allignement = len(str(len(histogram)-1))
	resultat = [f"{i: >{allignement}} {ROW_CHAR*elem}" for i,elem in enumerate(histogram) if i!=0]
	return str.join("\n",resultat)

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	hauteur = max(histogram)
	largeur = len(histogram)
	histogramHelper = histogram.copy()
	resultat= []
	while max(histogramHelper) !=0:
		str = ""
		for i,elem in enumerate(histogramHelper):
			if i==0:
				continue
			else:
				if elem >= 1:
					str += BLOCK_CHAR
					histogramHelper[i] -=1
				else:
					str += " "
		str += "\n"
		resultat.append(str)

	resultat.reverse()
	histo=""
	for elem in resultat:
		histo += elem

	histo += LINE_CHAR * largeur
	return histo


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
