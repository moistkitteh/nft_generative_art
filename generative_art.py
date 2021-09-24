import numpy as np
import random
import PIL as pl
from PIL import Image, ImageDraw, ImageFilter
import os
	#Code Dependencies
	#Code Libraries/Packages
	# python3 --> sudo apt-get update
	#	      sudo apt-get install python3.8
	# PIL     --> python3 -m pip install --upgrade Pillow
	# random  --> (installed with python3)
	#Files
	#  weights.dat -- list of all of the desired weights for each trait
	#Directories
	#  images/ -- directory to store generated images [name changeable]
	#  traits/ -- directory that traits will be picked up from. Layers will be added alphabetically/numerical by directory name
	#User Set Variables
        #  nf -- final number of art pieces you want
	#  tl[t,[c,[[loc1,w1],[loc2,w2]]] -- number of traits, number of choices for each trait, locs, weights for each traits
	#  dout -- directory to store all of the created image
	#  dtraits -- directory where all traits are stored
	#		Proper hierarchy is to have a subfolder within traits/ for each trait
	#		ex: traits/ contains [trait1/, trait2/, trait3/]
	#		    trait1/ contains [image1.png, image2.png, image3.png]
	#		    
	#		    In the test example, the mint green background is stored as 
	#			traits/trait1/bg1.png
	#		      the circle outline layer is stored as
	#			traits/trait2/circle.png
	#		      and the smiley emoji layer is stored as 
	#			traits/trait3/smile.png
	#		      and so on 
	#Code Blocks
	#  [100% done] Initializer: User sets nf,dout,dtraits. Reads in weights.dat. Finds all trait file locations within dtraits path
	#  [100% done] Generator: Loop through nt, randomly (w/ weights) grab traits (records usage)
	#	       use pillow to generate/export images and a text file with the metadata to the dout folder 
	#		Done:   loop through from 1:nf, weighted random snag of background
	#			loop through all other traits, randomly snag one and paste it onto the bg
	#			export the image, continue 1:nf loop
	#			keep a master list of used trait combos, check against it to prevent repeats
	#			export a list of image #'s and their traits
	#  [100% done] Output: Create a rarity table based on the master list, export it as a .csv

def main():
   #Initializer Block
	#Set these to what you want
	nf = 36 		#number of images to be created
	dout = 'images/'	#path to store generated images
	dtraits = 'traits/'	#path to traits

	#Reading in weights
	w=[]	
	with open('weights.dat') as f:
		for line in f:
			line = line.split('#',1)[0]
			line = line.rstrip()
			if(line != ''):
				w.append(line)
	#Reading in trait classes
	tclass=[]
	with open('tnames.dat') as f:
		for line in f:
			line=line.split('#',1)[0]
			line=line.rstrip()
			line=line.strip('\n')
			if(line != ''):
				tclass.append(line)
	
	#Finding all trait file locations with the dtraits path
	#    tl[# of traits,[# of options,[file path,weight]]] 
	tl=[]
	tnames=[]
	t=-1
	j=0
	tl.append(0)
	for dirnames in os.walk(dtraits):
		if(t>=0):
			dn = dirnames[0]
			temp = []
			k = 0
			for i in range(0,len(dirnames[2])):
				fn = [str(dn)+'/'+str(dirnames[2][i]),float(w[j])]
				name = dirnames[2][i]
				name = name.split('.',1)
				tnames.append(name[0])
				j = j+1
				temp.append(fn)
			temp2=[len(dirnames[2]),temp]
			tl.append(temp2)		
		t=t+1
	tl[0] = t
		
	tlist = []
	abc = 'abcdefghijklmnopqrztuvwxyz'
	exists=True

	#Loop to randomly create images
	for i in range(0,nf):
		safe=0
		while exists is True:
			safe=safe+1
			exists=False

			#Selecting Base Layer
			n = random.random()
			llen = tl[1][0]
			w1 = 0.00
			j = 0
			for x in range(0,llen):
				w2 = w1 + tl[1][1][x][1]
				if(n >= w1 and n<w2):
					j = x
				w1 = w2
			l1 = Image.open(tl[1][1][j][0])
			temp=abc[0]+str(j)+'.'

			#Randomly selecting other layers
			for k in range(2,tl[0]+1):
				n = random.random()
				llen = tl[k][0]
				w1 = 0.00
				j = 0
				for x in range(0,llen):
					w2 = w1 + tl[k][1][x][1]
					if(n >= w1 and n<w2):
						j = x
					w1 = w2
				
				l2 = Image.open(tl[k][1][j][0])
				l1.paste(l2,mask=l2)
				temp = temp+abc[k-1]+str(j)+'.'
			for z in tlist:
				if(temp==z):
					exists=True
			if(safe>1000):
				print('broke loop')
				break
		exists=True
		tlist.append(temp)

		#Export Image
		fout = dout+'image'+str(i)+'.png'
		l1.save(fout,quality=95)
		print('Image #'+str(i)+' exported')
	print('Done!')	
	
	#Calculate Rarity Table and Export Image to Trait Table
	rarity = np.zeros(len(w))
	icsv = open('imagetraits.csv','w')
	title = 'Image #,'
	for x in tclass:
		title=title+x+','
	title=title+'\n'
	icsv.write(title)
	inum=0
	for x in tlist:
		b=0
		lout = str(inum)+','
		x = x.split('.',t)
		for i in range(0,t):
			temp = x[i].split(abc[i],1)
			j = int(temp[1])
			kk = int(tl[i+1][0])
			for m in range(0,kk):
				if(j==m):
					rarity[b+j] = rarity[b+j]+1/nf
					lout=lout+tnames[b+j]+','
			b=b+kk
		lout=lout+'\n'
		icsv.write(lout)
		inum=inum+1
	icsv.close()
	
	#Export Rarity Table
	csv = open('rarity.csv','w')
	csv.write('Trait,Rarity\n')
	j = 0
	k = 1
	csv.write(tclass[0]+'\n')
	for i in range(0,len(rarity)):
		if(j==tl[k][0]):
			csv.write(tclass[k]+'\n')
			j = 0
			k=k+1
		csv.write(tnames[i]+','+str(rarity[i])+'\n')
		j = j+1
	csv.close()

if __name__ =='__main__':
	main()
