import os

def main():
	###YOU NEED TO MANUALLY SET ALL OF THESE####
	iname = 'image'					#default filename you used for your images you uploaded to pinata
	itype = '.png'  				#the file extension you exported with
	address= 'https://gateway.pinata.cloud/ipfs/' 	#The past to the directory all of your images are hosted at
	mpath = 'metadata/'				#The path to the local folder you want all your metadata files saved at
	descr = 'test description'			#The description you wanted saved in all of your metadata files


	#Reading in image and trait information
	traits=[]
	tnames=[]
	with open('imagetraits.csv') as f:
		for line in f:
			temp = []
			line = line.split(',')
			ll = len(line)
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
		json=open(mpath+iname+x[0]+'.json','w')
		json.write('{\n')
		json.write('\t"attributes":[\n')
		z = 0
		for y in x:
			if(y==x[0]):
				num = y
			else:
				json.write('\t\t{\n')
				json.write('\t\t\t"trait_type": "'+tnames[z]+'",\n')
				json.write('\t\t\t"value": "'+y+'"\n')
				json.write('\t\t}\n')
		json.write('\t\t],\n')
		json.write('\t\t"description": "'+descr+'",\n')
		json.write('\t\t"image": "'+address+'/'+iname+num+itype+'",\n')
		json.write('\t\t"name": "'+iname+' '+num+'"\n')
		json.write('}')

if __name__ =='__main__':
        main()
