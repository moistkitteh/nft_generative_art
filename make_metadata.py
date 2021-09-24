import os

def main():
	###YOU NEED TO MANUALLY SET ALL OF THESE####
	iname = 'test name'					#default filename you used for your images you uploaded to pinata
	itype = '.png'  				#the file extension you exported with
	address= 'ipfs/[IPFSHASH]' 		#The IPFS hash to the directory all of your images are hosted at
	mpath = 'metadata/'				#The path to the local folder you want all your metadata files saved at
	descr = 'test description'			#The description you wanted saved in all of your metadata files


	#Reading in image and trait information
	traits=[]
	tnames=[]
	with open('imagetraits.csv') as f:
		for line in f:
			temp = []
			line = line.split(',')
			# ll = len(line)
			if(line[0] != 'Image #'):
				for x in line:
					if(x != '\n'):
						temp.append(x)
				traits.append(temp)
			else:
				for x in line:
					if(x != 'Image #' and x != '\n'):
						tnames.append(x)

	#Writing out metadata files
	for x in traits:
		num = x[0]
		json=open(mpath+iname+x[0]+'.json','w')
		json.write('{\n')
		json.write('\t"name": "'+iname+' #'+num+'",\n')
		json.write('\t"description": "'+descr+'",\n')
		json.write('\t"image": "'+address+'/'+num+itype+'",\n')
		json.write('\t"attributes":[\n')
		z = 0
		for y in x:
			if(y==x[0]):
				num = y
			else:	
				json.write('\t\t{\n')
				json.write('\t\t\t"trait_type": "'+tnames[z]+'",\n')
				json.write('\t\t\t"value": "'+y+'"\n')
				if(z==len(x)-2):
					json.write('\t\t}\n')
				else:
					json.write('\t\t},\n')
				z = z+1
		json.write('\t]\n')
		json.write('}')

if __name__ =='__main__':
        main()

